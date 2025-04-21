import unittest

# EXERCISES functions to test
def not_even(value): # 1
    return value % 2 != 0

def xyz_equal(value): # 2
    return value.lower()

class TestExercises(unittest.TestCase):
    def test_not_even(self):
        value = 7
        self.assertTrue(not_even(value))
        with self.assertRaises(AssertionError):
            value = 6
            self.assertTrue(not_even(value), "value is not odd") # fails

    def test_xyz_equal(self):
        value = "XYZ"
        self.assertEqual(xyz_equal(value), 'xyz')

        value2 = "ABC"
        with self.assertRaises(AssertionError):
            self.assertEqual(xyz_equal(value2), 'xyz', "value is not xyz") # fails

    def test_is_none(self):
        value = None
        self.assertIsNone(value)

        value = "hi"
        with self.assertRaises(AssertionError):
            self.assertIsNone(value, "value is not None")

    def test_in(self):
        lst = [1, 2, 'xyz']
        value = 'xyz'
        self.assertIn(value, lst)

        with self.assertRaises(AssertionError):
            lst = [1, 2, 3]
            self.assertIn(value, lst)

    def test_not_in(self):
        lst = [1, 2, 3]
        self.assertNotIn('xyz', lst)




if __name__ == '__main__':
    unittest.main()
    





