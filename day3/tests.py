import unittest

import day3
import utils

PART_1_EXAMPLE = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(357, day3.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(16858, day3.part_1_answer(utils.read_input_lines(3)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3121910778619, day3.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(167549941654721, day3.part_2_answer(utils.read_input_lines(3)))
