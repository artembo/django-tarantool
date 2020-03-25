from django.db import DatabaseError
from django.test import TestCase

from app.models import SmallInteger


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