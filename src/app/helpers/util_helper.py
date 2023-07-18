from datetime import datetime
from pytz import timezone
from dateutil import relativedelta

class DateUtil:
    def __init__(self, date_str, date_format="%Y-%m-%d"):
        self._date = datetime.strptime(date_str, date_format)

    @classmethod
    def new(cls, date_str, date_format="%Y-%m-%d"):
        '''
        create new datetime instance using date-formatted string (same as strptime method in datetime)
        :param date_str: date-formatted string
        :param date_format: date-format
        :return: instance of datetime
        '''
        return cls(date_str, date_format)._date

    @staticmethod
    def now():
        '''
        create new current datetime instance in Asia/Seoul timezone
        :return: instance of datetime
        '''
        return datetime.now(timezone('Asia/Seoul'))

    @staticmethod
    def diff(date1, date2):
        '''
        calculate difference of two datetime instance in days
        :param date1: augend (datetime instance)
        :param date2: operand2 (datetime instance)
        :return: difference of dates (In days)
        '''
        return (date1-date2).days

    @staticmethod
    def add(date, **kwargs):
        '''
        add date
        :param date: base date (datetime instance)
        :param kwargs: years, months, days, hours ..
        :return: instance of datetime
        '''
        return date + relativedelta.relativedelta(**kwargs)
