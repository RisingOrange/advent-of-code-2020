import unittest

from main import *


class TestFoo(unittest.TestCase):

    def test_chinese_remainder_1(self):
        modulos = [3,5,7]
        vals = [2,3,2]
        self.assertEqual(chinese_remainder(modulos, vals), 23)
    


if __name__ == '__main__':
    unittest.main()
