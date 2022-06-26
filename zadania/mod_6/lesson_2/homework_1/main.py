
# Zastąp implementacje klas Product, ExpiringProduct oraz OrderElement dataclass.
# Zastanów się jaka jest korzyść z takiego podejścia w każdym z tych wariantów.
# A jak by to było w przypadku klasy Order?
from shop import data_generator
from shop.order import Order
from shop.product import Product, ProductCategory


def run_homework():
    order_elements_on_limit= data_generator.generate_order_elements(products_number=Order.MAX_ELEMENTS_NUMBER)
    order_on_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limit)
    print(order_on_limit)

    product = data_generator.generate_product()
    quantity = data_generator.generate_quantity()
    order_on_limit.add_product_to_order(product, quantity)

    order_elements_over_limit = data_generator.generate_order_elements(products_number=Order.MAX_ELEMENTS_NUMBER +1)
    order_over_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limit)






if __name__ == '__main__':
    run_homework()
