import unittest

from main import *

example = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''.strip()

round_1 = '''
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
'''.strip()

round_2 = '''
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
'''.strip()

round_3 = '''
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
'''.strip()

round_4 = '''
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
'''.strip()

round_5 = '''
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
'''.strip()

def print_grids(grid_a, grid_b):
    print()
    print(grid_to_string(grid_a))
    print()
    print(grid_to_string(grid_b))

class TestFoo(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(apply_rules_until_stable(to_grid(example), cell_transform_1), 37)

    def test_round_1(self):
        result, _ = apply_rules_to_every_cell(to_grid(example), cell_transform_1)
        expected = to_grid(round_1)
        print_grids(result, expected)
        self.assertEqual(result, expected)

    def test_round_2(self):
        result, _ = apply_rules_to_every_cell(to_grid(round_1), cell_transform_1)
        expected = to_grid(round_2)
        print_grids(result, expected)
        self.assertEqual(result, expected)

    def test_round_3(self):
        result, _ = apply_rules_to_every_cell(to_grid(round_2), cell_transform_1)
        expected = to_grid(round_3)
        print_grids(result, expected)
        self.assertEqual(result, expected)

    def test_round_4(self):
        result, _ = apply_rules_to_every_cell(to_grid(round_3), cell_transform_1)
        expected = to_grid(round_4)
        print_grids(result, expected)
        self.assertEqual(result, expected)

    def test_round_5(self):
        result, _ = apply_rules_to_every_cell(to_grid(round_4), cell_transform_1)
        expected = to_grid(round_5)
        print_grids(result, expected)
        self.assertEqual(result, expected)

    def test_stable(self):
        result, _ = apply_rules_to_every_cell(to_grid(round_5), cell_transform_1)
        expected = to_grid(round_5)
        print_grids(result, expected)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
