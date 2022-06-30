from unittest import TestCase

from hibouks.book import Dimension

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