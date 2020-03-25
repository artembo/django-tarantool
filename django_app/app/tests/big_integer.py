from django.db import DatabaseError
from django.test import TestCase

from app.models import BigInteger


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
