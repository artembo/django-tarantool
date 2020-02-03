import random
import string

from django.test import TestCase

# Create your tests here.
from app.models import MyModel


def test_creation():
    def generate_name():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    for _ in range(1000):
        MyModel.objects.create(name=generate_name())