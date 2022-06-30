from unittest import TestCase

from hibouks.tools import to_int, to_languagecode

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