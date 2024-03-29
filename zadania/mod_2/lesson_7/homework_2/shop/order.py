import random

from shop.order_element import OrderElement
from shop.product import Product


class Order:

    MAX_ELEMENTS_NUMBER = 5

    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements = []
        if len(order_elements) < Order.MAX_ELEMENTS_NUMBER:
            self._order_elements = order_elements
        else:
            self._order_elements = order_elements[:Order.MAX_ELEMENTS_NUMBER]
        self.total_price = self._calculate_total_price()

    def _calculate_total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return total_price

    def add_product_to_order(self, product, quantity):
        new_element = OrderElement(product, quantity)
        if len(self._order_elements) < Order.MAX_ELEMENTS_NUMBER:
            self._order_elements.append(new_element)
        else:
            print(f"Przekroczono limit {Order.MAX_ELEMENTS_NUMBER} elementów")
        self.total_price = self._calculate_total_price()


    def __str__(self):
        mark_line = "=" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        order_value = f"O łącznej wartości: {self.total_price} PLN"
        product_details = f"Zamówione produkty:"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, order_value, product_details])
        return result

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if (self.client_first_name and self.client_last_name) != (other.client_first_name and other.client_last_name):
            return False

        if len(self._order_elements) != len(other.order_elements):
            return False

        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False
        return True

    @classmethod
    def generate_order(cls, number_of_product):
        order_elements = []
        for product_number in range(number_of_product):
            product_name = f"Produkt-{product_number}"
            category_name = "Inne"
            unit_price = random.randint(1, 30)
            product = Product(product_name, category_name, unit_price)
            quantity = random.randint(1, 10)
            order_elements.append(OrderElement(product, quantity))

        order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski", order_elements=order_elements)
        return order
