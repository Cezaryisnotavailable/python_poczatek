class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def calculate_price(self, kg):
        return self.price * kg
