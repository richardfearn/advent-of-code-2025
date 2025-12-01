import unittest

import day1
import utils

PART_1_EXAMPLE = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3, day1.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1152, day1.part_1_answer(utils.read_input_lines(1)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(6, day1.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(6671, day1.part_2_answer(utils.read_input_lines(1)))
