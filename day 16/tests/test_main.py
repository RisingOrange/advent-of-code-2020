import unittest

from main import *

example = '''
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''.strip()

class TestFoo(unittest.TestCase):

    def test_field_order(self):
        fields, my_ticket, other_tickets = parse_input(example)
        self.assertEqual(field_order(fields, valid_tickets(fields, other_tickets + [my_ticket])), ['row', 'class', 'seat'])


if __name__ == '__main__':
    unittest.main()
