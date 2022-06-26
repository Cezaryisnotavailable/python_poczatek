from homework import new_order, products_data

def run_shop():
    print("Witaj w naszym sklepie!")
    product_name = input("Jaki towar chcesz kupić? ")
    quantity = int(input("Ile sztuk/kg chcesz kupić? "))

    result = new_order.create_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f" łączny koszt to {total_price} ")
        products_data.update_products_quantity(product_name, quantity)
        print(products_data.products)

if __name__ == "__main__":
    run_shop()
