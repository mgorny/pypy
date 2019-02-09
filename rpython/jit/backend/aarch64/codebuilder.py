
from rpython.rlib.objectmodel import we_are_translated
from rpython.jit.backend.llsupport.asmmemmgr import BlockBuilderMixin
from rpython.jit.backend.aarch64.locations import RegisterLocation
from rpython.jit.backend.aarch64 import registers as r
from rpython.rlib.rarithmetic import intmask
from rpython.rtyper.lltypesystem import lltype, rffi
from rpython.tool.udir import udir


class AbstractAarch64Builder(object):
    def write32(self, word):
        self.writechar(chr(word & 0xFF))
        self.writechar(chr((word >> 8) & 0xFF))
        self.writechar(chr((word >> 16) & 0xFF))
        self.writechar(chr((word >> 24) & 0xFF))

    def RET_r(self, arg):
        self.write32((0b1101011001011111 << 16) | (arg << 5))

    def STP_rr_preindex(self, reg1, reg2, rn, offset):
        base = 0b1010100110
        assert -512 <= offset < 512
        assert offset & 0x7 == 0
        self.write32((base << 22) | ((0x7F & (offset >> 3)) << 15) |
                     (reg2 << 10) | (rn << 5) | reg1)

    def STP_rri(self, reg1, reg2, rn, offset):
        base = 0b1010100100
        assert -512 <= offset < 512
        assert offset & 0x7 == 0
        self.write32((base << 22) | ((0x7F & (offset >> 3)) << 15) |
                     (reg2 << 10) | (rn << 5) | reg1)

    def MOV_r_u16(self, rd, immed, shift):     # u16 is an unsigned 16-bit
        self.MOVK_r_u16(rd, immed, shift)

    def MOV_rr(self, rd, rn):
        self.ORR_rr(rd, r.xzr.value, rn)

    def ORR_rr(self, rd, rn, rm):
        base = 0b10101010000
        self.write32((base << 21) | (rm << 16) |
                     (rn << 5) | rd)

    def MOVK_r_u16(self, rd, immed, shift):
        base = 0b111100101
        assert 0 <= immed < 1 << 16
        assert shift in (0, 16, 32, 48)
        self.write32((base << 23) | (shift >> 4 << 21) | (immed << 5) | rd) 

    def MOVN_r_u16(self, rd, immed):
        base = 0b10010010100
        assert 0 <= immed < 1 << 16
        self.write32((base << 21) | (immed << 5) | rd)

    def ADD_ri(self, rd, rn, constant):
        base = 0b1001000100
        assert 0 <= constant < 4096
        self.write32((base << 22) | (constant << 10) |
                     (rn << 5) | rd)

    def LDP_rri(self, reg1, reg2, rn, offset):
        base = 0b1010100101
        assert -512 <= offset < 512
        assert offset & 0x7 == 0
        self.write32((base << 22) | ((0x7F & (offset >> 3)) << 15) |
                     (reg2 << 10) | (rn << 5) | reg1)

    def LDP_rr_postindex(self, reg1, reg2, rn, offset):
        base = 0b1010100011
        assert -512 <= offset < 512
        assert offset & 0x7 == 0
        self.write32((base << 22) | ((0x7F & (offset >> 3)) << 15) |
                     (reg2 << 10) | (rn << 5) | reg1)

    def LDR_ri(self, rt, rn, immed):
        base = 0b1111100101
        assert 0 <= immed <= 1<<15
        assert immed & 0x7 == 0
        immed >>= 3
        self.write32((base << 22) | (immed << 10) | (rn << 5) | rt)

    def ADD_rr(self, rd, rn, rm):
        base = 0b10001011000
        self.write32((base << 21) | (rm << 16) | (rn << 5) | (rd))

    def BRK(self):
        self.write32(0b11010100001 << 21)

    def gen_load_int(self, r, value):
        """r is the register number, value is the value to be loaded to the
        register"""
        shift = 0
        if value < 0:
            value = ~value
            nxt = intmask(value & 0xFFFF)
            self.MOVN_r_u16(r, nxt)
            value >>= 16
            shift += 16
        while value:
            nxt = intmask(value & 0xFFFF)
            self.MOV_r_u16(r, nxt, shift)
            value >>= 16
            shift += 16


class InstrBuilder(BlockBuilderMixin, AbstractAarch64Builder):

    def __init__(self, arch_version=7):
        AbstractAarch64Builder.__init__(self)
        self.init_block_builder()
        #
        # ResOperation --> offset in the assembly.
        # ops_offset[None] represents the beginning of the code after the last op
        # (i.e., the tail of the loop)
        self.ops_offset = {}

    def mark_op(self, op):
        pos = self.get_relative_pos()
        self.ops_offset[op] = pos

    def _dump_trace(self, addr, name, formatter=-1):
        if not we_are_translated():
            if formatter != -1:
                name = name % formatter
            dir = udir.ensure('asm', dir=True)
            f = dir.join(name).open('wb')
            data = rffi.cast(rffi.CCHARP, addr)
            for i in range(self.currpos()):
                f.write(data[i])
            f.close()

    def clear_cache(self, addr):
        if we_are_translated():
            startaddr = rffi.cast(llmemory.Address, addr)
            endaddr = rffi.cast(llmemory.Address,
                            addr + self.get_relative_pos())
            clear_cache(startaddr, endaddr)

    def copy_to_raw_memory(self, addr):
        self._copy_to_raw_memory(addr)
        self.clear_cache(addr)
        self._dump(addr, "jit-backend-dump", 'arm')

    def currpos(self):
        return self.get_relative_pos()
