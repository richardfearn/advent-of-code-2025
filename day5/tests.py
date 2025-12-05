import unittest

import day5
import utils

PART_1_EXAMPLE = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3, day5.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(840, day5.part_1_answer(utils.read_input_lines(5)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(14, day5.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(359913027576322, day5.part_2_answer(utils.read_input_lines(5)))
