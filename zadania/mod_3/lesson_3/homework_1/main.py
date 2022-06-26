
from shop.order import Order
from shop.data_generator import generate_order_elements
from shop.discount_policy import loyal_consumer_policy, christmas_policy
from shop.product import BestBefore


def run_homework():
    chleb = BestBefore(name="chleb", category_name="pieczywo", unit_price=4, production_year=2010, best_before_years=5)

    chleb.does_expire(2023)





if __name__ == '__main__':
    run_homework()
