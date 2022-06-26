
from shop.order import Order
from shop.data_generator import generate_order_elements
from shop.discount_policy import loyal_consumer_policy, christmas_policy


def run_homework():
    first_name = "Mikołaj"
    last_name = "Lewandowski"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)

    for element in normal_order.order_elements:
        print(element)






if __name__ == '__main__':
    run_homework()
