import os

from .abstract import Parser
from ..labels import DATA_LABELS as DL


class TxtWdParser(Parser):

    data_map = {
        4: (DL['TEMP'], 'temp'),
        5: (DL['TEMP_MAX'], 'temp'),
        7: (DL['TEMP_MIN'], 'temp'),
    }

    def parse(self, content):
        lines = content.split(os.linesep)

        data = {}
        for k, i in self.data_map.iteritems():
            value = lines[k]
            value = getattr(self, '_clean_%s' % i[1].lower())(value)
            data[i[0]] = value

        return data
