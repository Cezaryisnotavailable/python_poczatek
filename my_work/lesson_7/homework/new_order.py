from homework.products_data import products
order_list = []

def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]

    if available_quantity < quantity:
        print("przykro nam, nie mamy tyle towaru")
        return None
    total_price = quantity * price
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    order_list.append(new_order)
    return new_order

