from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from app.models import Date


class DateTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.date_value = timezone.now().date()
        cls.date_in_the_future = cls.date_value + timedelta(days=10)
        cls.date_in_the_past = cls.date_value - timedelta(days=10)
        Date.objects.create(date=cls.date_value)
        Date.objects.create(date=cls.date_in_the_future)
        Date.objects.create(date=cls.date_in_the_past)

    def test_date(self):
        date = Date.objects.get(date=self.date_value)
        self.assertEqual(self.date_value, date.date)

    def test_date_lt(self):
        dates = Date.objects.filter(date__lt=self.date_in_the_future)
        self.assertEqual(dates.count(), 2)

    def test_date_gt(self):
        dates = Date.objects.filter(date__gt=self.date_in_the_past)
        self.assertEqual(dates.count(), 2)

    def test_date_gte(self):
        dates = Date.objects.filter(date__gte=self.date_value)
        self.assertEqual(dates.count(), 2)

    def test_date_lte(self):
        dates = Date.objects.filter(date__gte=self.date_value)
        self.assertEqual(dates.count(), 2)
