import unittest

from mathProblems import SquareRoot
from mathProblems import Logarithm


class MyTestCase(unittest.TestCase):
    def test_squareRoot(self):
        self.assertEqual(5, SquareRoot.squareRoot(25))

    def test_logarithm(self):
        self.assertEqual(3, Logarithm.logarithm(729,9))


if __name__ == '__main__':
    unittest.main()
