import decimal
import time
import uuid

from django.core.exceptions import ValidationError
from django.utils import lorem_ipsum
from django.test import TestCase
from django.db import DatabaseError
from django.utils import timezone

from app.models import Boolean, NullBoolean, Integer, DateTime, Uuid, Char, Decimal, Text, Time, Float, SmallInteger, \
    BigInteger, PositiveSmallInteger, PositiveInteger, Date


class BooleanTests(TestCase):

    def setUp(self):
        Boolean.objects.create(boolean=True)
        Boolean.objects.create(boolean=False)

    def test_create_boolean(self):
        true = Boolean.objects.get(boolean=True)
        false = Boolean.objects.get(boolean=False)
        self.assertTrue(true.boolean)
        self.assertFalse(false.boolean)

    def test_wrong_values(self):
        with self.assertRaises(ValidationError):
            Boolean.objects.create(boolean='string value')
        with self.assertRaises(DatabaseError):
            Boolean.objects.create(boolean=None)
        with self.assertRaises(ValidationError):
            Boolean.objects.create(boolean=100)


class NullBooleanTests(TestCase):
    def setUp(self):
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


class DateTimeTests(TestCase):
    beginning = None

    def setUp(self):
        self.beginning = timezone.now()
        DateTime.objects.create(date_time=self.beginning)

    def test_create_date_time(self):
        date_time = DateTime.objects.get()  # TODO fix datetime conversion
        # self.assertEqual(date_time.date_time, self.beginning)

        # date_time_item = DateTime.objects.latest('date_time')
        # now = timezone.now()
        # self.assertGreater(now, date_time_item.date_time)


class TimeTests(TestCase):
    def setUp(self):
        self.time_value = timezone.now().time()
        self.time_item_id = Time.objects.create(time=self.time_value).id

    def test_create_time(self):
        time_item = Time.objects.get(id=self.time_item_id)
        # print(time_item.time, self.time_value)
        # self.assertEqual(time_item.time, self.time_value)
        # time_now = timezone.now()
        # self.assertLess(time_item.time, time_now)
        # self.assertGreater(time_now, time_item.time)


class DateTests(TestCase):
    def setUp(self):
        self.date_value = timezone.now().date()
        self.float_item_id = Date.objects.create(date=self.date_value).id


class FloatTests(TestCase):
    def setUp(self):
        self.float_value = 44.66
        self.float_item_id = Float.objects.create(float=self.float_value).id

    def test_float_create(self):
        float_item = Float.objects.get(id=self.float_item_id)
        self.assertEqual(float_item.float, self.float_value)

    def test_invalid_float(self):
        pass


class DecimalTests(TestCase):
    def setUp(self):
        self.decimal_value = 55.33
        self.decimal_item_id = Decimal.objects.create(decimal=self.decimal_value).id

    def test_char_create(self):
        decimal_item = Decimal.objects.get(id=self.decimal_item_id)
        self.assertEqual(decimal_item.decimal, self.decimal_value)

    def test_invalid_decimal(self):
        decimal_invalid_value = 55555.11111
        with self.assertRaises(decimal.InvalidOperation):
            Decimal.objects.create(decimal=decimal_invalid_value)


class IntegerTests(TestCase):
    def setUp(self):
        self.int0_id = Integer.objects.create(integer=0).id
        self.int1_id = Integer.objects.create(integer=1111).id

    def test_create_integer(self):
        int0 = Integer.objects.get(id=self.int0_id)
        int1 = Integer.objects.get(id=self.int1_id)
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
    def setUp(self):
        self.int0_id = BigInteger.objects.create(big_integer=0).id
        self.int1_id = BigInteger.objects.create(big_integer=1111).id

    def test_create_integer(self):
        int0 = BigInteger.objects.get(id=self.int0_id)
        int1 = BigInteger.objects.get(id=self.int1_id)
        self.assertEqual(int0.big_integer, 0)
        self.assertEqual(int1.big_integer, 1111)
        self.assertLess(int0.big_integer, int1.big_integer)
        self.assertGreater(int1.big_integer, int0.big_integer)

    def test_extremal_values(self):
        int_biggest = BigInteger.objects.create(big_integer=18446744073709551615)
        self.assertEqual(int_biggest.big_integer, 18446744073709551615)
        int_smallest = BigInteger.objects.create(big_integer=-9223372036854776839)
        self.assertEqual(int_smallest.big_integer, -9223372036854776839)
        self.assertLess(int_smallest.big_integer, int_biggest.big_integer)
        with self.assertRaises(DatabaseError):
            BigInteger.objects.create(big_integer=18446744073709551616)
        with self.assertRaises(DatabaseError):
            BigInteger.objects.create(big_integer=-9223372036854776840)


class PositiveIntegerTests(TestCase):
    def setUp(self):
        self.int0_id = PositiveInteger.objects.create(positive_integer=0).id
        self.int1_id = PositiveInteger.objects.create(positive_integer=1111).id

    def test_create_integer(self):
        int0 = PositiveInteger.objects.get(id=self.int0_id)
        int1 = PositiveInteger.objects.get(id=self.int1_id)
        self.assertEqual(int0.positive_integer, 0)
        self.assertEqual(int1.positive_integer, 1111)
        self.assertLess(int0.positive_integer, int1.positive_integer)
        self.assertGreater(int1.positive_integer, int0.positive_integer)

    def test_extremal_values(self):
        int_biggest = PositiveInteger.objects.create(positive_integer=18446744073709551615)
        self.assertEqual(int_biggest.positive_integer, 18446744073709551615)
        int_smallest = PositiveInteger.objects.create(positive_integer=0)
        self.assertEqual(int_smallest.positive_integer, 0)
        self.assertLess(int_smallest.positive_integer, int_biggest.positive_integer)
        with self.assertRaises(DatabaseError):
            PositiveInteger.objects.create(positive_integer=18446744073709551616)
        with self.assertRaises(DatabaseError):
            PositiveInteger.objects.create(positive_integer=-1)


class SmallIntegerTests(TestCase):
    def setUp(self):
        self.int0_id = SmallInteger.objects.create(small_integer=0).id
        self.int1_id = SmallInteger.objects.create(small_integer=1111).id

    def test_create_integer(self):
        int0 = SmallInteger.objects.get(id=self.int0_id)
        int1 = SmallInteger.objects.get(id=self.int1_id)
        self.assertEqual(int0.small_integer, 0)
        self.assertEqual(int1.small_integer, 1111)
        self.assertLess(int0.small_integer, int1.small_integer)
        self.assertGreater(int1.small_integer, int0.small_integer)

    def test_extremal_values(self):
        int_biggest = SmallInteger.objects.create(small_integer=18446744073709551615)
        self.assertEqual(int_biggest.small_integer, 18446744073709551615)
        int_smallest = SmallInteger.objects.create(small_integer=-9223372036854776839)
        self.assertEqual(int_smallest.small_integer, -9223372036854776839)
        self.assertLess(int_smallest.small_integer, int_biggest.small_integer)
        with self.assertRaises(DatabaseError):
            SmallInteger.objects.create(small_integer=18446744073709551616)
        with self.assertRaises(DatabaseError):
            SmallInteger.objects.create(small_integer=-9223372036854776840)


class PositiveSmallIntegerTests(TestCase):
    def setUp(self):
        self.int0_id = PositiveSmallInteger.objects.create(positive_small_integer=0).id
        self.int1_id = PositiveSmallInteger.objects.create(positive_small_integer=1111).id

    def test_create_integer(self):
        int0 = PositiveSmallInteger.objects.get(id=self.int0_id)
        int1 = PositiveSmallInteger.objects.get(id=self.int1_id)
        self.assertEqual(int0.positive_small_integer, 0)
        self.assertEqual(int1.positive_small_integer, 1111)
        self.assertLess(int0.positive_small_integer, int1.positive_small_integer)
        self.assertGreater(int1.positive_small_integer, int0.positive_small_integer)

    def test_extremal_values(self):
        int_biggest = PositiveSmallInteger.objects.create(positive_small_integer=18446744073709551615)
        self.assertEqual(int_biggest.positive_small_integer, 18446744073709551615)
        int_smallest = PositiveSmallInteger.objects.create(positive_small_integer=0)
        self.assertEqual(int_smallest.positive_small_integer, 0)
        self.assertLess(int_smallest.positive_small_integer, int_biggest.positive_small_integer)
        with self.assertRaises(DatabaseError):
            PositiveSmallInteger.objects.create(positive_small_integer=18446744073709551616)
        with self.assertRaises(DatabaseError):
            PositiveSmallInteger.objects.create(positive_small_integer=-1)


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
        self.assertTrue(Text.objects.filter(text__contains='lorem').exists())
        self.assertFalse(Text.objects.filter(text__contains='string which is not in the text').exists())

    def test_text_icontains(self):
        self.assertTrue(Text.objects.filter(text__icontains='lOrEm').exists())
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


class UuidTests(TestCase):
    def test_uuid_create(self):
        uuid_value = uuid.uuid4()
        uuid_id = Uuid.objects.create(uuid=uuid_value).id
        uuid_item = Uuid.objects.get(id=uuid_id)
        self.assertEqual(uuid_item.uuid, uuid_value)

    def test_invalid_uuid(self):
        with self.assertRaises(ValidationError):
            Uuid.objects.create(uuid='non-uuid text value')


