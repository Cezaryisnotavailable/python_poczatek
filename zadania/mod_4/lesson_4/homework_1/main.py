
from shop.order import Order
from shop.data_generator import generate_order_elements
from shop.discount_policy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount
from shop.product import BestBefore
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = generate_order_elements()

    identifier_to_product = {
        order_element.product.identifier: order_element.product
        for order_element in order_elements
    }

    print(identifier_to_product)


if __name__ == '__main__':
    run_homework()
