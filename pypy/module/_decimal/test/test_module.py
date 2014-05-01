class AppTestDecimalModule:
    spaceconfig = dict(usemodules=('_decimal',))

    def test_constants(self):
        import _decimal
        assert _decimal.IEEE_CONTEXT_MAX_BITS > 3

    def test_type(self):
        import _decimal
        assert isinstance(_decimal.Decimal, type)

    def test_contextflags(self):
        import _decimal
        from collections.abc import MutableMapping
        flags = _decimal.getcontext().flags
        assert type(flags).__name__ == 'SignalDict'
        bases = type(flags).__bases__
        assert bases[1] is MutableMapping

    def test_exceptions(self):
        import _decimal
        for name in ('Clamped', 'Rounded', 'Inexact', 'Subnormal',
                     'Underflow', 'Overflow', 'DivisionByZero',
                     'InvalidOperation', 'FloatOperation'):
            ex = getattr(_decimal, name)
            assert issubclass(ex, _decimal.DecimalException)
            assert issubclass(ex, ArithmeticError)

