# flake8: noqa

import unittest

import day6
import utils

PART_1_EXAMPLE = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(4277556, day6.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(5595593539811, day6.part_1_answer(utils.read_input_lines(6)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3263827, day6.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(10153315705125, day6.part_2_answer(utils.read_input_lines(6)))
