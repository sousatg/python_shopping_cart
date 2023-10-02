class PercentageDiscount:
    def __init__(self, value: float, min_qtd: int):
        self.value = value
        self.min_qtd = min_qtd

    def apply(self, price: float, qtd: int) -> float:
        if qtd >= self.min_qtd:
            price = price - (price * self.value)

        return round(price * qtd, 2)
