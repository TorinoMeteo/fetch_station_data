import re


class Parser(object):
    """ Parser class interface
        - parse: parses the given content and returns a python dict of data
    """

    non_decimal = re.compile(r'[^\d.]+')

    def parse(content):
        raise NotImplementedError("Should have implemented this")

    def _clean_temp(self, value):
        return float(self.non_decimal.sub('', value))
