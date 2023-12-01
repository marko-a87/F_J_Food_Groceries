from django.test import TestCase
from django.contrib.auth.models import User
from Database.models import Product, Cart, Customer, Order
from Business_Logic.Shopping_Cart import Cart_Shop 
class ShoppingCartTest(TestCase):
    def setUp(self):
        # Create a user for testing
        Product.objects.create(name="apple", description="red juicy fruit", cost = 100.00,)
        Product.objects.create(name="chicken", description="Whole Chicken", cost = 900.00,)
        Product.objects.create(name="corn", description="corn on hte cob", cost = 500.00,)

    def test_view_product_catalogue(self):
        apple = Product.objects.get(name="apple")
        chicken = Product.objects.get(name="chicken")
        corn = Product.objects.get(name="corn")
        

    def test_add_items_to_cart(self,request):
        apple = Product.objects.get(name="apple")
        chicken = Product.objects.get(name="chicken")
        corn = Product.objects.get(name="corn")
        cart = Cart.objects.create(customer=self.customer)
        cart.add_product_to_cart(request, apple)
        cart.add_product_to_cart(request, chicken)
        cart.add_product_to_cart(request, corn)
        self.assertEqual(cart.products.count(), 1)

    def test_view_cart(self):
        cart = Cart.objects.create(customerr=self.customer)
        response = self.client.get(f'shop_cart.html{cart.id}/')  # Replace with your actual URL
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your specific implementation

    def test_remove_items_from_cart(self):
        cart = Cart.objects.create(user=self.user)
        cart.products.add(self.product)
        cart.products.remove(self.product)

        self.assertEqual(cart.products.count(), 0)

    def test_place_order(self):
        cart = Cart.objects.create(user=self.user)
        cart.products.add(self.product)

        response = self.client.post('/path-to-place-order/', {'cart_id': cart.id})  # Replace with your actual URL
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your specific implementation

    def test_view_previous_orders(self):
        order = Order.objects.create(user=self.user)
        response = self.client.get(f'/path-to-view-orders/{order.id}/')  # Replace with your actual URL
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your specific implementation

    def test_cancel_order(self):
        order = Order.objects.create(user=self.user)
        response = self.client.post(f'/path-to-cancel-order/{order.id}/')  # Replace with your actual URL
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your specific implementation
