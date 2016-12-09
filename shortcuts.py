from .core import fetch, parse


def fetch_data(url, type):
    content = fetch(url)
    data = parse(content, type)

    return data
