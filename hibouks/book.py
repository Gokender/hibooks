from .tools import check_size, to_int, to_languagecode, to_liststr, to_str

class Dimension:
    def __init__(self) -> None:
        self._width = None
        self._height = None
    
    @property
    def width(self) -> str:
        return self._width

    @width.setter
    def width(self, value) -> None:
        self._width = to_int(value)

    @property
    def height(self) -> str:
        return self._height

    @height.setter
    def height(self, value) -> None:
        self._height = to_int(value)

    def to_dict(self) -> dict:
        return {k.lstrip('_'): v for k, v in vars(self).items()}


class Translation:
    def __init__(self) -> None:
        self._original_lang = None
        self._translators = None
    
    @property
    def original_lang(self) -> str:
        return self._original_lang

    @original_lang.setter
    def original_lang(self, value) -> None:
        self._original_lang = to_languagecode(value)

    @property
    def translators(self) -> list:
        return self._translators

    @translators.setter
    def translators(self, value) -> None:
        self._translators = to_liststr(value)
    
    def to_dict(self) -> dict:
        return {k.lstrip('_'): v for k, v in vars(self).items()}


class Collection:
    def __init__(self) -> None:
        self._name = None
        self._id = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = to_str(value)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value) -> None:
        self._id = to_int(value)

    def to_dict(self) -> dict:
        return {k.lstrip('_'): v for k, v in vars(self).items()}



class Book:
    def __init__(self):
        self._title = None
        self._subtitle = None
        self._original_title = None

        self._authors = None

        self._isbn10 = None
        self._isbn13 = None

        self._translation = Translation()

        self._publisher = None
        self._language = None
        self._date_published = None

        self._collection = Collection()

        self._description = None
        self._pages = None
        self._dimensions = Dimension()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value) -> None:
        self._title = to_str(value)

    @property
    def subtitle(self) -> str:
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value) -> None:
        self._subtitle = to_str(value)

    @property
    def original_title(self) -> str:
        return self._original_title

    @original_title.setter
    def original_title(self, value) -> None:
        self._original_title = to_str(value)

    @property
    def authors(self) -> list:
        return self._authors

    @authors.setter
    def authors(self, value) -> None:
        self._authors = to_liststr(value)

    @property
    def isbn10(self) -> int:
        return self._isbn10

    @isbn10.setter
    def isbn10(self, value) -> None:
        if check_size(to_int(value), 10):
            self._isbn10 = to_int(value)
        else:
            print(f'{value} is not valid isbn 10 code')

    @property
    def isbn13(self) -> int:
        return self._isbn13

    @isbn13.setter
    def isbn13(self, value) -> None:
        if check_size(to_int(value), 13):
            self._isbn13 = to_int(value)
        else:
            print(f'{value} is not valid isbn 13 code')

    @property
    def translation(self) -> Translation:
        return self._translation

    @translation.setter
    def translation(self, value: Translation) -> None:
        if isinstance(value, Translation):
            self._translation = value
        else:
            print(f'{value} is not valid Translation object')

    @property
    def publisher(self) -> str:
        return self._publisher

    @publisher.setter
    def publisher(self, value) -> None:
        self._publisher = to_str(value)

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, value) -> None:
        self._language = to_languagecode(value)

    #TODO: Control date format
    @property
    def date_published(self) -> str:
        return self._date_published

    @date_published.setter
    def date_published(self, value) -> None:
        self._date_published = to_str(value)

    @property
    def collection(self) -> Collection:
        return self._collection

    @collection.setter
    def collection(self, value: Collection) -> None:
        if isinstance(value, Collection):
            self._collection = value
        else:
            print(f'{value} is not valid Collection object')

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value) -> None:
        self._description = to_str(value)

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value) -> None:
        self._pages = to_int(value)

    @property
    def dimensions(self) -> Dimension:
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value: Dimension) -> None:
        if isinstance(value, Dimension):
            self._dimensions = value
        else:
            print(f'{value} is not valid Dimension object')

    def to_dict(self):
        data = {k.lstrip('_'): v for k, v in vars(self).items()}
        data['translation'] = data['translation'].to_dict()
        data['collection'] = data['collection'].to_dict()
        data['dimensions'] = data['dimensions'].to_dict()
        return data