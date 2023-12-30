class NumberConverter:
    def __init__(self):
        self._base_functions = {
            2 : bin,
            8 : oct,
            10 : int,
            16 : hex,
        }

    def convert(self, value, base_to, base_from=0):
        if base_from == 0:
            base_from = self.determine_base(value)

        if base_from not in self._base_functions.keys():
            pass # error
        if base_to not in self._base_functions.keys():
            pass # error

        int_value = int(value, base_from)
        return self._base_functions[base_to](int_value)

    def determine_base(self, value):
        if value.startswith('0b'): return 2
        elif value.startswith('0o'): return 8
        elif value.startswith('0x'): return 16
        elif len(value) > 0: return 10
        else: return -1 # not a valid base
