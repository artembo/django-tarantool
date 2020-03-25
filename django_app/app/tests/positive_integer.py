from django.db import DatabaseError
from django.test import TestCase

from app.models import PositiveInteger


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