
products = {
    "chleb": {
        "quantity": 100,
        "price": 3.5
    },
    "jabłka": {
        "quantity": 100,
        "price": 3.5
    }
}


def update_product_quantity(product_name, order_quantity):
    products[product_name]["quantity"] -= order_quantity