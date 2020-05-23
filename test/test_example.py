import unittest
import os.path
import sys

sys.path.append(os.path.abspath('.'))
from lib.something import TestClass


class Atest(unittest.TestCase):

    def test_example(self):
        tc = TestClass()
        self.assertEqual(tc.a_method(), 'i am a method')


if __name__ == "__main__":
    unittest.main()
