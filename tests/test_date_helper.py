import unittest
from datetime import datetime, timedelta

from dateutil import tz

from hermes_fix.utils import date_helper


class Test(unittest.TestCase):
    def setUp(self):
        pass


    """Daily: time < start < end"""
    def test_daily_t_s_e(self):
        self.tz = tz.gettz("UTC")

        dt  = datetime(2020, 2, 2, 10,0,0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(dt, self.tz, "11:00:00", "12:00:00")

        self.assertEqual(dt.date(), start.date())
        self.assertEqual(dt.date(), end.date())
        self.assertEqual(increment, timedelta(days=1))

    """Daily: start < time < end"""
    def test_daily_s_t_e(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 2, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "09:00:00", "12:00:00")

        self.assertEqual(dt.date(), start.date())
        self.assertEqual(dt.date(), end.date())
        self.assertEqual(increment, timedelta(days=1))

    """Daily: start < end < time"""
    def test_daily_s_e_t(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 2, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "08:00:00", "09:00:00")

        self.assertEqual(dt.date(), start.date())
        self.assertEqual(dt.date(), end.date())
        self.assertEqual(increment, timedelta(days=1))

    """Daily: time < end < start"""
    def test_daily_t_e_s(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 2, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "12:00:00", "11:00:00")

        self.assertEqual(start, datetime(2020, 2, 1, 12, 0, 0, tzinfo=self.tz))
        self.assertEqual(end, datetime(2020, 2, 2, 11, 0, 0, tzinfo=self.tz))
        self.assertEqual(increment, timedelta(days=1))

    """Daily: end < time < start"""
    def test_daily_e_t_s(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 2, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "12:00:00", "09:00:00")

        self.assertEqual(dt.date(), start.date())
        self.assertEqual(dt.date(), end.date() - timedelta(days=1))
        self.assertEqual(increment, timedelta(days=1))

    """Daily: end < start < time"""
    def test_daily_e_s_t(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 2, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "09:00:00", "08:00:00")

        self.assertEqual(dt.date(), start.date())
        self.assertEqual(dt.date(), end.date() - timedelta(days=1))
        self.assertEqual(increment, timedelta(days=1))

    """Weekly: time < start < end"""
    def test_weekly_t_s_e(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 4, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "Wednesday 11:00:00", "Friday 12:00:00")

        self.assertEqual(start, datetime(2020, 2, 5, 11, 0, 0, tzinfo=self.tz))
        self.assertEqual(end,  datetime(2020, 2, 7, 12, 0, 0, tzinfo=self.tz))
        self.assertEqual(increment, timedelta(days=7))

    """Weekly: start < time < end"""
    def test_weekly_s_t_e(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 5, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "Monday 11:00:00", "Friday 12:00:00")

        self.assertEqual(start, datetime(2020, 2, 3, 11, 0, 0, tzinfo=self.tz))
        self.assertEqual(end,  datetime(2020, 2, 7, 12, 0, 0, tzinfo=self.tz))
        self.assertEqual(increment, timedelta(days=7))

    """Weekly: start < end < time """
    def test_weekly_s_e_t(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 7, 15, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "Monday 11:00:00", "Friday 12:00:00")

        self.assertEqual(start, datetime(2020, 2, 10, 11, 0, 0, tzinfo=self.tz))
        self.assertEqual(end,  datetime(2020, 2, 14, 12, 0, 0, tzinfo=self.tz))
        self.assertEqual(increment, timedelta(days=7))

    """Weekly: time < end < start"""
    def test_weekly_t_e_s(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 4, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "Friday 11:00:00", "Wednesday 12:00:00")

        self.assertEqual(start, datetime(2020, 1, 31, 11, 0, 0, tzinfo=self.tz))
        self.assertEqual(end,  datetime(2020, 2, 5, 12, 0, 0, tzinfo=self.tz))
        self.assertEqual(increment, timedelta(days=7))

    """Weekly: end < time < start"""
    def test_weekly_e_t_s(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 4, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "Friday 11:00:00", "Monday 12:00:00")

        self.assertEqual(start, datetime(2020, 2, 7, 11, 0, 0, tzinfo=self.tz))
        self.assertEqual(end,  datetime(2020, 2, 10, 12, 0, 0, tzinfo=self.tz))
        self.assertEqual(increment, timedelta(days=7))

    """Weekly: end < start < time"""
    def test_weekly_e_s_t(self):
        self.tz = tz.gettz("UTC")

        dt = datetime(2020, 2, 7, 10, 0, 0, tzinfo=self.tz)
        start, end, increment = date_helper.get_session_times(
            dt, self.tz, "Thursday 11:00:00", "Monday 12:00:00")

        self.assertEqual(start, datetime(2020, 2, 6, 11, 0, 0, tzinfo=self.tz))
        self.assertEqual(end,  datetime(2020, 2, 10, 12, 0, 0, tzinfo=self.tz))
        self.assertEqual(increment, timedelta(days=7))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
