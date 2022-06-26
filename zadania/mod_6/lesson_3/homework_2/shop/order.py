import random

from shop.errors import OverLimitError
from shop.order_element import OrderElement
from shop.product import Product
from shop.discount_policy import DiscountPolicy


class Order:

    MAX_ELEMENTS_NUMBER = 5

    def __init__(self, client_first_name, client_last_name, order_elements=None, discount_policy=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements = []
        if len(order_elements) < Order.MAX_ELEMENTS_NUMBER:
            self._order_elements = order_elements
        else:
            self._order_elements = order_elements[:Order.MAX_ELEMENTS_NUMBER]
        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) > Order.MAX_ELEMENTS_NUMBER:
            raise OverLimitError(allowed_limit=Order.MAX_ELEMENTS_NUMBER)
        self._order_elements = value


    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy.apply_discount(total_price)

    def add_product_to_order(self, product, quantity):

        if len(self._order_elements) < Order.MAX_ELEMENTS_NUMBER:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)

        else:
            raise OverLimitError(allowed_limit=Order.MAX_ELEMENTS_NUMBER)

    def __str__(self):
        mark_line = "=" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        order_value = f"O łącznej wartości: {self.total_price} PLN"
        product_details = f"Zamówione produkty:\n"
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


