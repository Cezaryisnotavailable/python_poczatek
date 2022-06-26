class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price


class Order:
    def __init__(self, first_name, last_name, products_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if products_list is None:
            products_list = []
        self.products_list = products_list

        total_price = 0
        for product in products_list:
            total_price += product.price
        self.total_price = total_price


class Apple():
    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price


class Potato:
    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price




# def assign_product_to_order(order, product):
#     order.products_list.append(product)






def print_product_order(order):
    print(f"zamowinie {order.first_name} {order.last_name} to {order.products_list}")
    for _ in order.products_list:
        print(f"części składowe to: {_.name}")
    print(f"łączna suma to {order.total_price}")


def run_example():
    samochod = Product("samochod", "pojazdy", 20000)
    komputer = Product("komputer", "urządzenia", 5000)
    iphone = Product("iphone", "telefon", 3000)
    products_list = [samochod, komputer, iphone]
    order_1 = Order("Jan", "Kowalski", products_list)
    print_product_order(order_1)


if __name__ == "__main__":
    run_example()