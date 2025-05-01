import unittest
from roman_num import RomanNumeral

class RomanNumeralsTest(unittest.TestCase):
    # @unittest.skip
    def test_1(self):
        number = RomanNumeral(1)
        self.assertEqual(number.to_roman(), "I")

    # @unittest.skip
    def test_2(self):
        number = RomanNumeral(2)
        self.assertEqual(number.to_roman(), "II")

    # @unittest.skip
    def test_3(self):
        number = RomanNumeral(3)
        self.assertEqual(number.to_roman(), "III")

    # @unittest.skip
    def test_4(self):
        number = RomanNumeral(4)
        self.assertEqual(number.to_roman(), "IV")

    # @unittest.skip
    def test_5(self):
        number = RomanNumeral(5)
        self.assertEqual(number.to_roman(), "V")

    # @unittest.skip
    def test_6(self):
        number = RomanNumeral(6)
        self.assertEqual(number.to_roman(), "VI")

    # @unittest.skip
    def test_9(self):
        number = RomanNumeral(9)
        self.assertEqual(number.to_roman(), "IX")

    # @unittest.skip
    def test_27(self):
        number = RomanNumeral(27)
        self.assertEqual(number.to_roman(), "XXVII")

    # @unittest.skip
    def test_48(self):
        number = RomanNumeral(48)
        self.assertEqual(number.to_roman(), "XLVIII")

    # @unittest.skip
    def test_59(self):
        number = RomanNumeral(59)
        self.assertEqual(number.to_roman(), "LIX")

    # @unittest.skip
    def test_93(self):
        number = RomanNumeral(93)
        self.assertEqual(number.to_roman(), "XCIII")

    # @unittest.skip
    def test_141(self):
        number = RomanNumeral(141)
        self.assertEqual(number.to_roman(), "CXLI")

    # @unittest.skip
    def test_163(self):
        number = RomanNumeral(163)
        self.assertEqual(number.to_roman(), "CLXIII")

    # @unittest.skip
    def test_402(self):
        number = RomanNumeral(402)
        self.assertEqual(number.to_roman(), "CDII")

    # @unittest.skip
    def test_575(self):
        number = RomanNumeral(575)
        self.assertEqual(number.to_roman(), "DLXXV")

    # @unittest.skip
    def test_911(self):
        number = RomanNumeral(911)
        self.assertEqual(number.to_roman(), "CMXI")

    # @unittest.skip
    def test_1024(self):
        number = RomanNumeral(1024)
        self.assertEqual(number.to_roman(), "MXXIV")

    # @unittest.skip
    def test_3000(self):
        number = RomanNumeral(3000)
        self.assertEqual(number.to_roman(), "MMM")

if __name__ == "__main__":
    unittest.main()