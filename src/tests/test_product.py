import unittest
from product import Product


class CreateProducTest(unittest.TestCase):
    def test_creating_product(self):
        product = Product("GR1", "Green Tea", 3.11)

        self.assertIsInstance(product, Product)
