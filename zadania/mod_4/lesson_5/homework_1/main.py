
from shop.order import Order
from shop.data_generator import generate_order_elements
from shop.discount_policy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount
from shop.product import BestBefore
from shop.express_order import ExpressOrder
from shop.delivery import products_delivery


def run_homework():
    ordered_products = [
        "chleb",
        "ciastka",
        "jabłka",
        "dżem",
        "pomarańcze",
        "marchew",
        "bułki",
        "ziemniaki",
        "ser",
        "mleko"
    ]

    received_products = []

    while not set(ordered_products) == set(received_products):
        new_products = products_delivery()
        received_products += new_products
        print(f"Otrzymano {new_products}")
        missing_products = set(ordered_products).difference(received_products)
        print(f"Brakuje nam jeszcze: {missing_products}")

    print(f"Łącznie otrzymano: {received_products}")


if __name__ == '__main__':
    run_homework()
