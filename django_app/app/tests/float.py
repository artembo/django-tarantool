from django.db import DatabaseError
from django.test import TestCase

from app.models import Float


class FloatTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.float_value = 44.66
        cls.float_item_id = Float.objects.create(float=cls.float_value).id

    def test_float_create(self):
        float_item = Float.objects.get(id=self.float_item_id)
        self.assertEqual(float_item.float, self.float_value)

    def test_invalid_float(self):
        with self.assertRaises(ValueError):
            Float.objects.create(float='string value')
        with self.assertRaises(DatabaseError):  # Why DatabaseError?
            Float.objects.create(float=None)
