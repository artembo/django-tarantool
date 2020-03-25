from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models import Boolean
from django.db import DatabaseError


class BooleanTests(TestCase):

    @classmethod
    def setUpClass(cls):
        Boolean.objects.create(boolean=True)
        Boolean.objects.create(boolean=False)

    def test_boolean_create(self):
        true = Boolean.objects.get(boolean=True)
        false = Boolean.objects.get(boolean=False)
        self.assertTrue(true.boolean)
        self.assertFalse(false.boolean)

    def test_boolean_exact_lookup(self):
        self.assertTrue(Boolean.objects.filter(boolean__exact=True).exists())

    def test_boolean_in_lookup(self):
        self.assertEqual(Boolean.objects.filter(boolean__in=[True, False]).count(), 2)

    def test_boolean_isnull_lookup(self):
        self.assertEqual(Boolean.objects.filter(boolean__isnull=False).count(), 2)

    def test_boolean_incorrect_values(self):
        with self.assertRaises(ValidationError):
            Boolean.objects.create(boolean='string value')
        with self.assertRaises(DatabaseError):  # Why DatabaseError?
            Boolean.objects.create(boolean=None)
        with self.assertRaises(ValidationError):
            Boolean.objects.create(boolean=100)