import unittest

class EqualityTest(unittest.TestCase):
    def test_value_equality(self):
        lst1 = [1, 2, 3]
        lst2 = [1, 2, 3]

        self.assertEqual(lst1, lst2)
        self.assertIs(lst1, lst2)

if __name__ == "__main__":
    unittest.main()