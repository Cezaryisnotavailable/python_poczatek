from product import Product


def run_homework():

    parameters = [
        ("chleb", "pieczywo", 3, "chleb", "pieczywo", 3, True),
        ("chleb", "pieczywo", 3, "chleb", "pieczywo", 6, False),
        ("chleb", "pieczywo", 3, "chleb", "pieczywo", 6, True)
    ]

    for params in parameters:
        name, category_name, unit_price, other_name, other_category_name, other_unit_price, expected_result = params

        result = Product(name, category_name, unit_price) == Product(other_name, other_category_name, other_unit_price)

        if result == expected_result:
            print("OK")
        else:
            print(f"Błąd! Dla danych {params} wynik porównania jest {result} a powinien być {expected_result}")



if __name__ == '__main__':
    run_homework()
