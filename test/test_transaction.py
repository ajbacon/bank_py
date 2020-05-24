import unittest
import os.path
import sys
sys.path.append(os.path.abspath('.'))

from lib.transaction import Transaction


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.credit = Transaction(1000, 'CREDIT', 500)
        self.debit = Transaction(500, 'DEBIT', 1000)

    def test_amount(self):
        """it should have a property to return the amount"""
        self.assertEqual(self.credit.amount, 1000)

    def test_category_credit(self):
        """it should have a property of category, which is set to either 'CREDIT' or 'DEBIT'"""
        self.assertEqual(self.credit.amount, 1000)
        self.assertEqual(self.credit.category, 'CREDIT')
        self.assertEqual(self.debit.amount, 500)
        self.assertEqual(self.debit.category, 'DEBIT')

    def test_update_balance_credit(self):
        """it should update and store the new balance after a credit transaction"""
        self.assertEqual(self.credit.balance, 1500)


if __name__ == "__main__":
    unittest.main()
