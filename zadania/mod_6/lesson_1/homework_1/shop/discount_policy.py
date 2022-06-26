
class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price


class PercentageDiscount(DiscountPolicy):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_discount(self, total_price):
        return (100 - self.discount_percentage) / 100 * total_price


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, total_price):
        if self.discount_amount <= total_price:
            return total_price - self.discount_amount
        return total_price

