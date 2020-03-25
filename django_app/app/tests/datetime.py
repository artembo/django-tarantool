from django.test import TestCase, override_settings
from django.utils import timezone

from app.models import DateTime


class DateTimeTests(TestCase):
    pass
    # @classmethod
    # def setUpClass(cls):
    #     cls.beginning = timezone.now()
    #     DateTime.objects.create(date_time=cls.beginning)

    # def test_date_time_create(self):
    #     date_time = DateTime.objects.get()  # TODO fix datetime conversion
    #     self.assertEqual(date_time.date_time, self.beginning)
        #
        # date_time_item = DateTime.objects.latest('date_time')
        # now = timezone.now()
        # self.assertGreater(now, date_time_item.date_time)

    # @override_settings(USE_TZ=True)
    # def test_21432(self):
    #     now = timezone.localtime(timezone.now().replace(microsecond=0))
    #     DateTime.objects.create(date_time=now)
    #     qs = DateTime.objects.datetimes('date_time', 'second')
    #     self.assertEqual(qs[0], now)
