
products = {
    "chleb":
        {"quantity": 10,
         "price": 3},
    "jabłka":
        {"quantity": 5,
         "price": 5}

}

def update_products_quantity (product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity
