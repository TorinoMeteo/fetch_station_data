import importlib


def parser_factory(type):
    """ Factory method to retrieve the parse class to be used with
        contents formatted as type
    """
    path = '.parsers.%s'
    if type == 'txt-wd':
        mod = importlib.import_module(
            path % 'txtwd', __name__.rsplit('.', 1)[0]
        )
        return getattr(mod, 'TxtWdParser')
