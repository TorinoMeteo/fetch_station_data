import os
import json

from .abstract import Parser
from ..labels import DATA_LABELS as DL


class SintPiParser(Parser):

    # line num: (label, clean)
    data_map = {
        'last_measure_time': (DL['TIME'], 'time'),
        'last_measure_time': (DL['DATE'], 'date'),
        'temp_out': (DL['TEMP'], 'temp'),
        'TempOutMax': (DL['TEMP_MAX'], 'temp'),
        'TempOutMin': (DL['TEMP_MIN'], 'temp'),
        'hum_out': (DL['HUMIDITY'], 'humidity'),
        'UmOutMax': (DL['HUMIDITY_MAX'], 'humidity'),
        'UmOutMin': (DL['HUMIDITY_MIN'], 'humidity'),
        'dew_point': (DL['DEW'], 'dew'),
        'rel_pressure': (DL['PRESSURE'], 'pressure'),
        'PressureMax': (DL['PRESSURE_MAX'], 'pressure'),
        'PressureMin': (DL['PRESSURE_MIN'], 'pressure'),
        'wind_gust': (DL['WIND'], 'wind'),
        'wind_dir': (DL['WIND_DIR'], 'wind_dir'),
	'winDayGustMax': (DL['WIND_MAX'], 'wind'),
        'wind_dir_ave': (DL['WIND_DIR_MAX'], 'wind_dir'),
        'rain': (DL['RAIN'], 'rain'),
        'rain_rate_1h': (DL['RAIN_RATE'], 'rain_rate'),
	'rain_rate_24h': (DL['RAIN_RATE_MAX'], 'rain_rate'),
    }

    def parse(self, content):

        jsondata = json.loads(content)

        data = {}
        for k, i in self.data_map.iteritems():
            value = jsondata[k]
            value = getattr(self, '_clean_%s' % i[1].lower())(value)
            data[i[0]] = value
        return data
