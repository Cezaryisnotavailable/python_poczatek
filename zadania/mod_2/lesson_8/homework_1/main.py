
from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
from shop.tax_calculator import TaxCalculator

def orders_total_price_sort(order):
    return order.total_price

def run_homework():
    orders = []

    for order in range(5):
        orders.append(Order.generate_order(1))
    for order in orders:
        print(order)

    print("\n Po sortowaniu \n")

    orders.sort(key=orders_total_price_sort)
    for order in orders:
        print(order)

if __name__ == '__main__':
    run_homework()
