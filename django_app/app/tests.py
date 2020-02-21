
from django.test import TestCase

from app.models import Boolean


class BooleanTests(TestCase):

    def test_create_boolean(self):
        true = Boolean.objects.create(boolean=True)
        false = Boolean.objects.create(boolean=False)
        self.assertEqual(true, True)
        self.assertEqual(false, False)
