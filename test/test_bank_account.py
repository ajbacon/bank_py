import unittest
import os.path
import sys
sys.path.append(os.path.abspath('.'))

from lib.bank_account import BankAccount


class Atest(unittest.TestCase):

    def test_deposit(self):
        """should add the deposit to the account balance and return updated balance"""
        account = BankAccount()
        self.assertEqual(account.deposit(1000), 1000)


if __name__ == "__main__":
    unittest.main()
