import unittest
from series import Series

class SeriesTest(unittest.TestCase):
    # @unittest.skip
    def test_simple_slices_of_one(self):
        series = Series("01234")
        self.assertEqual([[0], [1], [2], [3], [4]], series.slices(1))

    # @unittest.skip
    def test_simple_slices_of_one_again(self):
        series = Series("92834")
        self.assertEqual([[9], [2], [8], [3], [4]], series.slices(1))

    # @unittest.skip
    def test_simple_slices_of_two(self):
        series = Series("01234")
        self.assertEqual([[0, 1], [1, 2], [2, 3], [3, 4]], series.slices(2))

    # @unittest.skip
    def test_other_slices_of_two(self):
        series = Series("98273463")
        expected = [[9, 8], [8, 2], [2, 7], [7, 3], [3, 4], [4, 6], [6, 3]]
        self.assertEqual(expected, series.slices(2))

    # @unittest.skip
    def test_simple_slices_of_two_again(self):
        series = Series("37103")
        self.assertEqual([[3, 7], [7, 1], [1, 0], [0, 3]], series.slices(2))

    # @unittest.skip
    def test_simple_slices_of_three(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2], [1, 2, 3], [2, 3, 4]], series.slices(3))

    # @unittest.skip
    def test_simple_slices_of_three_again(self):
        series = Series("31001")
        self.assertEqual([[3, 1, 0], [1, 0, 0], [0, 0, 1]], series.slices(3))

    # @unittest.skip
    def test_other_slices_of_three(self):
        series = Series("982347")
        expected = [[9, 8, 2], [8, 2, 3], [2, 3, 4], [3, 4, 7]]
        self.assertEqual(expected, series.slices(3))

    # @unittest.skip
    def test_simple_slices_of_four(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2, 3], [1, 2, 3, 4]], series.slices(4))

    # @unittest.skip
    def test_simple_slices_of_four_again(self):
        series = Series("91274")
        self.assertEqual([[9, 1, 2, 7], [1, 2, 7, 4]], series.slices(4))

    # @unittest.skip
    def test_simple_slices_of_five(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2, 3, 4]], series.slices(5))

    # @unittest.skip
    def test_simple_slices_of_five_again(self):
        series = Series("81228")
        self.assertEqual([[8, 1, 2, 2, 8]], series.slices(5))

    # @unittest.skip
    def test_simple_slice_that_blows_up(self):
        series = Series("01234")
        with self.assertRaises(ValueError):
            series.slices(6)

    # @unittest.skip
    def test_more_complicated_slice_that_blows_up(self):
        slice_string = "01032987583"
        series = Series(slice_string)
        with self.assertRaises(ValueError):
            series.slices(len(slice_string) + 1)

if __name__ == "__main__":
    unittest.main()