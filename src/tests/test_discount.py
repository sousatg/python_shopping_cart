import unittest
from discount import PercentageDiscount, BulkDiscount, BOGODiscount


class TestPercentageDiscount(unittest.TestCase):
    def setUp(self) -> None:
        self.discount = PercentageDiscount(1.0/3.0, 3)

    def test_apply_discount(self):
        value = self.discount.apply(11.23, 3)

        self.assertEqual(value, 22.46)


class TestBulkDiscount(unittest.TestCase):
    def setUp(self) -> None:
        self.discount = BulkDiscount(4.5, 3)

    def test_apply_discount(self):
        value = self.discount.apply(5.0, 3)

        self.assertEqual(value, 13.5)

    def test_apply_discount_missing_min_qtd(self):
        value = self.discount.apply(5.0, 2)

        self.assertEqual(value, 10.0)


class TestBOGODiscount(unittest.TestCase):
    def setUp(self) -> None:
        self.discount = BOGODiscount()

    def test_apply_discount_even_number_of_items(self):
        value = self.discount.apply(2, 2)

        self.assertEqual(value, 2)

    def test_apply_discount_odd_number_of_items(self):
        value = self.discount.apply(2, 3)

        self.assertEqual(value, 4)
