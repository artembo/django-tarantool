from django.db import DatabaseError
from django.test import TestCase

from app.models import Integer


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