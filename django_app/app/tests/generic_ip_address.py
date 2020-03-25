from django.test import TestCase

from app.models import GenericIPAddress


class ForeignKeyTests(TestCase):

    def test_create_ip_addresses(self):
        GenericIPAddress.objects.create(
            ip_address_v4='127.0.0.1',
            ip_address_v6='2001:0db8:0000:0000:0000:ff00:0042:8329',
            generic_ip_address='192.168.1.1',
        )
        self.assertEqual(
            GenericIPAddress.objects.get(ip_address_v4='127.0.0.1').ip_address_v4,
            '127.0.0.1')
        self.assertEqual(
            GenericIPAddress.objects.get(ip_address_v6='2001:0db8:0000:0000:0000:ff00:0042:8329').ip_address_v6,
            '2001:db8::ff00:42:8329')
        self.assertEqual(
            GenericIPAddress.objects.get(generic_ip_address='192.168.1.1').generic_ip_address,
            '192.168.1.1')

        GenericIPAddress.objects.create(
            ip_address_v4='0.0.0.0',
            ip_address_v6='2001:db8:0:0:0:ff00:42:8339',
            generic_ip_address='255.255.128.0',
        )
        self.assertEqual(
            GenericIPAddress.objects.get(ip_address_v4='0.0.0.0').ip_address_v4,
            '0.0.0.0')
        self.assertEqual(
            GenericIPAddress.objects.get(ip_address_v6='2001:db8:0:0:0:ff00:42:8339').ip_address_v6,
            '2001:db8::ff00:42:8339')
        self.assertEqual(
            GenericIPAddress.objects.get(generic_ip_address='255.255.128.0').generic_ip_address,
            '255.255.128.0')

        GenericIPAddress.objects.create(
            ip_address_v4='255.255.255.255',
            ip_address_v6='2001:4860:4861::8888',
            generic_ip_address='172.16.10.10',
        )
        self.assertEqual(
            GenericIPAddress.objects.get(ip_address_v4='255.255.255.255').ip_address_v4,
            '255.255.255.255')
        self.assertEqual(
            GenericIPAddress.objects.get(ip_address_v6='2001:4860:4861::8888').ip_address_v6,
            '2001:4860:4861::8888')
        self.assertEqual(
            GenericIPAddress.objects.get(generic_ip_address='172.16.10.10').generic_ip_address,
            '172.16.10.10')
