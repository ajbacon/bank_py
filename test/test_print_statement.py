
import unittest
import io
from unittest.mock import patch, MagicMock, Mock, PropertyMock
import os.path
import sys
sys.path.append(os.path.abspath('.'))
from lib.print_statement import PrintStatement
from lib.transaction_history import TransactionHistory
# from lib.transaction import PrintStatement


class TestPrintStatement(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_printout(self, mock_stdout):

        history = TransactionHistory()
        history.add(1000, 'CREDIT', 0)
        history.add(500, 'DEBIT', 1000)

        printer = PrintStatement(history)
        printer.get_printout()
        expected = 'CREDIT: 1000.00, BALANCE: 1000.00\nDEBIT: 500.00, BALANCE: 500.00\n'
        self.assertEqual(mock_stdout.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()

    #    credit = MagicMock()
    #     category1 = PropertyMock(return_value='CREDIT')
    #     type(credit).category = category1
    #     print(credit.category)

    #     debit = MagicMock()
    #     category2 = PropertyMock(return_value='DEBIT')
    #     type(debit).category = category2
    #     print(debit.category)
