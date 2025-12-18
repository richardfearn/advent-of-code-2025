import unittest

import day11
import utils

PART_1_EXAMPLE = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

PART_2_EXAMPLE = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(5, day11.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(555, day11.part_1_answer(utils.read_input_lines(11)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2, day11.part_2_answer(utils.to_lines(PART_2_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(502447498690860, day11.part_2_answer(utils.read_input_lines(11)))
