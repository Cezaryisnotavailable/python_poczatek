
# class TaxCalculator:
#
#     FRUIT_VEG_TAX = 0.05
#     FOOD_TAX = 0.08
#     OTHER_TAX = 0.2
#
#     @staticmethod
#     def calculate_tax_order_element(order_element):
#         if order_element.product.category_name == "Owoce i warzywa":
#             return order_element.calculate_price() * TaxCalculator.FRUIT_VEG_TAX
#         elif order_element.product.category_name == "Jedzenie":
#             return order_element.calculate_price() * TaxCalculator.FOOD_TAX
#         else:
#             return order_element.calculate_price() * TaxCalculator.OTHER_TAX


# Alternatywne rozwiązanie

class TaxCalculator:

    TAX_RATES = {
        "Owoce i warzywa:": 0.05,
        "Jedzenie": 0.08
    }
    BASE_TAX_RATE = 0.2

    @staticmethod
    def calculate_tax_order_element(order_element):
        product_category = order_element.product.category_name
        if product_category in TaxCalculator.TAX_RATES:
            tax_rate = TaxCalculator.TAX_RATES[product_category]
        else:
            tax_rate = TaxCalculator.BASE_TAX_RATE
        return tax_rate * order_element.calculate_price()


