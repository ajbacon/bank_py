import unittest
import os.path
import sys
sys.path.append(os.path.abspath('.'))

from lib.transaction import Transaction


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.credit = Transaction(1000, 'CREDIT')

    def test_amount(self):
        """should have a property to return the amount"""
        self.assertEqual(self.credit.amount, 1000)

    def test_type_credit(self):
        """should have a type property of 'CREDIT' when a cre property to return the amount"""
        self.assertEqual(self.credit.amount, 1000)
        self.assertEqual(self.credit.category, 'CREDIT')


if __name__ == "__main__":
    unittest.main()
