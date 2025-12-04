import unittest

import day4
import utils

PART_1_EXAMPLE = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(13, day4.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1416, day4.part_1_answer(utils.read_input_lines(4)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(43, day4.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(9086, day4.part_2_answer(utils.read_input_lines(4)))
