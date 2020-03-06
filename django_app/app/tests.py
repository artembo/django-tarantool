import decimal
import time
import uuid

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.db import DatabaseError
from django.utils import timezone

from app.models import Boolean, NullBoolean, Integer, DateTime, Uuid, Char, Decimal


class BooleanTests(TestCase):

    def test_create_boolean(self):
        true = Boolean.objects.create(boolean=True)
        false = Boolean.objects.create(boolean=False)
        self.assertTrue(true.boolean)
        self.assertFalse(false.boolean)

    def test_wrong_values(self):
        with self.assertRaises(ValidationError):
            Boolean.objects.create(boolean='string value')


class NullBooleanTests(TestCase):

    def test_create_null_boolean(self):
        true = NullBoolean.objects.create(null_boolean=True)
        false = NullBoolean.objects.create(null_boolean=False)
        none = NullBoolean.objects.create(null_boolean=None)
        self.assertTrue(true.null_boolean)
        self.assertFalse(false.null_boolean)
        self.assertIsNone(none.null_boolean)


class DateTimeTests(TestCase):

    def test_create_date_time(self):
        beginning = timezone.now()
        date_time = DateTime.objects.create(date_time=beginning)
        self.assertEqual(date_time.date_time, beginning)

        date_time_item = DateTime.objects.latest('date_time')
        now = timezone.now()
        self.assertGreater(now, date_time_item.date_time)


class TimeTests(TestCase):

    def tist_create_time(self):
        time_value = time.time()


class DateTests(TestCase):
    pass


class FloatTests(TestCase):
    pass


class DecimalTests(TestCase):
    def test_char_create(self):
        decimal_value = 55.33
        decimal_item = Decimal.objects.create(decimal=decimal_value)
        self.assertEqual(decimal_item.decimal, decimal_value)

    def test_invalid_decimal(self):
        decimal_invalid_value = 55555.11111
        with self.assertRaises(decimal.InvalidOperation):
            Decimal.objects.create(decimal=decimal_invalid_value)


class IntegerTests(TestCase):

    def test_create_integer(self):
        int0 = Integer.objects.create(integer=0)
        int1 = Integer.objects.create(integer=1111)

        self.assertEqual(int0.integer, 0)
        self.assertEqual(int1.integer, 1111)
        self.assertLess(int0.integer, int1.integer)
        self.assertGreater(int1.integer, int0.integer)

    def test_extremal_values(self):
        int_biggest = Integer.objects.create(integer=18446744073709551615)
        self.assertEqual(int_biggest.integer, 18446744073709551615)
        int_smallest = Integer.objects.create(integer=-9223372036854776839)
        self.assertEqual(int_smallest.integer, -9223372036854776839)
        self.assertLess(int_smallest.integer, int_biggest.integer)
        with self.assertRaises(DatabaseError):
            Integer.objects.create(integer=18446744073709551616)
        with self.assertRaises(DatabaseError):
            Integer.objects.create(integer=-9223372036854776840)


class BigIntegerTests(TestCase):
    pass


class PositiveIntegerTests(TestCase):
    pass


class PositiveSmallIntegerTests(TestCase):
    pass


class SmallIntegerTests(TestCase):
    pass


class CharTests(TestCase):
    def test_char_create(self):
        char_value = 'a'
        char_item = Char.objects.create(char=char_value)
        self.assertEqual(char_item.char, char_value)


class TextTests(TestCase):
    pass


class UuidTests(TestCase):

    def test_uuid_create(self):
        uuid_value = uuid.uuid4()
        uuid_item = Uuid.objects.create(uuid=uuid_value)
        self.assertEqual(uuid_item.uuid, uuid_value)

