#!/usr/bin/env python3

import unittest
from calc import calc

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = calc.Calc()

    def test_add(self):
        self.assertEqual(self.calculator.add(1,1), 2)

    def test_sub(self):
        self.assertEqual(self.calculator.sub(1,1), 0)

    def test_mul(self):
        self.assertEqual(self.calculator.mul(1,1), 1)

    def test_div(self):
        self.assertEqual(self.calculator.div(1,1), 1)

if __name__ == '__main__':
    unittest.main()
