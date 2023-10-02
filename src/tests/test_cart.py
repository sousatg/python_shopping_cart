import unittest
from product import Product
from cart import Cart


class TestCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = Cart()
        self.gree_tea = Product("GR1", "Green Tea", 3.11)

    def test_calculate_total_empty_cart(self):
        total = self.cart.calculate_total()

        self.assertEqual(total, 0.0)

    def test_calculate_total_single_product(self):
        self.cart.add_product(self.gree_tea)

        total = self.cart.calculate_total()

        self.assertEqual(total, 3.11)

    def test_calculate_multi_items(self):
        self.cart.add_product(self.gree_tea, 3)

        self.assertEqual(self.cart.calculate_total(), self.gree_tea.price * 3)

    def test_remove_item(self):
        self.cart.add_product(self.gree_tea, 2)

        self.cart.remove_product(self.gree_tea, 1)

        self.assertEqual(self.cart.calculate_total(), 3.11)
