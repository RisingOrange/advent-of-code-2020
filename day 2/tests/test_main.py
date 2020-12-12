import unittest

from main import *


class TestFoo(unittest.TestCase):

    def test_valid_password_1(self):
        self.assertEqual(is_password_valid('1-3 a', 'abcde'), True)

    def test_valid_password_2(self):
        self.assertEqual(is_password_valid('1-3 b', 'cdefg'), False)

    def test_valid_password_3(self):
        self.assertEqual(is_password_valid('2-9 c', 'ccccccccc'), True)


if __name__ == '__main__':
    unittest.main()
