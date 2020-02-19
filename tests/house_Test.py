import unittest

from makingHouses import SummerHouse
from makingHouses import WinterHouse

"""
This script helps with the unittest
"""


class MyTestCase(unittest.TestCase):

    def test_creating_a_SummerHouse(self):
        wildwood_house = SummerHouse("Small", "Red", 3, 5, False)
        color = wildwood_house.get_color()
        self.assertEqual("Red", color)

    def test_get_garage_info(self):
        wildwood_house = SummerHouse("Big", "Blue", 6, 10, True)
        garage = wildwood_house.do_We_Need_garage()
        self.assertEqual("Yes, we need a garage!", garage)

    def test_creating_a_winterHouse(self):
        london_house = WinterHouse("Medium", "Red and Blue", 5, 5, False)
        size = london_house.get_size()
        self.assertEqual("Medium", size)

    def test_get_garage_info2(self):
        london_house = WinterHouse("Small", "Green", 3, 2, True)
        garage = london_house.do_We_Need_garage()
        self.assertEqual("No, we do not need a garage!", garage)


if __name__ == '__main__':
    unittest.main()
