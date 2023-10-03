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

while option != "Q":
    print("A - Add Product\nB - Remove Product\nC - Get Total\nD - Display Cart\nQ - Quit")
    option = input("Select a option: ")

    if option == "A":
        for i in range(len(products)):
            print(f"{i} - {products[i].name} {products[i].price}")
        prod_index = input("Select prod to add: ")
        qtd = input("Select QTD: ")

        cart.add_product(products[int(prod_index)], int(qtd))
    if option == "B":
        print(cart.get_items())
        product_code = input("Select product code to remove: ")
        qtd = input("Select QTD: ")

        cart.remove_product(product_code, int(qtd))
    if option == "D":
        print(cart.get_items())
    elif option == "C":
        print("Cart Total: ", cart.calculate_total())
