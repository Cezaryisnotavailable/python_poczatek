
from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
from shop.tax_calculator import TaxCalculator


def run_homework():
    orders = []

    for order in range(5):
        orders.append(Order.generate_order(1))
    for order in orders:
        print(order)

    print("\n Po sortowaniu \n")

    orders.sort(key=lambda order: order.total_price)
    for order in orders:
        print(order)

if __name__ == '__main__':
    run_homework()
