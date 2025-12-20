import unittest

import day12
import utils

PART_1_EXAMPLE = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""


class Part1Tests(unittest.TestCase):

    @unittest.skip
    def test_example(self):
        self.assertEqual(2, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(469, day12.part_1_answer(utils.read_input_lines(12)))
