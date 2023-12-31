from product import Product


class Cart:
    def __init__(self) -> None:
        self.items = {}
        self.discounts = {}

    def get_items(self):
        return self.items

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

    def remove_product(self, product_code: str, qtd: int = 1) -> None:
        item = self.__get_item(product_code)

        if item is None:
            print("Product isn't at the basket")
            return

        if item.get("qtd") <= qtd:
            del self.items[product_code]
        else:
            self.items[product_code]["qtd"] -= qtd

    def add_discount(self, code, discount) -> None:
        self.discounts[code] = discount

    def calculate_total(self) -> float:
        total = 0.0

        for item in self.items.items():
            price = item[1].get("price", 0.0)
            qtd = item[1].get("qtd", 0)

            discount = 0.0

            productDiscount = self.discounts.get(item[0], None)
            if productDiscount is not None:
                discount = productDiscount.apply(price, qtd)

            total += (price * qtd) - discount

        return total
