import random
from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 100


def generate_order_elements(products_number=None):
    if products_number is None:
        products_number = random.randint(1, Order.MAX_ELEMENTS_NUMBER)

    order_elements = []
    for product_number in range(products_number):
        product_name = f"Product-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)
        product = Product(product_name, category_name, unit_price, identifier)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))
    return order_elements



