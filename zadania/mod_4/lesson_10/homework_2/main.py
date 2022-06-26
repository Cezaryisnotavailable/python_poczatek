
# Zastąp implementacje klas Product, ExpiringProduct oraz OrderElement dataclass.
# Zastanów się jaka jest korzyść z takiego podejścia w każdym z tych wariantów.
# A jak by to było w przypadku klasy Order?
from shop import data_generator
from shop.order import Order


def run_homework():
    some_order_elements = data_generator.generate_order_elements()
    my_order = Order("Bob", "Kowalski", order_elements=some_order_elements)
    print(my_order)

    print(my_order.order_elements[0] == my_order.order_elements[1])
    print(my_order.order_elements[0] == my_order.order_elements[0])



if __name__ == '__main__':
    run_homework()
