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

    def __get_item(self, code: str) -> dict:
        item = self.items.get(code, None)

        return item

    def remove_product(self, product: Product, qtd: int = 1) -> None:
        item = self.__get_item(product.code)

        if item is None:
            print("Product isn't at the basket")
            return

        if item.get("qtd") <= qtd:
            del self.items[product.code]
        else:
            self.items[product.code]["qtd"] -= qtd

    def calculate_total(self) -> float:
        total = 0.0

        for item in self.items.values():
            total += item.get("price", 0.0) * item.get("qtd", 0)

        return total
