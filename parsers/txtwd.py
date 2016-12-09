import os

from .abstract import Parser
from ..labels import DATA_LABELS as DL


class TxtWdParser(Parser):

    data_map = (
        ('temp', 4),
        ('temp_max', 5),
    )

    def parse(self, content):
        lines = content.split(os.linesep)
        print lines
        return {
            DL['TEMP']: 40,
        }
