from django.test import TestCase
from django.utils import lorem_ipsum

from app.models import Char


class CharTests(TestCase):
    @classmethod
    def setUpClass(cls):
        char_value = lorem_ipsum.words(5)
        cls.char_value = char_value
        Char.objects.create(char=char_value)
        cls.end = ' '.join(char_value.split()[-2:])

    def test_char_get(self):
        char_item = Char.objects.get(char=self.char_value)
        self.assertEqual(char_item.char, self.char_value)
        with self.assertRaises(Char.DoesNotExist):
            Char.objects.get(char='string which is not in the char')

    def test_char_contains(self):
        self.assertTrue(Char.objects.filter(char__contains='lorem').exists())
        self.assertFalse(Char.objects.filter(char__contains='string which is not in the char').exists())

    def test_char_icontains(self):
        self.assertTrue(Char.objects.filter(char__icontains='lOrEm').exists())
        self.assertFalse(Char.objects.filter(char__icontains='string which is not in the char').exists())

    def test_char_exact(self):
        self.assertTrue(Char.objects.filter(char__exact=self.char_value).exists())
        self.assertFalse(Char.objects.filter(char__exact='string which is not in the char').exists())

    def test_char_iexact(self):
        self.assertTrue(Char.objects.filter(char__iexact=self.char_value.upper()).exists())
        self.assertFalse(Char.objects.filter(char__iexact='string which is not in the char').exists())

    def test_char_startswith(self):
        self.assertTrue(Char.objects.filter(char__startswith='lorem ipsum').exists())
        self.assertFalse(Char.objects.filter(char__startswith='string which is not in the char').exists())

    def test_char_istartswith(self):
        self.assertTrue(Char.objects.filter(char__istartswith='lOreM iPSUm').exists())
        self.assertFalse(Char.objects.filter(char__istartswith='string which is not in the char').exists())

    def test_char_endswith(self):
        self.assertTrue(Char.objects.filter(char__endswith=self.end).exists())
        self.assertFalse(Char.objects.filter(char__endswith='string which is not in the char').exists())

    def test_char_iendswith(self):
        self.assertTrue(Char.objects.filter(char__iendswith=self.end.upper()).exists())
        self.assertFalse(Char.objects.filter(char__iendswith='string which is not in the char').exists())
