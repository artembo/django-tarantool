from django.db import DatabaseError
from django.test import TestCase

from app.models import OneToOneRelative, OneToOne


class OneToOneTests(TestCase):
    @classmethod
    def setUpClass(cls):
        for _ in range(10):
            relative = OneToOneRelative.objects.create()
            OneToOne.objects.create(one_to_one=relative)

    def test_one_to_one(self):
        relative_first = OneToOneRelative.objects.first()
        relative_last = OneToOneRelative.objects.last()
        relative_random = OneToOneRelative.objects.all().order_by('?')[0]
        self.assertEqual(relative_first.id, 1)
        self.assertEqual(relative_last.id, 10)
        self.assertEqual(relative_random.one.one_to_one_id, relative_random.pk)
        self.assertEqual(OneToOne.objects.count(), OneToOneRelative.objects.count())

    def test_values_list(self):
        self.assertListEqual(list(OneToOne.objects.values_list('one_to_one', flat=True)),
                             list(OneToOneRelative.objects.filter(one__isnull=False).values_list('one__id', flat=True)))

    def test_one_to_one_duplicate_relative(self):
        relative = OneToOneRelative.objects.first()
        with self.assertRaises(DatabaseError):
            OneToOne.objects.create(one_to_one=relative)

    def test_one_to_one_invalid(self):
        with self.assertRaises(ValueError):
            OneToOne.objects.create(one_to_one='string value')
