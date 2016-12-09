import requests
import json

from .factory import parser_factory


class Data(dict):
    def as_json(self):
        return json.dumps(self)


def fetch(url):
    response = requests.get(url).text
    return response


def parse(content, type):
    klass = parser_factory(type)()
    return Data(klass.parse(content))
