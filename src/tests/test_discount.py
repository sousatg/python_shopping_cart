import unittest
from discount import PercentageDiscount


class TestPercentageDiscount(unittest.TestCase):
    def setUp(self) -> None:
        self.discount = PercentageDiscount(0.25, 3)

    def test_apply_discount(self):
        value = self.discount.apply(11.23, 3)

        self.assertEqual(value, 7.48)
