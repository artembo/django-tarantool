from django.test import TestCase
from django.utils import timezone

from app.models import DateTime


class DateTimeTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.beginning = timezone.now()
        DateTime.objects.create(date_time=cls.beginning)

    def test_date_time(self):
        date_time = DateTime.objects.get()
        self.assertEqual(date_time.date_time, self.beginning)

        now = timezone.now()
        DateTime.objects.create(date_time=now)
        latest = DateTime.objects.latest('date_time')
        self.assertEqual(now, latest.date_time)
        self.assertGreater(now, date_time.date_time)
