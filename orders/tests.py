from django.test import TestCase
from orders.apps import OrdersConfig

class OrdersConfigTestCase(TestCase):
    def test_app_name(self):
        self.assertEqual(OrdersConfig.name, 'orders')
