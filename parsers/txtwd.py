import os

from .abstract import Parser
from ..labels import DATA_LABELS as DL


class TxtWdParser(Parser):

    # line num: (label, clean)
    data_map = {
        1: (DL['TIME'], 'time'),
        2: (DL['DATE'], 'date'),
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

"""
1=>"observation_time",
2=>"observation_date",
6=>"temp_max_time",
8=>"temp_min_time",
16=>"relative_humidity",
17=>"relative_humidity_max",
18=>"relative_humidity_max_time",
19=>"relative_humidity_min",
20=>"relative_humidity_min_time",
22=>"dewpoint",
23=>"dewpoint_max",
24=>"dewpoint_max_time",
25=>"dewpoint_min",
26=>"dewpoint_min_time",
28=>"pressure",
29=>"pressure_max",
30=>"pressure_max_time",
31=>"pressure_min",
32=>"pressure_min_time",
34=>"wind_strength",
35=>"wind_dir",
36=>"wind_strength_max",
37=>"wind_dir_max",
38=>"wind_max_time",
40=>"rain",
41=>"rain_rate",
42=>"rain_rate_max",
43=>"rain_rate_max_time",
44=>"rain_month",
45=>"rain_year"
"""
