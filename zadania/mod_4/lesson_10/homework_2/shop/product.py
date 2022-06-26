from dataclasses import dataclass

@dataclass
class Product:
    name: str
    category_name: str
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price}/szt"


@dataclass
class BestBefore(Product):
    production_year: int
    best_before_years: int

    def does_expire(self, current_year):
        if (current_year - self.production_year) > self.best_before_years:
            print("Upłynął termin ważności")
        else:
            print(f"Do końca terminu ważności zostało {self.best_before_years - (current_year - self.production_year)} "
                  f"lat/a")

