import unittest
from add import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

if __name__ == "__main__":
    unittest.main()