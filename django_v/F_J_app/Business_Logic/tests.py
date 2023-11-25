from django.test import TestCase

# Create your tests here.

"""Implement the following tests
The system shall allow the user to view the product catalogue. 

The system shall allow the user to add items to the cart. 

The system shall allow the user to view their cart. 

The system shall allow the user to remove items from their cart. 

The system shall allow the user to place an order. 

The system shall allow the user to view previously placed orders. 

The system shall allow the user to cancel an order. 

"""


class TestProductCatalogue(TestCase):
    def test_catalogue(self):
        self.assertEqual(1, 1)


class TestViewCart(TestCase):
    def test_catalogue(self):
        self.assertEqual(1, 1)


class TestRemovefromCart(TestCase):
    def test_catalogue(self):
        self.assertEqual(1, 1)


class TestPlaceOrder(TestCase):
    def test_catalogue(self):
        self.assertEqual(1, 1)


class TestViewOrder(TestCase):
    def test_catalogue(self):
        self.assertEqual(1, 1)


class TestCancelOrder(TestCase):
    def test_catalogue(self):
        self.assertEqual(1, 1)
