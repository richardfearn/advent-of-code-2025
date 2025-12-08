import unittest

import day8
import utils

PART_1_EXAMPLE = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(40, day8.part_1_answer(utils.to_lines(PART_1_EXAMPLE), 10))

    def test_with_input(self):
        self.assertEqual(57970, day8.part_1_answer(utils.read_input_lines(8), 1000))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(25272, day8.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(8520040659, day8.part_2_answer(utils.read_input_lines(8)))
