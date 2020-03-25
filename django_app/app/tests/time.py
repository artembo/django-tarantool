import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from app.models import Time


class TimeTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.morning_time_value = datetime.time(hour=9, minute=20, second=10)
        cls.evening_time_value = datetime.time(hour=19, minute=2, second=55)
        cls.time_value = timezone.now().time().replace(microsecond=0)
        Time.objects.create(time=cls.time_value)
        Time.objects.create(time=cls.morning_time_value)
        Time.objects.create(time=cls.evening_time_value)

    def test_time_values(self):
        time_item = Time.objects.get(time=self.time_value)
        self.assertEqual(time_item.time, self.time_value)
        time_now = timezone.now().time()
        self.assertLess(time_item.time, time_now)
        self.assertGreater(time_now, time_item.time)

    def test_lookups(self):
        time_now = timezone.now().time()
        Time.objects.filter(time__lte=time_now)
        self.assertTrue(Time.objects.filter(time__lt=self.evening_time_value).exists())
        self.assertTrue(Time.objects.filter(time__lte=self.evening_time_value).exists())
        self.assertTrue(Time.objects.filter(time__gt=self.morning_time_value).exists())
        self.assertTrue(Time.objects.filter(time__gte=self.morning_time_value).exists())

    def test_time_invalid_value(self):
        with self.assertRaises(ValidationError):
            Time.objects.create(time='string value')
