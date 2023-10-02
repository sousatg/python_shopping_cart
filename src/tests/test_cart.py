import unittest
from product import Product
from cart import Cart


class TestCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = Cart()
        self.gree_tea = Product("GR1", "Green Tea", 3.11)

    def test_calculate_total(self):
        self.cart.add_product(self.gree_tea)

        total = self.cart.calculate_total()

        self.assertEqual(total, 3.11)
