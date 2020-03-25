from django.test import TestCase
from django.utils import lorem_ipsum

from app.models import Slug


class SlugTests(TestCase):
    @classmethod
    def setUpClass(cls):
        slug_value = lorem_ipsum.words(100)
        cls.slug_value = slug_value
        Slug.objects.create(slug=slug_value)
        cls.end = ' '.join(slug_value.split()[-2:])

    def test_slug_get(self):
        slug_item = Slug.objects.get(slug=self.slug_value)
        self.assertEqual(slug_item.slug, self.slug_value)
        with self.assertRaises(Slug.DoesNotExist):
            Slug.objects.get(slug='string which is not in the slug')

    def test_slug_contains(self):
        self.assertTrue(Slug.objects.filter(slug__contains='ipsum').exists())
        self.assertTrue(Slug.objects.filter(slug__contains='lorem ipsum').exists())
        self.assertFalse(Slug.objects.filter(slug__contains='string which is not in the slug').exists())

    def test_slug_icontains(self):
        self.assertTrue(Slug.objects.filter(slug__icontains='IpSuM').exists())
        self.assertFalse(Slug.objects.filter(slug__icontains='string which is not in the slug').exists())

    def test_slug_exact(self):
        self.assertTrue(Slug.objects.filter(slug__exact=self.slug_value).exists())
        self.assertFalse(Slug.objects.filter(slug__exact='string which is not in the slug').exists())

    def test_slug_iexact(self):
        self.assertTrue(Slug.objects.filter(slug__iexact=self.slug_value.upper()).exists())
        self.assertFalse(Slug.objects.filter(slug__iexact='string which is not in the slug').exists())

    def test_slug_startswith(self):
        self.assertTrue(Slug.objects.filter(slug__startswith='lorem ipsum').exists())
        self.assertFalse(Slug.objects.filter(slug__startswith='string which is not in the slug').exists())

    def test_slug_istartswith(self):
        self.assertTrue(Slug.objects.filter(slug__istartswith='lOreM iPSUm').exists())
        self.assertFalse(Slug.objects.filter(slug__istartswith='string which is not in the slug').exists())

    def test_slug_endswith(self):
        self.assertTrue(Slug.objects.filter(slug__endswith=self.end).exists())
        self.assertFalse(Slug.objects.filter(slug__endswith='string which is not in the slug').exists())

    def test_slug_iendswith(self):
        self.assertTrue(Slug.objects.filter(slug__iendswith=self.end.upper()).exists())
        self.assertFalse(Slug.objects.filter(slug__iendswith='string which is not in the slug').exists())
