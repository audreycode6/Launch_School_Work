import unittest
from perf_num import PerfectNumber

class PerfectNumberTest(unittest.TestCase):
    # @unittest.skip
    def test_initialize_perfect_number(self):
        try:
            PerfectNumber.classify(-1)
            self.fail("Expected exception not raised")
        except ValueError as e:
            self.assertEqual(str(e), "Input must be a positive integer")

    # @unittest.skip
    def test_classify_deficient(self):
        result = PerfectNumber.classify(13)
        self.assertEqual(result, "deficient")

    # @unittest.skip
    def test_classify_perfect(self):
        result = PerfectNumber.classify(28)
        self.assertEqual(result, "perfect")

    # @unittest.skip
    def test_classify_abundant(self):
        result = PerfectNumber.classify(12)
        self.assertEqual(result, "abundant")

if __name__ == "__main__":
    unittest.main()