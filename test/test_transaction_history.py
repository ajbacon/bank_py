import unittest
from unittest.mock import patch, MagicMock
import os.path
import sys
sys.path.append(os.path.abspath('.'))
from lib.transaction_history import TransactionHistory
from lib.transaction import Transaction


class TestTransactionHistory(unittest.TestCase):

    def setUp(self):
        self.history = TransactionHistory()

    @patch('lib.transaction_history.Transaction')
    def test_add(self, mock_transaction):
        """it should add a new transaction and return that transaction"""
        transaction_instance = MagicMock()
        mock_transaction.return_value = transaction_instance
        transaction = self.history.add(1000, 'CREDIT', 500)

        mock_transaction.assert_called_with(1000, 'CREDIT', 500)
        self.assertEqual(transaction, transaction_instance)


if __name__ == "__main__":
    unittest.main()
