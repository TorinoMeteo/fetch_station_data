import importlib


def parser_factory(type):
    """ Factory method to retrieve the parse class to be used with
        contents formatted as type
    """
    path = 'realtime.fetch.parsers.%s'
    if type == 'txt-wd':
        mod = importlib.import_module(path % 'txtwd')
        return getattr(mod, 'TxtWdParser')
