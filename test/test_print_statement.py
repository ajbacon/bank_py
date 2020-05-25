
import unittest
import io
from unittest.mock import patch, MagicMock, Mock, PropertyMock
import os.path
import sys
sys.path.append(os.path.abspath('.'))
from lib.print_statement import PrintStatement


class TestPrintStatement(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_printout(self, mock_stdout):

        credit = MagicMock()
        amount1 = PropertyMock(return_value=1000)
        category1 = PropertyMock(return_value='CREDIT')
        balance1 = PropertyMock(return_value=1000)
        type(credit).amount = amount1
        type(credit).category = category1
        type(credit).balance = balance1

        debit = MagicMock()
        amount1 = PropertyMock(return_value=250)
        category1 = PropertyMock(return_value='DEBIT')
        balance1 = PropertyMock(return_value=750)
        type(debit).amount = amount1
        type(debit).category = category1
        type(debit).balance = balance1

        history = MagicMock()
        history.get_history.return_value = [credit, debit]

        printer = PrintStatement(history)
        printer.get_printout()
        expected = 'CREDIT: 1000.00, BALANCE: 1000.00\nDEBIT: 250.00, BALANCE: 750.00\n'
        self.assertEqual(mock_stdout.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
