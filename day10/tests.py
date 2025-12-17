import unittest

import day10
import utils

PART_1_EXAMPLE = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(7, day10.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(512, day10.part_1_answer(utils.read_input_lines(10)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(33, day10.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(19857, day10.part_2_answer(utils.read_input_lines(10)))
