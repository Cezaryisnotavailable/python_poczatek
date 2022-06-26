
from shop.order import Order
from shop.data_generator import generate_order_elements
from shop.discount_policy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount
from shop.product import BestBefore
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = generate_order_elements()
    express_order = ExpressOrder(
        delivery_date="10-05-2020",
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements
    )
    print(express_order)


if __name__ == '__main__':
    run_homework()
