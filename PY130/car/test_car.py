import unittest
from car import Car

class CarTest(unittest.TestCase):
    def test_value_equality(self):
        car1 = Car()
        car2 = Car()

        car1.name = "Kim"
        car2.name = "Kim"

        self.assertEqual(car1, car2)

if __name__ == "__main__":
    unittest.main()