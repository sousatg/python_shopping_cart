import math


class PercentageDiscount:
    def __init__(self, value: float, min_qtd: int):
        self.value = value
        self.min_qtd = min_qtd

    def apply(self, price: float, qtd: int) -> float:
        if qtd < self.min_qtd:
            return 0

        return (price - (price * self.value)) * qtd


class BulkDiscount:
    def __init__(self, value: float, min_qtd: int) -> None:
        self.value = value
        self.min_qtd = min_qtd

    def apply(self, price: float, qtd: int) -> float:
        if qtd < self.min_qtd:
            return 0

        return (price - self.value) * qtd


class BOGODiscount:
    def apply(self, price: float, qtd: int) -> float:
        return price * math.floor(qtd / 2)
