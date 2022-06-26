
from shop.order import Order
from shop.data_generator import generate_order_elements
from shop.discount_policy import loyal_consumer_policy, christmas_policy
from shop.product import BestBefore
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = generate_order_elements()
    express_order = ExpressOrder(client_first_name="Jakub", client_last_name="Mościcki", order_elements=order_elements,
                                 delivery_date="5/22/2022")
    print(express_order)




if __name__ == '__main__':
    run_homework()
