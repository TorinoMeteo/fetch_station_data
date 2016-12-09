import importlib


def parser_factory(type):
    path = 'realtime.fetch.parsers.%s'
    if type == 'txt-wd':
        mod = importlib.import_module(path % 'txtwd')
        return getattr(mod, 'TxtWdParser')
