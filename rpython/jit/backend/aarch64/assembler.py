
from rpython.jit.backend.aarch64.arch import WORD, JITFRAME_FIXED_SIZE
from rpython.jit.backend.aarch64.codebuilder import InstrBuilder
#from rpython.jit.backend.arm.locations import imm, StackLocation, get_fp_offset
#from rpython.jit.backend.arm.helper.regalloc import VMEM_imm_size
from rpython.jit.backend.aarch64.opassembler import ResOpAssembler
from rpython.jit.backend.aarch64.regalloc import (Regalloc,
#    CoreRegisterManager, check_imm_arg, VFPRegisterManager,
    operations as regalloc_operations)
#from rpython.jit.backend.arm import callbuilder
from rpython.jit.backend.aarch64 import registers as r
from rpython.jit.backend.llsupport import jitframe
from rpython.jit.backend.llsupport.assembler import BaseAssembler
from rpython.jit.backend.llsupport.regalloc import get_scale, valid_addressing_size
from rpython.jit.backend.llsupport.asmmemmgr import MachineDataBlockWrapper
from rpython.jit.backend.model import CompiledLoopToken
from rpython.jit.codewriter.effectinfo import EffectInfo
from rpython.jit.metainterp.history import AbstractFailDescr, FLOAT, INT, VOID
from rpython.jit.metainterp.resoperation import rop
from rpython.rlib.debug import debug_print, debug_start, debug_stop
from rpython.rlib.jit import AsmInfo
from rpython.rlib.objectmodel import we_are_translated, specialize, compute_unique_id
from rpython.rlib.rarithmetic import r_uint
from rpython.rtyper.annlowlevel import llhelper, cast_instance_to_gcref
from rpython.rtyper.lltypesystem import lltype, rffi
from rpython.rtyper.lltypesystem.lloperation import llop
from rpython.rlib.rjitlog import rjitlog as jl

class AssemblerARM64(ResOpAssembler):
    def assemble_loop(self, jd_id, unique_id, logger, loopname, inputargs,
                      operations, looptoken, log):
        clt = CompiledLoopToken(self.cpu, looptoken.number)
        clt._debug_nbargs = len(inputargs)
        looptoken.compiled_loop_token = clt

        if not we_are_translated():
            # Arguments should be unique
            assert len(set(inputargs)) == len(inputargs)

        self.setup(looptoken)

        frame_info = self.datablockwrapper.malloc_aligned(
            jitframe.JITFRAMEINFO_SIZE, alignment=WORD)
        clt.frame_info = rffi.cast(jitframe.JITFRAMEINFOPTR, frame_info)
        clt.frame_info.clear() # for now

        if log:
            operations = self._inject_debugging_code(looptoken, operations,
                                                     'e', looptoken.number)

        regalloc = Regalloc(assembler=self)
        allgcrefs = []
        operations = regalloc.prepare_loop(inputargs, operations, looptoken,
                                           allgcrefs)
        self.reserve_gcref_table(allgcrefs)
        functionpos = self.mc.get_relative_pos()

        self._call_header_with_stack_check()
        self._check_frame_depth_debug(self.mc)

        loop_head = self.mc.get_relative_pos()
        looptoken._ll_loop_code = loop_head
        #
        frame_depth_no_fixed_size = self._assemble(regalloc, inputargs, operations)
        self.update_frame_depth(frame_depth_no_fixed_size + JITFRAME_FIXED_SIZE)
        #
        size_excluding_failure_stuff = self.mc.get_relative_pos()

        self.write_pending_failure_recoveries()

        full_size = self.mc.get_relative_pos()
        rawstart = self.materialize_loop(looptoken)
        looptoken._ll_function_addr = rawstart + functionpos

        self.patch_gcref_table(looptoken, rawstart)
        self.process_pending_guards(rawstart)
        self.fixup_target_tokens(rawstart)

        if log and not we_are_translated():
            self.mc._dump_trace(rawstart,
                    'loop.asm')

        ops_offset = self.mc.ops_offset

        if logger:
            log = logger.log_trace(jl.MARK_TRACE_ASM, None, self.mc)
            log.write(inputargs, operations, ops_offset=ops_offset)

            # legacy
            if logger.logger_ops:
                logger.logger_ops.log_loop(inputargs, operations, 0,
                                           "rewritten", name=loopname,
                                           ops_offset=ops_offset)

        self.teardown()

        debug_start("jit-backend-addr")
        debug_print("Loop %d (%s) has address 0x%x to 0x%x (bootstrap 0x%x)" % (
            looptoken.number, loopname,
            r_uint(rawstart + loop_head),
            r_uint(rawstart + size_excluding_failure_stuff),
            r_uint(rawstart + functionpos)))
        debug_print("       gc table: 0x%x" % r_uint(rawstart))
        debug_print("       function: 0x%x" % r_uint(rawstart + functionpos))
        debug_print("         resops: 0x%x" % r_uint(rawstart + loop_head))
        debug_print("       failures: 0x%x" % r_uint(rawstart +
                                                 size_excluding_failure_stuff))
        debug_print("            end: 0x%x" % r_uint(rawstart + full_size))
        debug_stop("jit-backend-addr")

        return AsmInfo(ops_offset, rawstart + loop_head,
                       size_excluding_failure_stuff - loop_head)

    def setup(self, looptoken):
        BaseAssembler.setup(self, looptoken)
        assert self.memcpy_addr != 0, 'setup_once() not called?'
        if we_are_translated():
            self.debug = False
        self.current_clt = looptoken.compiled_loop_token
        self.mc = InstrBuilder()
        self.pending_guards = []
        #assert self.datablockwrapper is None --- but obscure case
        # possible, e.g. getting MemoryError and continuing
        allblocks = self.get_asmmemmgr_blocks(looptoken)
        self.datablockwrapper = MachineDataBlockWrapper(self.cpu.asmmemmgr,
                                                        allblocks)
        self.mc.datablockwrapper = self.datablockwrapper
        self.target_tokens_currently_compiling = {}
        self.frame_depth_to_patch = []

    def teardown(self):
        self.current_clt = None
        self._regalloc = None
        self.mc = None
        self.pending_guards = None

    def _build_failure_recovery(self, exc, withfloats=False):
        pass # XXX

    def _build_wb_slowpath(self, withcards, withfloats=False, for_frame=False):
        pass # XXX

    def build_frame_realloc_slowpath(self):
        pass

    def _build_propagate_exception_path(self):
        pass

    def _build_cond_call_slowpath(self, supports_floats, callee_only):
        pass

    def _build_stack_check_slowpath(self):
        self.stack_check_slowpath = 0  #XXX

    def _check_frame_depth_debug(self, mc):
        pass

    def update_frame_depth(self, frame_depth):
        baseofs = self.cpu.get_baseofs_of_frame_field()
        self.current_clt.frame_info.update_frame_depth(baseofs, frame_depth)

    def write_pending_failure_recoveries(self):
        pass # XXX

    def reserve_gcref_table(self, allgcrefs):
        pass

    def materialize_loop(self, looptoken):
        self.datablockwrapper.done()      # finish using cpu.asmmemmgr
        self.datablockwrapper = None
        allblocks = self.get_asmmemmgr_blocks(looptoken)
        size = self.mc.get_relative_pos() 
        res = self.mc.materialize(self.cpu, allblocks,
                                   self.cpu.gc_ll_descr.gcrootmap)
        #self.cpu.codemap.register_codemap(
        #    self.codemap.get_final_bytecode(res, size))
        return res

    def patch_gcref_table(self, looptoken, rawstart):
        pass

    def process_pending_guards(self, rawstart):
        pass

    def fixup_target_tokens(self, rawstart):
        for targettoken in self.target_tokens_currently_compiling:
            targettoken._ll_loop_code += rawstart
        self.target_tokens_currently_compiling = None

    def _call_header_with_stack_check(self):
        self._call_header()
        if self.stack_check_slowpath == 0:
            pass                # no stack check (e.g. not translated)
        else:
            endaddr, lengthaddr, _ = self.cpu.insert_stack_check()
            # load stack end
            self.mc.gen_load_int(r.ip.value, endaddr)          # load ip, [end]
            self.mc.LDR_ri(r.ip.value, r.ip.value)             # LDR ip, ip
            # load stack length
            self.mc.gen_load_int(r.lr.value, lengthaddr)       # load lr, lengh
            self.mc.LDR_ri(r.lr.value, r.lr.value)             # ldr lr, *lengh
            # calculate ofs
            self.mc.SUB_rr(r.ip.value, r.ip.value, r.sp.value) # SUB ip, current
            # if ofs
            self.mc.CMP_rr(r.ip.value, r.lr.value)             # CMP ip, lr
            self.mc.BL(self.stack_check_slowpath, c=c.HI)      # call if ip > lr

    def _call_header(self):
        stack_size = (len(r.callee_saved_registers) + 2) * WORD
        self.mc.STP_rr_preindex(r.fp.value, r.lr.value, r.sp.value, -stack_size)
        for i in range(0, len(r.callee_saved_registers), 2):
            self.mc.STP_rri(r.callee_saved_registers[i].value,
                            r.callee_saved_registers[i + 1].value,
                            r.sp.value,
                            (i + 2) * WORD)
        
        #self.saved_threadlocal_addr = 0   # at offset 0 from location 'sp'
        # ^^^XXX save it from register x1 into some place
        if self.cpu.supports_floats:
            XXX
            self.mc.VPUSH([reg.value for reg in r.callee_saved_vfp_registers])
            self.saved_threadlocal_addr += (
                len(r.callee_saved_vfp_registers) * 2 * WORD)

        # set fp to point to the JITFRAME, passed in argument 'x0'
        self.mc.MOV_rr(r.fp.value, r.x0.value)
        #
        gcrootmap = self.cpu.gc_ll_descr.gcrootmap
        if gcrootmap and gcrootmap.is_shadow_stack:
            self.gen_shadowstack_header(gcrootmap)

    def _assemble(self, regalloc, inputargs, operations):
        #self.guard_success_cc = c.cond_none
        regalloc.compute_hint_frame_locations(operations)
        self._walk_operations(inputargs, operations, regalloc)
        #assert self.guard_success_cc == c.cond_none
        frame_depth = regalloc.get_final_frame_depth()
        jump_target_descr = regalloc.jump_target_descr
        if jump_target_descr is not None:
            tgt_depth = jump_target_descr._arm_clt.frame_info.jfi_frame_depth
            target_frame_depth = tgt_depth - JITFRAME_FIXED_SIZE
            frame_depth = max(frame_depth, target_frame_depth)
        return frame_depth

    def _walk_operations(self, inputargs, operations, regalloc):
        self._regalloc = regalloc
        regalloc.operations = operations
        while regalloc.position() < len(operations) - 1:
            regalloc.next_instruction()
            i = regalloc.position()
            op = operations[i]
            self.mc.mark_op(op)
            opnum = op.getopnum()
            if rop.has_no_side_effect(opnum) and op not in regalloc.longevity:
                regalloc.possibly_free_vars_for_op(op)
            elif not we_are_translated() and op.getopnum() == rop.FORCE_SPILL:
                regalloc.prepare_force_spill(op)
            else:
                arglocs = regalloc_operations[opnum](regalloc, op)
                if arglocs is not None:
                    asm_operations[opnum](self, op, arglocs)
            if rop.is_guard(opnum):
                regalloc.possibly_free_vars(op.getfailargs())
            if op.type != 'v':
                regalloc.possibly_free_var(op)
            regalloc.possibly_free_vars_for_op(op)
            regalloc.free_temp_vars()
            regalloc._check_invariants()
        if not we_are_translated():
            self.mc.BRK()
        self.mc.mark_op(None)  # end of the loop
        regalloc.operations = None

    # regalloc support
    def load(self, loc, value):
        """load an immediate value into a register"""
        assert (loc.is_core_reg() and value.is_imm()
                    or loc.is_vfp_reg() and value.is_imm_float())
        if value.is_imm():
            self.mc.gen_load_int(loc.value, value.getint())
        elif value.is_imm_float():
            self.mc.gen_load_int(r.ip.value, value.getint())
            self.mc.VLDR(loc.value, r.ip.value)

    def _mov_stack_to_loc(self, prev_loc, loc):
        offset = prev_loc.value
        if loc.is_core_reg():
            assert prev_loc.type != FLOAT, 'trying to load from an \
                incompatible location into a core register'
            # unspill a core register
            assert 0 <= offset <= (1<<15) - 1
            self.mc.LDR_ri(loc.value, r.fp.value, offset)
            return
        xxx
        # elif loc.is_vfp_reg():
        #     assert prev_loc.type == FLOAT, 'trying to load from an \
        #         incompatible location into a float register'
        #     # load spilled value into vfp reg
        #     is_imm = check_imm_arg(offset)
        #     helper, save = self.get_tmp_reg()
        #     save_helper = not is_imm and save
        # elif loc.is_raw_sp():
        #     assert (loc.type == prev_loc.type == FLOAT
        #             or (loc.type != FLOAT and prev_loc.type != FLOAT))
        #     tmp = loc
        #     if loc.is_float():
        #         loc = r.vfp_ip
        #     else:
        #         loc, save_helper = self.get_tmp_reg()
        #         assert not save_helper
        #     helper, save_helper = self.get_tmp_reg([loc])
        #     assert not save_helper
        # else:
        #     assert 0, 'unsupported case'

        # if save_helper:
        #     self.mc.PUSH([helper.value], cond=cond)
        # self.load_reg(self.mc, loc, r.fp, offset, cond=cond, helper=helper)
        # if save_helper:
        #     self.mc.POP([helper.value], cond=cond)

    def regalloc_mov(self, prev_loc, loc):
        """Moves a value from a previous location to some other location"""
        if prev_loc.is_imm():
            return self._mov_imm_to_loc(prev_loc, loc)
        elif prev_loc.is_core_reg():
            self._mov_reg_to_loc(prev_loc, loc)
        elif prev_loc.is_stack():
            self._mov_stack_to_loc(prev_loc, loc)
        elif prev_loc.is_imm_float():
            self._mov_imm_float_to_loc(prev_loc, loc)
        elif prev_loc.is_vfp_reg():
            self._mov_vfp_reg_to_loc(prev_loc, loc)
        elif prev_loc.is_raw_sp():
            self._mov_raw_sp_to_loc(prev_loc, loc)
        else:
            assert 0, 'unsupported case'
    mov_loc_loc = regalloc_mov

    def gen_func_epilog(self, mc=None):
        gcrootmap = self.cpu.gc_ll_descr.gcrootmap
        if mc is None:
            mc = self.mc
        if gcrootmap and gcrootmap.is_shadow_stack:
            self.gen_footer_shadowstack(gcrootmap, mc)
        if self.cpu.supports_floats:
            XXX
        #    mc.VPOP([reg.value for reg in r.callee_saved_vfp_registers])

        # pop all callee saved registers

        stack_size = (len(r.callee_saved_registers) + 2) * WORD
        for i in range(0, len(r.callee_saved_registers), 2):
            mc.LDP_rri(r.callee_saved_registers[i].value,
                            r.callee_saved_registers[i + 1].value,
                            r.sp.value,
                            (i + 2) * WORD)
        mc.LDP_rr_postindex(r.fp.value, r.lr.value, r.sp.value, stack_size)

        mc.RET_r(r.lr.value)



def not_implemented(msg):
    msg = '[ARM/asm] %s\n' % msg
    if we_are_translated():
        llop.debug_print(lltype.Void, msg)
    raise NotImplementedError(msg)


def notimplemented_op(self, op, arglocs, regalloc):
    print "[ARM/asm] %s not implemented" % op.getopname()
    raise NotImplementedError(op)


asm_operations = [notimplemented_op] * (rop._LAST + 1)
asm_extra_operations = {}

for name, value in ResOpAssembler.__dict__.iteritems():
    if name.startswith('emit_opx_'):
        opname = name[len('emit_opx_'):]
        num = getattr(EffectInfo, 'OS_' + opname.upper())
        asm_extra_operations[num] = value
    elif name.startswith('emit_op_'):
        opname = name[len('emit_op_'):]
        num = getattr(rop, opname.upper())
        asm_operations[num] = value
