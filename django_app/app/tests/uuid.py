import uuid

from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models import Uuid


class UuidTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.uuid_value = uuid.uuid4()
        Uuid.objects.create(uuid=cls.uuid_value)

    def test_uuid(self):
        uuid_item = Uuid.objects.get(uuid=self.uuid_value)
        self.assertEqual(uuid_item.uuid, self.uuid_value)

    def test_uuid_exact(self):
        uuid_item = Uuid.objects.get(uuid__exact=self.uuid_value)
        self.assertEqual(uuid_item.uuid, self.uuid_value)

    def test_uuid_in(self):
        uuid_item = Uuid.objects.get(uuid__in=[self.uuid_value])
        self.assertEqual(uuid_item.uuid, self.uuid_value)

    def test_invalid_uuid(self):
        with self.assertRaises(ValidationError):
            Uuid.objects.create(uuid='non-uuid text value')
