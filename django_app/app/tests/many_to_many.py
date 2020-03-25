# from django.db import DatabaseError
# from django.test import TestCase
#
# from app.models import ManyToMany, ForeignKey
#
#
# class ManyToManyTests(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         for _ in range(10):
#             fk = ForeignKey.objects.create()
#             m2m = ManyToMany.objects.create(name='m2m_initial')
