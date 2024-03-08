from django.test import SimpleTestCase
from django.urls import resolve
from cart.views import cart_detail, cart_add, cart_remove

class TestCartURLs(SimpleTestCase):
    def test_cart_detail_url_resolves(self):
        url = '/cart/'
        resolver = resolve(url)
        self.assertEqual(resolver.func, cart_detail)
        self.assertEqual(resolver.namespace, 'cart')
        self.assertEqual(resolver.url_name, 'cart_detail')

    def test_cart_add_url_resolves(self):
        url = '/cart/add/123/'  # Replace '123' with a valid product ID
        resolver = resolve(url)
        self.assertEqual(resolver.func, cart_add)
        self.assertEqual(resolver.namespace, 'cart')
        self.assertEqual(resolver.url_name, 'cart_add')

    def test_cart_remove_url_resolves(self):
        url = '/cart/remove/123/'  # Replace '123' with a valid product ID
        resolver = resolve(url)
        self.assertEqual(resolver.func, cart_remove)
        self.assertEqual(resolver.namespace, 'cart')
        self.assertEqual(resolver.url_name, 'cart_remove')
