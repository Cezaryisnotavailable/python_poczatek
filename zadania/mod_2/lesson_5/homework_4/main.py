
from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement



def run_homework():
    car = Product("seat", "suv", 5)
    other_car = Product("seat", "suv", 5)

    first_order_elements = [
        OrderElement(car, 1),
        OrderElement(other_car, 2)]
    second_order_elements = [
        OrderElement(car, 1),
        OrderElement(other_car, 2)]

    order = Order(client_first_name="Jan", client_last_name="Kowalski", order_elements=first_order_elements)
    other_order = Order(client_first_name="Jan", client_last_name="Kowalski", order_elements=second_order_elements)


    if order == other_order:
        print("Te zamówienia są równe")
    else:
        print("Te zamówienia nie są równe")


if __name__ == '__main__':
    run_homework()
