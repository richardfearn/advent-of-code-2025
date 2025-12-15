import unittest

import day9
import utils

PART_1_EXAMPLE = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(50, day9.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(4750092396, day9.part_1_answer(utils.read_input_lines(9)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(24, day9.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1468516555, day9.part_2_answer(utils.read_input_lines(9)))
