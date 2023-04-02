from tests.test_base import TestBase

class TestConvertBase(TestBase):
    def test_example1(self):
        num_as_str = "615"
        expected = "1A7"
        assert self.solve(num_as_str, 7, 13) == expected
    
    def test_example2(self):
        num_as_str = "-615"
        expected = "-1A7"
        assert self.solve(num_as_str, 7, 13) == expected
    
    def test_octal_hex(self):
        def extract_digits(num, convertor):
            num_str = convertor(num)
            num_str = num_str[0] + num_str[3:] if num < 0 else num_str[2:]
            num_str = num_str.upper()
            return num_str
        
        for num in range(-1000, 1001):
            bin_str = extract_digits(num, bin)
            oct_str = extract_digits(num, oct)
            hex_str = extract_digits(num, hex)
            assert self.solve(bin_str, 2, 8) == oct_str
            assert self.solve(bin_str, 2, 16) == hex_str
            assert self.solve(oct_str, 8, 2) == bin_str
            assert self.solve(oct_str, 8, 16) == hex_str
            assert self.solve(hex_str, 16, 2) == bin_str
            assert self.solve(hex_str, 16, 8) == oct_str