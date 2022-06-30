from .tools import to_int, to_languagecode

class Dimension:
    def __init__(self):
        self._width = None
        self._height = None
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = to_int(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = to_int(value)

    def to_dict(self):
        return {k.lstrip('_'): v for k, v in vars(self).items()}


class Translation:
    def __init__(self):
        self._original_lang = None
        self._translators = None
    
    @property
    def original_lang(self):
        return self.original_lang

    @original_lang.setter
    def original_lang(self, value):
        pass#self._original_lang = to_geocode(value)