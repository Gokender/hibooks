from bs4 import BeautifulSoup

with open('./twyford.htm') as infile:
    data = infile.read()


class Dimension:
    def __init__(self):
        self._width = None
        self._height = None
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        try:
            self._width = int(value)
        except Exception as exc:
            print(exc)
        #self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def to_dict(self):
        return {k.lstrip('_'): v for k, v in vars(self).items()}

class BookDetail:
    def __init__(self):
        self.title = ''
        self.subtitle = ''
        self.original_title = ''

        self.authors = []

        self.isbn10 = ''
        self.isbn13 = ''

        self.original_lang = ''
        self.translators = []

        self.publisher = ''
        self.language = ''
        self.date_published = None

        self.collection_name = ''
        self.collection_id = None

        self.description = ''
        self.pages = None
        self.dimensions = Dimension()

    def to_dict(self):
        data = {k.lstrip('_'): v for k, v in vars(self).items()}
        data['dimensions'] = data['dimensions'].to_dict()
        return data


dim = Dimension()
print('1', dim.__dict__)

dim.height = 205
print(dim.to_dict())

detail = BookDetail()
detail.dimensions.width = 140.0
detail.dimensions.height = 205
print(detail.to_dict())

soup_root = BeautifulSoup(data, 'html.parser')
soup_book = soup_root.find('div', attrs={'class':'book_detail'})

#print(soup_book)
author = soup_book.find('h3').text.strip()
title = soup_book.find('h1').text.strip()

if soup_book.find('span', attrs={'class':'original_title'}):
    title_original = soup_book.find('span', attrs={'class':'original_title'}).text.replace('[', '').replace(']', '')
else:
    title_original = None

#print(author, title, title_original)

print(int('140.0'))