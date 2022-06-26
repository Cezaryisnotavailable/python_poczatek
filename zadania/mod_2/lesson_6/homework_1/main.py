
from shop.order import Order
from shop.order import generate_order
from shop.product import Product
from shop.order_element import OrderElement



def run_homework():
    first_order = generate_order()
    print(first_order)

    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    first_order.add_product_to_order(cookie, quantity=10)
    print(first_order)


if __name__ == '__main__':
    run_homework()
