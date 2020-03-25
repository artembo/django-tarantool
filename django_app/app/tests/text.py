from django.test import TestCase
from django.utils import lorem_ipsum

from app.models import Text


class TextTests(TestCase):
    @classmethod
    def setUpClass(cls):
        text_value = lorem_ipsum.words(100)
        cls.text_value = text_value
        Text.objects.create(text=text_value)
        cls.end = ' '.join(text_value.split()[-2:])

    def test_text_get(self):
        text_item = Text.objects.get(text=self.text_value)
        self.assertEqual(text_item.text, self.text_value)
        with self.assertRaises(Text.DoesNotExist):
            Text.objects.get(text='string which is not in the text')

    def test_text_contains(self):
        self.assertTrue(Text.objects.filter(text__contains='ipsum').exists())
        self.assertFalse(Text.objects.filter(text__contains='string which is not in the text').exists())

    def test_text_icontains(self):
        self.assertTrue(Text.objects.filter(text__icontains='IpSuM').exists())
        self.assertFalse(Text.objects.filter(text__icontains='string which is not in the text').exists())

    def test_text_exact(self):
        self.assertTrue(Text.objects.filter(text__exact=self.text_value).exists())
        self.assertFalse(Text.objects.filter(text__exact='string which is not in the text').exists())

    def test_text_iexact(self):
        self.assertTrue(Text.objects.filter(text__iexact=self.text_value.upper()).exists())
        self.assertFalse(Text.objects.filter(text__iexact='string which is not in the text').exists())

    def test_text_startswith(self):
        self.assertTrue(Text.objects.filter(text__startswith='lorem ipsum').exists())
        self.assertFalse(Text.objects.filter(text__startswith='string which is not in the text').exists())

    def test_text_istartswith(self):
        self.assertTrue(Text.objects.filter(text__istartswith='lOreM iPSUm').exists())
        self.assertFalse(Text.objects.filter(text__istartswith='string which is not in the text').exists())

    def test_text_endswith(self):
        self.assertTrue(Text.objects.filter(text__endswith=self.end).exists())
        self.assertFalse(Text.objects.filter(text__endswith='string which is not in the text').exists())

    def test_text_iendswith(self):
        self.assertTrue(Text.objects.filter(text__iendswith=self.end.upper()).exists())
        self.assertFalse(Text.objects.filter(text__iendswith='string which is not in the text').exists())
