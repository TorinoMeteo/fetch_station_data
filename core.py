import requests
import json

from .factory import parser_factory


class Data(dict):
    """ Wraps the python dict object to add convenience methods, i.e. as_json
    """
    def as_json(self):
        return json.dumps(self)


def fetch(url):
    """ Fetches an url content
    """
    response = requests.get(url).text
    return response


def parse(content, type):
    """ Parses the given cotent base upon type
    """
    klass = parser_factory(type)()
    return Data(klass.parse(content))
