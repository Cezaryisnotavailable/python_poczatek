from zad_1.orders import create_new_order

print("Witaj w naszym sklepie!")
product_name = input("jaki towar chcesz kupic?")
quantity = int(input("Ile sztuk/kg chcesz kupic"))

result = create_new_order(product_name, quantity)
if result is not None:
    total_price = result["total_price"]
    print(f"Laczny koszt wynisei {total_price} PLN")