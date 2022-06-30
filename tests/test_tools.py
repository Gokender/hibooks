from unittest import TestCase

from hibouks.tools import to_int, to_languagecode, to_liststr, to_str, check_size

class TestTools(TestCase):

    def test_to_int_int(self):
        value = to_int(67890)
        result = 67890
        self.assertEqual(value, result)
    
    def test_to_int_str_int(self):
        value = to_int('12345')
        result = 12345
        self.assertEqual(value, result)

    def test_to_int_float(self):
        value = to_int(3.14)
        result = 3
        self.assertEqual(value, result)
    
    def test_to_int_bin(self):
        value = to_int(0b010101)
        result = 21
        self.assertEqual(value, result)
    
    def test_to_int_hexa(self):
        value = to_int(0xFE)
        result = 254
        self.assertEqual(value, result)

    def test_to_int_str(self):
        value = to_int('Not convertible')
        result = None
        self.assertEqual(value, result)
    
    def test_to_int_str_float(self):
        value = to_int('104.0')
        result = None
        self.assertEqual(value, result)
    
    def test_to_int_list(self):
        value = to_int([1])
        result = None
        self.assertEqual(value, result)

    def test_to_languagecode_fr(self):
        value = to_languagecode('fr')
        result = 'fra'
        self.assertEqual(value, result)
    
    def test_to_languagecode_france(self):
        value = to_languagecode('france')
        self.assertIsNone(value)

    def test_to_languagecode_French(self):
        value = to_languagecode('French')
        result = 'fra'
        self.assertEqual(value, result)

    def test_to_languagecode_None(self):
        value = to_languagecode(None)
        self.assertIsNone(value)

    def test_to_languagecode_str(self):
        value = to_languagecode('This is a test')
        self.assertIsNone(value)

    def test_to_liststr_empty(self):
        value = to_liststr(None)
        self.assertIsNone(value)
    
    def test_to_liststr_str_one(self):
        value = to_liststr('test')
        result = ['test']
        self.assertListEqual(value, result)
    
    def test_to_liststr_str_multiple(self):
        value = to_liststr('test1 & test2')
        result = ['test1', 'test2']
        self.assertListEqual(value, result)
    
    def test_to_liststr_list_one(self):
        value = to_liststr(['test1'])
        result = ['test1']
        self.assertListEqual(value, result)
    
    def test_to_liststr_list_multiple(self):
        value = to_liststr(['test1', 'test2'])
        result = ['test1', 'test2']
        self.assertListEqual(value, result)

    def test_to_liststr_int(self):
        value = to_liststr(1)
        result = ['1']
        self.assertListEqual(value, result)

    def test_to_str_int(self):
        value = to_str(1)
        result = '1'
        self.assertEqual(value, result)
    
    def test_to_str_str(self):
        value = to_str('test')
        result = 'test'
        self.assertEqual(value, result)
    
    def test_to_str_none(self):
        value = to_str(None)
        self.assertIsNone(value)

    def test_to_str_dict(self):
        value = to_str({'test':1})
        self.assertIsNone(value)

    def test_to_str_list(self):
        value = to_str([])
        self.assertIsNone(value)

    def test_check_size_int_good(self):
        value = 1000
        self.assertTrue(check_size(value, size=4))

    def test_check_size_int_bad(self):
        value = 1000
        self.assertFalse(check_size(value, size=3))

    def test_check_size_none(self):
        value = None
        self.assertFalse(check_size(value, size=3))

    def test_check_size_str(self):
        value = 'test'
        self.assertFalse(check_size(value, size=3))