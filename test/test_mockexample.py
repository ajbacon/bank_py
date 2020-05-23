import datetime
import unittest
from unittest.mock import patch
import os.path
import sys
sys.path.append(os.path.abspath('.'))
from sandbox.mockexample import is_weekday

# Save a test days before mock
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)


class TestIsWeekdayModule(unittest.TestCase):
    # def setUp(self)
    #     self.tues
    # tuesday = datetime.datetime(year=2019, month=1, day=1)
    # saturday = datetime.datetime(year=2019, month=1, day=5)

    @patch('sandbox.mockexample.datetime')
    def test_is_weekday(self, mock_datetime):
        """is weekday should be True"""
        mock_datetime.datetime.today.return_value = tuesday
        actual = is_weekday()
        mock_datetime.datetime.today.assert_called_once()
        self.assertEqual(actual, True)

    @patch('sandbox.mockexample.datetime')
    def test_is_not_weekday(self, mock_datetime):
        """is_weekday should be false"""
        mock_datetime.datetime.today.return_value = saturday
        actual = is_weekday()
        mock_datetime.datetime.today.assert_called_once()
        self.assertEqual(actual, False)


if __name__ == "__main__":
    unittest.main()
