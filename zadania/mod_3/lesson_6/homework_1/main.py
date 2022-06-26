
from shop.order import Order
from shop.data_generator import generate_order_elements
from shop.discount_policy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount
from shop.product import BestBefore
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = generate_order_elements()
    ten_percent_discount = PercentageDiscount(discount_percentage=10)
    hundred_pln_discount = AbsoluteDiscount(discount_amount=100)

    no_discount_order = Order(
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements
    )
    order_with_percentage_discount = Order(
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements,
        discount_policy=ten_percent_discount
    )
    order_with_amount_discount = Order(
        client_first_name="M",
        client_last_name="L",
        order_elements=order_elements,
        discount_policy=hundred_pln_discount
    )

    print(no_discount_order)
    print(order_with_percentage_discount)
    print(order_with_amount_discount)


if __name__ == '__main__':
    run_homework()
