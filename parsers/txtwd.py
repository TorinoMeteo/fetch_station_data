from .abstract import Parser


class TxtWdParser(Parser):

    def parse(self, content):
        return {
            'key1': 'value1',
            'key2': 'value2',
        }
