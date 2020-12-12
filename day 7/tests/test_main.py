import unittest

from main import *

rules = '''
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''.strip()

class TestFoo(unittest.TestCase):

    def test_parse_rules(self):
        print(parse_rules('muted tomato bags contain 1 bright brown bag, 1 dotted gold bag, 2 faded gray bags, 1 posh yellow bag.'))

    def test_amount_contained_bags(self):
        self.assertEqual(amount_descendants('shiny gold', parse_rules(rules)), 126)

    def test_amount_contained_bags(self):
        self.assertEqual(amount_descendants('shiny gold', parse_rules(rules)), 126)


if __name__ == '__main__':
    unittest.main()
