import unittest

import day2
import utils

PART_1_EXAMPLE = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1227775554, day2.part_1_answer(utils.join_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(53420042388, day2.part_1_answer(utils.read_input(2)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(4174379265, day2.part_2_answer(utils.join_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(69553832684, day2.part_2_answer(utils.read_input(2)))
