from random import randint

from django.test import TestCase

from app.models import ForeignKey, Integer


class ForeignKeyTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.random_int = randint(1, 1000000)
        integer = Integer.objects.create(integer=cls.random_int)
        for _ in range(10):
            ForeignKey.objects.create(foreign_key=integer)

    def test_foreign_key(self):
        integer = Integer.objects.get(integer=self.random_int)
        fk = ForeignKey.objects.filter(foreign_key=integer)[0]
        self.assertEqual(fk.foreign_key, integer)

    def test_foreign_key_count(self):
        integer = Integer.objects.get(integer=self.random_int)
        self.assertEqual(ForeignKey.objects.count(), integer.foreignkey_set.count())
