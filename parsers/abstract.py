import re
import datetime


class Parser(object):
    """ Parser class interface
        - parse: parses the given content and returns a python dict of data
    """

    non_decimal = re.compile(r'[^\d.]+')

    def __init__(self, **kwargs):
        self.time_format = kwargs.get('time_format') or '%H:%M %p'
        self.date_format = kwargs.get('date_format') or '%d/%m/%Y'

    def parse(self, content):
        raise NotImplementedError("Should have implemented this")

    def _clean_temp(self, value):
        return float(self.non_decimal.sub('', value))

    def _clean_time(self, value):
        return datetime.datetime.strptime(value.strip(), self.time_format).time() # noqa

    def _clean_date(self, value):
        return datetime.datetime.strptime(value.strip(), self.date_format).date() # noqa
