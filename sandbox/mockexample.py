import datetime
# import unittest
# from unittest.mock import Mock

# # Save a couple of test days
# tuesday = datetime.datetime(year=2019, month=1, day=1)
# saturday = datetime.datetime(year=2019, month=1, day=5)

# # Mock datetime to control today's date
# datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


# class TestIsWeekdayModule(unittest.TestCase):

#     def test_is_weekday(self):
#         """test text"""
#         datetime.datetime.today.return_value = tuesday
#         self.assertEqual(is_weekday(), True)

#     def test_is_not_weekday(self):
#         """test text"""
#         datetime.datetime.today.return_value = saturday
#         self.assertEqual(is_weekday(), False)


# if __name__ == "__main__":
#     unittest.main()

# # Mock .today() to return Tuesday
# datetime.datetime.today.return_value = tuesday
# # Test Tuesday is a weekday
# print(is_weekday())
# # Mock .today() to return Saturday
# datetime.datetime.today.return_value = saturday
# # Test Saturday is not a weekday
# print(not is_weekday())
