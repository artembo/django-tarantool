from django.db import DatabaseError
from django.test import TestCase

from app.models import PositiveSmallInteger


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