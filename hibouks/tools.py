from iso639 import Lang
from iso639.exceptions import InvalidLanguageValue


def to_int(value):
    try:
        data = int(value)
    except ValueError as val:
        print(f'{value} is not a valid integer')
        data = None
    except TypeError as typ:
        data = None
    finally:
        return data


def to_str(value):
    if isinstance(value, list):
        print(f'{value} is not a valid str')
        data = None
    elif isinstance(value, dict):
        print(f'{value} is not a valid str')
        data = None
    elif value is None:
        data = None
    else:
        data = str(value)
    return data


def to_languagecode(value):
    try:
        data = Lang(value).pt2t
    except InvalidLanguageValue as val:
        print(f'{value} is not a valid language')
        data = None
    finally:
        return data


def to_liststr(value):
    if isinstance(value, list):
        data = [str(k) for k in value]
    elif isinstance(value, str):
        data = [str(k).strip() for k in value.split('&')]
    elif value is None:
        data = None
    else:
        data = [str(value)]
    return data

def check_size(value: int, size=10) -> bool:
    try:
        data = False
        if len(str(value)) == size:
            data = True
    except ValueError as val:
        print(f'{value} is not a valid integer')
        data = False
    except TypeError as typ:
        data = False
    finally:
        return data
