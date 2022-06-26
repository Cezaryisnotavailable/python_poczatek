from shop.order import Order

class ExpressOrder(Order):

    EXPRESS_DELIVERY_FEE = 10

    def __init__(self, delivery_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy.apply_discount(total_price) + ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        mark_line = "=" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        order_value = f"O łącznej wartości: {self.total_price} PLN"
        product_details = f"Zamówione produkty:\n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, order_value, product_details])
        delivery_date = self.delivery_date
        result += f"zamówienie zostanie dostarczone {delivery_date}; dodatkowa opłata to " \
                  f"{ExpressOrder.EXPRESS_DELIVERY_FEE}"
        return result
