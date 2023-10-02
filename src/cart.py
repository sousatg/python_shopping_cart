from product import Product


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product: Product):
        raise

    def remove_product(self, product: Product):
        raise

    def calculate_total(self) -> float:
        raise
