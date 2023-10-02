from product import Product


class Cart:
    def __init__(self) -> None:
        self.items = {}

    def add_product(self, product: Product, qtd: int = 1) -> None:
        if self.items.get(product.code, None) is None:
            self.items[product.code] = {
                "price": product.price,
                "qtd": qtd
            }
        else:
            self.items[product.code]["qtd"] += qtd

    def remove_product(self, product: Product):
        raise

    def calculate_total(self) -> float:
        raise
