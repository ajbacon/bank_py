import unittest
import os.path
import sys
sys.path.append(os.path.abspath('.'))

from lib.transaction import Transaction


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.credit = Transaction(1000, 'CREDIT')
        self.debit = Transaction(500, 'DEBIT')

    def test_amount(self):
        """should have a property to return the amount"""
        self.assertEqual(self.credit.amount, 1000)

    def test_category_credit(self):
        """should have a property of category, which is set to either 'CREDIT' or 'DEBIT'"""
        self.assertEqual(self.credit.amount, 1000)
        self.assertEqual(self.credit.category, 'CREDIT')
        self.assertEqual(self.debit.amount, 500)
        self.assertEqual(self.debit.category, 'DEBIT')


if __name__ == "__main__":
    unittest.main()
