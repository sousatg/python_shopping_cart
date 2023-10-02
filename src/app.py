from product import Product
from discount import BulkDiscount, BOGODiscount, PercentageDiscount
from cart import Cart


pd1 = Product("GR1", "Green Tea", 3.11)
pd2 = Product("SR1", "Strawberries", 5.00)
pd3 = Product("CF1", "Coffee", 11.23)

cart = Cart()

cart.add_discount(pd1.code, BOGODiscount())
cart.add_discount(pd2.code, BulkDiscount(4.50, 3))
cart.add_discount(pd3.code, PercentageDiscount(2/3, 3))

cart.add_product(pd1, 1)
cart.add_product(pd2, 1)
cart.add_product(pd3, 3)

print(cart.calculate_total())