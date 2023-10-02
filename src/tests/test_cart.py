import unittest
from product import Product
from cart import Cart
from discount import BOGODiscount


class TestCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = Cart()
        self.green_tea = Product("GR1", "Green Tea", 3.11)
        self.green_tea_discount = BOGODiscount()

    def test_calculate_total_empty_cart(self):
        total = self.cart.calculate_total()

        self.assertEqual(total, 0.0)

    def test_calculate_total(self):
        self.cart.add_product(self.green_tea)

        total = self.cart.calculate_total()

        self.assertEqual(total, 3.11)

    def test_calculate_total_with_discount(self):
        self.cart.add_product(self.green_tea, 2)
        self.cart.add_discount(self.green_tea.code, self.green_tea_discount)

        total = self.cart.calculate_total()

        self.assertEqual(total, 3.11)
