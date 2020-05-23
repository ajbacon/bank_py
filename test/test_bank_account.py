import unittest
import os.path
import sys
sys.path.append(os.path.abspath('.'))

from lib.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        """should add the deposit the amount to the account balance and return updated balance"""
        account = BankAccount()
        self.assertEqual(account.deposit(1000), 1000)

    def test_withdraw(self):
        """should add the withdraw amount from the account balance and return updated balance"""
        account = BankAccount()
        account.deposit(1000)
        self.assertEqual(account.withdraw(500), 500)


if __name__ == "__main__":
    unittest.main()
