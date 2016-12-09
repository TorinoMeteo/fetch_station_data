from .core import fetch, parse


def fetch_data(url, type):
    """ Fetches url content and parses data based upon type
        Returns a fetch.core.Data object, which is a python
        dict with some convenience methods, i.e. as_json
    """
    content = fetch(url)
    data = parse(content, type)

    return data
