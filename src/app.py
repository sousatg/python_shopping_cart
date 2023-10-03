from product import Product
from discount import BulkDiscount, BOGODiscount, PercentageDiscount
from cart import Cart


products = [
    Product("GR1", "Green Tea", 3.11),
    Product("SR1", "Strawberries", 5.00),
    Product("CF1", "Coffee", 11.23)
]


cart = Cart()

cart.add_discount("GR1", BOGODiscount())
cart.add_discount("SR1", BulkDiscount(4.50, 3))
cart.add_discount("CF1", PercentageDiscount(2/3, 3))

option = ""

while option != "q":
    print("A - Add Product\nB - Get Total")
    option = input("Select a option: ")

    if option == "A":
        for i in range(len(products)):
            print(f"i - {products[i].name} {products[i].price}")
        prod_index = input("Select prod to add: ")
        qtd = input("Select QTD: ")

        print(qtd)

        cart.add_product(products[int(prod_index)], int(qtd))
    elif option == "B":
        print("Cart Total: ", cart.calculate_total())
