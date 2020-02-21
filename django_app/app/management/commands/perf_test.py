import cProfile
import datetime
from random import randint

from django.core.management import BaseCommand
from django.db import transaction
# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from ...models import *
from ...utils import camel_to_snake

ITERATIONS = 1000


class Command(BaseCommand):

    def handle(self, *args, **options):

        # def rand_int():
        #     return randint(0, 10000)
        #
        # def rand_float():
        #     return randint(0, 10000000) / 1000
        #
        # cls_list = (
        #     (Integer, rand_int),
        #     (SmallInteger, rand_int),
        #     (PositiveSmallInteger, rand_int),
        #     (PositiveInteger, rand_int),
        #     (Float, rand_float),
        # )
        #
        # def perform_test(cls, func=rand_int):
        #     t = datetime.datetime.now()
        #     for _ in range(ITERATIONS):
        #         with transaction.atomic():
        #             cls.objects.create(**{camel_to_snake(cls.__name__): func()})
        #     dt = datetime.datetime.now() - t
        #     print(f"{ITERATIONS} {cls.__name__}s generated for {dt}")
        #
        # # for c in cls_list:
        # #     perform_test(*c)
        #
        t = datetime.datetime.now()
        # # with transaction.atomic():
        # with PyCallGraph(output=GraphvizOutput()):
        for _ in range(30000):
            Integer.objects.create(integer=123123)


        # count = len(SmallInteger.objects.filter(small_integer__lt=1000))
        # print(f'{count} small integers bigger than 1000')
        # count = SmallInteger.objects.filter(small_integer__gt=2000).count()
        # print(f'{count} small integers bigger than 2000')
        # count = SmallInteger.objects.filter(small_integer__gt=3000).count()
        # print(f'{count} small integers bigger than 3000')
        # count = SmallInteger.objects.filter(small_integer__gt=4000).count()
        # print(f'{count} small integers bigger than 4000')
        # count = SmallInteger.objects.filter(small_integer__gt=5000).count()
        # print(f'{count} small integers bigger than 5000')

        dt = datetime.datetime.now() - t

        print(f"Insertion took {dt}")