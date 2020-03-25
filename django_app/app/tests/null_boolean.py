from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models import NullBoolean


class NullBooleanTests(TestCase):
    @classmethod
    def setUpClass(cls):
        NullBoolean.objects.create(null_boolean=True)
        NullBoolean.objects.create(null_boolean=False)
        NullBoolean.objects.create(null_boolean=None)

    def test_create_null_boolean(self):
        true = NullBoolean.objects.get(null_boolean=True)
        false = NullBoolean.objects.get(null_boolean=False)
        none = NullBoolean.objects.get(null_boolean=None)
        self.assertTrue(true.null_boolean)
        self.assertFalse(false.null_boolean)
        self.assertIsNone(none.null_boolean)

    def test_wrong_values(self):
        with self.assertRaises(ValidationError):
            NullBoolean.objects.create(null_boolean='string value')
        with self.assertRaises(ValidationError):
            NullBoolean.objects.create(null_boolean=100)
