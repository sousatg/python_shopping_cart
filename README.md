# Cart Application

## Run

```
python src/app.py
```


## Add Products

Note: The application currently has 3 products already setup

Open the `src/app.py` and create a new `Product` object inside the `product` list.

## Add / Edit Discounts

The application supports 3 types of discout:

| Name | Class | Description |
|--|--|--|
| Percentage Discount | PercentageDiscount |Applied based on the product unit price |
| Bulk Discount | BulkDiscount| Changes a product base price |
| BOGO Discount | BOGODiscount | Buy One, Get One |

## Create the a Discount object using one of the Discount classes

```
discount = BulkDiscount(4.50, 3)
```

## Associate the Discount with a Product in Cart
```
cart.add_discount("SR1", discount)
```
