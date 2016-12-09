import os

from .abstract import Parser
from ..labels import DATA_LABELS as DL


class TxtWdParser(Parser):

    data_map = {
        4: DL['TEMP'],
    }

    def parse(self, content):
        lines = content.split(os.linesep)

        data = {}
        for k, l in self.data_map.iteritems():
            value = lines[k]
            value = getattr(self, '_clean_%s' % l.lower())(value)
            data[l] = value

        return data
