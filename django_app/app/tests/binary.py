# from io import BytesIO
#
# from django.core.exceptions import ValidationError
# from django.test import TestCase
#
# from app.models import Binary
# from django.db import DatabaseError
#
#
# class BinaryTests(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         # cls.bytes = BytesIO(b'Binary content')
#         test_string = "Binary content"
#         res = bytes(test_string, 'utf-8')
#         Binary.objects.create(binary=res)
#
#     def test_binary_content(self):
#         binary = Binary.objects.get()
#         print(binary)
