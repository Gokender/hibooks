from iso639 import Lang
from iso639.exceptions import InvalidLanguageValue


def to_int(value):
    try:
        data = int(value)
    except ValueError as val:
        print(f'{value} is not a valid integer.')
        data = None
    except TypeError as typ:
        data = None
    finally:
        return data


def to_languagecode(value):
    try:
        data = Lang(value).pt2t
    except InvalidLanguageValue as val:
        print(f'{value} is not a valid language')
        data = None
    #except TypeError as typ:
    #    data = None
    finally:
        return data
