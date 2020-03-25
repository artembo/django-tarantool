import decimal

from django.test import TestCase

from app.models import Decimal


class DecimalTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decimal_value = 55.33
        cls.decimal_item_id = Decimal.objects.create(decimal=cls.decimal_value).id

    def test_char_create(self):
        decimal_item = Decimal.objects.get(id=self.decimal_item_id)
        self.assertEqual(decimal_item.decimal, self.decimal_value)

    def test_invalid_decimal(self):
        decimal_invalid_value = 55555.11111
        with self.assertRaises(decimal.InvalidOperation):
            Decimal.objects.create(decimal=decimal_invalid_value)