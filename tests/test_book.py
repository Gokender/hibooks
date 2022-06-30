from unittest import TestCase

from hibouks.book import Book, Collection, Dimension, Translation

class TestDimension(TestCase):
    def setUp(self) -> None:
        self.dim = Dimension()

    def test_dim_empty(self):
        self.assertIsNone(self.dim.height)
        self.assertIsNone(self.dim.width)

    def test_dim_values_int(self):
        self.dim.height = 200
        self.dim.width = 100
        self.assertEqual(self.dim.height, 200)
        self.assertEqual(self.dim.width, 100)

    def test_dim_values_str_good(self):
        self.dim.height = '200'
        self.dim.width = '100'
        self.assertEqual(self.dim.height, 200)
        self.assertEqual(self.dim.width, 100)

    def test_dim_values_str_wrong(self):
        self.dim.height = 'height'
        self.dim.width = 'width'
        self.assertIsNone(self.dim.height)
        self.assertIsNone(self.dim.width)

    def test_dim_to_dict(self):
        self.dim.height = 200
        self.dim.width = None
        result = {'width':None, 'height':200}
        self.assertDictEqual(self.dim.to_dict(), result)

class TestTranslation(TestCase):
    def setUp(self) -> None:
        self.trans = Translation()

    def test_trans_empty(self):
        self.assertIsNone(self.trans.original_lang)
        self.assertIsNone(self.trans.translators)

    def test_trans_original_lang_code_good(self):
        self.trans.original_lang = 'fr'
        self.assertEqual(self.trans.original_lang, 'fra')
    
    def test_trans_original_lang_str_good(self):
        self.trans.original_lang = 'French'
        self.assertEqual(self.trans.original_lang, 'fra')
    
    def test_trans_original_lang_str_false(self):
        self.trans.original_lang = 'Test'
        self.assertIsNone(self.trans.original_lang)

    def test_trans_original_lang_none(self):
        self.trans.original_lang = None
        self.assertIsNone(self.trans.original_lang)

    def test_trans_translators_list_str_one(self):
        self.trans.translators = ['Pierre Martin']
        self.assertListEqual(self.trans.translators, ['Pierre Martin'])

    def test_trans_translators_list_str_multiple(self):
        self.trans.translators = ['Pierre Martin', 'Martin Pierre']
        self.assertListEqual(self.trans.translators, ['Pierre Martin', 'Martin Pierre'])

    def test_trans_translators_list_int_one(self):
        self.trans.translators = [1]
        self.assertListEqual(self.trans.translators, ['1'])

    def test_trans_translators_list_int_multiple(self):
        self.trans.translators = [1, 2]
        self.assertListEqual(self.trans.translators, ['1', '2'])

    def test_trans_translators_str_one(self):
        self.trans.translators = 'Pierre Martin'
        self.assertListEqual(self.trans.translators, ['Pierre Martin'])
    
    def test_trans_translators_str_multiple(self):
        self.trans.translators = 'Pierre Martin & Martin Pierre'
        self.assertListEqual(self.trans.translators, ['Pierre Martin', 'Martin Pierre'])

    def test_trans_translators_none(self):
        self.trans.translators = None
        self.assertIsNone(self.trans.translators)
    
    def test_trans_to_dict(self):
        self.trans.original_lang = 'fr'
        self.trans.translators = 'Pierre Martin'
        result = {'original_lang': 'fra', 'translators': ['Pierre Martin']}
        self.assertDictEqual(self.trans.to_dict(), result)

class TestCollection(TestCase):
    def setUp(self) -> None:
        self.collec = Collection()

    def test_collec_empty(self):
        self.assertIsNone(self.collec.id)
        self.assertIsNone(self.collec.name)

    def test_collec_id_int(self):
        self.collec.id = 1
        self.assertEqual(self.collec.id, 1)

    def test_collec_id_str_good(self):
        self.collec.id = '1'
        self.assertEqual(self.collec.id, 1)

    def test_collec_id_str_bad(self):
        self.collec.id = 'a'
        self.assertIsNone(self.collec.id)

    def test_collec_id_float(self):
        self.collec.id = 1.0
        self.assertEqual(self.collec.id, 1)

    def test_collec_id_str_int_bad(self):
        self.collec.id = '1.0'
        self.assertIsNone(self.collec.id)

    def test_collec_name_str(self):
        self.collec.name = 'test'
        self.assertEqual(self.collec.name, 'test')

    def test_collec_name_int(self):
        self.collec.name = 1
        self.assertEqual(self.collec.name, '1')

    def test_collec_name_none(self):
        self.collec.name = None
        self.assertIsNone(self.collec.name)

    def test_collec_name_list(self):
        self.collec.name = ['test']
        self.assertIsNone(self.collec.name)

    def test_collec_to_dict(self):
        self.collec.name = {'test':1}
        self.assertIsNone(self.collec.name)

class TestBook(TestCase):
    def setUp(self) -> None:
        self.bo = Book()

    def test_book_empty(self):
        self.assertIsNone(self.bo.title)
        self.assertIsNone(self.bo.subtitle)
        self.assertIsNone(self.bo.original_title)
        self.assertIsNone(self.bo.authors)
        self.assertIsNone(self.bo.isbn10)
        self.assertIsNone(self.bo.isbn13)
        self.assertIsNone(self.bo.publisher)
        self.assertIsNone(self.bo.language)
        self.assertIsNone(self.bo.date_published)
        self.assertIsNone(self.bo.description)
        self.assertIsNone(self.bo.pages)

    def test_book_title_str(self):
        self.bo.title = 'test'
        self.assertEqual(self.bo.title, 'test')
        
    def test_book_title_int(self):
        self.bo.title = 1
        self.assertEqual(self.bo.title, '1')

    def test_book_title_none(self):
        self.bo.title = None
        self.assertIsNone(self.bo.title)

    def test_book_title_list(self):
        self.bo.title = []
        self.assertIsNone(self.bo.title)

    def test_book_subtitle_str(self):
        self.bo.subtitle = 'test'
        self.assertEqual(self.bo.subtitle, 'test')

    def test_book_subtitle_int(self):
        self.bo.subtitle = 1
        self.assertEqual(self.bo.subtitle, '1')

    def test_book_subtitle_none(self):
        self.bo.subtitle = None
        self.assertIsNone(self.bo.subtitle)

    def test_book_subtitle_list(self):
        self.bo.subtitle = []
        self.assertIsNone(self.bo.subtitle)

    def test_book_original_title_str(self):
        self.bo.original_title = 'test'
        self.assertEqual(self.bo.original_title, 'test')

    def test_book_original_title_int(self):
        self.bo.original_title = 1
        self.assertEqual(self.bo.original_title, '1')

    def test_book_original_title_none(self):
        self.bo.original_title = None
        self.assertIsNone(self.bo.original_title)

    def test_book_original_title_list(self):
        self.bo.original_title = []
        self.assertIsNone(self.bo.original_title)

    def test_book_authors_list_str_one(self):
        self.bo.authors = ['Pierre Martin']
        self.assertListEqual(self.bo.authors, ['Pierre Martin'])

    def test_book_authors_list_str_multiple(self):
        self.bo.authors = ['Pierre Martin', 'Martin Pierre']
        self.assertListEqual(self.bo.authors, ['Pierre Martin', 'Martin Pierre'])

    def test_book_authors_list_int_one(self):
        self.bo.authors = [1]
        self.assertListEqual(self.bo.authors, ['1'])

    def test_book_authors_list_int_multiple(self):
        self.bo.authors = [1, 2]
        self.assertListEqual(self.bo.authors, ['1', '2'])

    def test_book_authors_str_one(self):
        self.bo.authors = 'Pierre Martin'
        self.assertListEqual(self.bo.authors, ['Pierre Martin'])
    
    def test_book_authors_str_multiple(self):
        self.bo.authors = 'Pierre Martin & Martin Pierre'
        self.assertListEqual(self.bo.authors, ['Pierre Martin', 'Martin Pierre'])

    def test_book_authors_none(self):
        self.bo.authors = None
        self.assertIsNone(self.bo.authors)

    def test_book_isbn10_int_good(self):
        self.bo.isbn10 = 1000000000
        self.assertEqual(self.bo.isbn10, 1000000000)

    def test_book_isbn10_int_bad(self):
        self.bo.isbn10 = 100000000
        self.assertIsNone(self.bo.isbn10)

    def test_book_isbn10_str_good(self):
        self.bo.isbn10 = '1000000000'
        self.assertEqual(self.bo.isbn10, 1000000000)
    
    def test_book_isbn10_str_bad(self):
        self.bo.isbn10 = 'test'
        self.assertIsNone(self.bo.isbn10)

    def test_book_isbn13_int_good(self):
        self.bo.isbn13 = 1000000000000
        self.assertEqual(self.bo.isbn13, 1000000000000)

    def test_book_isbn13_int_bad(self):
        self.bo.isbn13 = 100000000
        self.assertIsNone(self.bo.isbn13)

    def test_book_isbn13_str_good(self):
        self.bo.isbn13 = '1000000000000'
        self.assertEqual(self.bo.isbn13, 1000000000000)
    
    def test_book_isbn13_str_bad(self):
        self.bo.isbn13 = 'test'
        self.assertIsNone(self.bo.isbn13)

    def test_book_translation_object(self):
        self.bo.translation = Translation()
        self.assertIsInstance(self.bo.translation, Translation)

    def test_book_translation_str(self):
        self.bo.translation = 'test'
        self.assertNotIsInstance(self.bo.translation, str)

    def test_book_publisher_str(self):
        self.bo.publisher = 'test'
        self.assertEqual(self.bo.publisher, 'test')

    def test_book_publisher_int(self):
        self.bo.publisher = 1
        self.assertEqual(self.bo.publisher, '1')

    def test_book_publisher_none(self):
        self.bo.publisher = None
        self.assertIsNone(self.bo.publisher)

    def test_book_publisher_list(self):
        self.bo.publisher = []
        self.assertIsNone(self.bo.publisher)

    def test_book_language_code_good(self):
        self.bo.language = 'fr'
        self.assertEqual(self.bo.language, 'fra')
    
    def test_book_language_str_good(self):
        self.bo.language = 'French'
        self.assertEqual(self.bo.language, 'fra')
    
    def test_book_language_str_false(self):
        self.bo.language = 'Test'
        self.assertIsNone(self.bo.language)

    def test_book_language_none(self):
        self.bo.language = None
        self.assertIsNone(self.bo.language)

    def test_book_date_published_str(self):
        self.bo.date_published = '2022-05-04'
        self.assertEqual(self.bo.date_published, '2022-05-04')

    def test_book_date_published_int(self):
        self.bo.date_published = 1
        self.assertEqual(self.bo.date_published, '1')

    def test_book_date_published_none(self):
        self.bo.date_published = None
        self.assertIsNone(self.bo.date_published)

    def test_book_date_published_list(self):
        self.bo.date_published = []
        self.assertIsNone(self.bo.date_published)

    def test_book_collection_object(self):
        self.bo.collection = Collection()
        self.assertIsInstance(self.bo.collection, Collection)

    def test_book_collection_str(self):
        self.bo.collection = 'test'
        self.assertNotIsInstance(self.bo.collection, str)

    def test_book_description_str(self):
        self.bo.description = 'test'
        self.assertEqual(self.bo.description, 'test')

    def test_book_description_int(self):
        self.bo.description = 1
        self.assertEqual(self.bo.description, '1')

    def test_book_description_none(self):
        self.bo.description = None
        self.assertIsNone(self.bo.description)

    def test_book_description_list(self):
        self.bo.description = []
        self.assertIsNone(self.bo.description)

    def test_book_pages_int(self):
        self.bo.pages = 1
        self.assertEqual(self.bo.pages, 1)

    def test_book_pages_str_good(self):
        self.bo.pages = '1'
        self.assertEqual(self.bo.pages, 1)

    def test_book_pages_str_bad(self):
        self.bo.pages = 'a'
        self.assertIsNone(self.bo.pages)

    def test_book_pages_float(self):
        self.bo.pages = 1.0
        self.assertEqual(self.bo.pages, 1)

    def test_book_pages_str_int_bad(self):
        self.bo.pages = '1.0'
        self.assertIsNone(self.bo.pages)

    def test_book_dimensions_object(self):
        self.bo.dimensions = Dimension()
        self.assertIsInstance(self.bo.dimensions, Dimension)

    def test_book_dimensions_str(self):
        self.bo.dimensions = 'test'
        self.assertNotIsInstance(self.bo.dimensions, str)