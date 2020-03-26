import datetime

from django.core.management import BaseCommand
from model_bakery import baker

from ...models import *

ITERATIONS = 10000


class Command(BaseCommand):

    def handle(self, *args, **options):
        t = datetime.datetime.now()
        # models_list = [ForeignKey, Text, Integer, Char, Float, GenericIPAddress, Uuid, Slug, DateTime, Date, Time]
        # for model in models_list:
        baker.make(AllModel, ITERATIONS)
        dt = datetime.datetime.now() - t

        print(f"Insertion took {dt}")