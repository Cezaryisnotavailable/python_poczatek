class Product:

    def __init__(self, name, category_name, unit_price, identifier):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price
        self.identifier = int(identifier)

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price}/szt"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category_name == other.category_name and
                self.unit_price == other.unit_price)

class BestBefore(Product):

    def __init__(self, name, category_name, unit_price, identifier, production_year, best_before_years):
        super().__init__(name, category_name, unit_price, identifier)
        self.production_year = production_year
        self.best_before_years = best_before_years

    def does_expire(self, current_year):
        if (current_year - self.production_year) > self.best_before_years:
            print("Upłynął termin ważności")
        else:
            print(f"Do końca terminu ważności zostało {self.best_before_years - (current_year - self.production_year)} lat/a")

