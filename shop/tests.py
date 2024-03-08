from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Category

class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            price=10.99,
            stock=5,
            available=True
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 10.99)
        self.assertEqual(self.product.stock, 5)
        self.assertTrue(self.product.available)
        self.assertEqual(str(self.product), 'Test Product')

class ProductListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        dummy_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            image=dummy_image,
            price=10.99,
            stock=5,
            available=True
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_product_list_view_with_category(self):
        response = self.client.get(reverse('shop:product_list_by_category', args=['test-category']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

class ProductDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        dummy_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            image=dummy_image,
            price=10.99,
            stock=5,
            available=True
        )

    def test_product_detail_view(self):
        response = self.client.get(reverse('shop:product_detail', args=[self.product.id, self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
