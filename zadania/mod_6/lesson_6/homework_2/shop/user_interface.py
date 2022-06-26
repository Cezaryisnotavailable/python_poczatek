import os.path
from enum import Enum

from shop.errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from shop.order import Order
from shop.store import Store

class Action(Enum):
    NEW_ORDER = "1"
    HISTORY = "2"


def handle_customer():
    say_hello()
    selection = selected_action()
    if selection is Action.NEW_ORDER:
        order = init_order()
        while want_more_products():
            add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
        print_order_summary(order)
        save_order_to_txt(order)
    else:
        show_recent_orders()


def say_hello():
    print("Witaj w naszym sklepie!")


def init_order():
    # TODO: Pobierz imię i nazwisko i zwróć to czego oczekuje wołający w handle customer
    first_name = input("Podaj imię ")
    last_name = input("Podaj nazwisko ")
    order = Order(first_name, last_name)
    return order


def want_more_products():
    selection = input("Czy chcesz dodać produkty do zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie - zakładam, że chcesz coś zamówić ;)")
        return True
    return selection.upper() == "T"


def selected_action():
    selection = input("Czy chcesz zlozyc nowe zamowienie (1) \n"
                      "czy zobaczyc historię zamówien (2)?")
    try:
        return Action(selection)

    except ValueError:
        print(f"Mozliwe sa tylko dwie opcje - domyslnie wybieram nowe zamowienie")
        return Action.NEW_ORDER



def add_product_to_order(order, available_products):
    print("Oto dostępne produkty:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        # TODO: Obsłuż błędne dane podane przez użytkownika
        print(f"Wprowadzono złą wartość: {input_error}")
        return

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Niestety mamy dostępne tylko {error.available_quantity} sztuk produktu {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")


def parse_product_index(product_index_str, max_index):
    # TODO: Zamień napis na liczbę i upewnij się, że jest poprawna (czyli, że na pewno taki indeks będzie na liście)
    # TODO: W przypadku błędu rzuć odpowiedni wyjątek, który oczekiwany jest w metodzie "wyżej"
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput(f"zły format wprowadzonych danych")

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f"index musi znajdować się w przedziale od 0 do {max_index}")

    return product_index


def parse_quantity(quantity_str):
    # TODO: Zamień napis na liczbę i upewnij się, że jest większa od 0, w razie czego rzuć odpowiedni wyjątek
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput(f"zły format wprowadzonych danych")

    if quantity < 1:
        raise NotValidInput("Podana liczba powinna być większa od 0")

    return quantity


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order)
    print("Dziękujemy i zapraszamy ponownie!")


def save_order_to_txt(order):
    order_path = os.path.join("data", "orders.txt")
    order_str = str(order)
    with open(order_path, mode="a", encoding="utf-8") as order_txt:
        order_txt.write(order_str)


def show_recent_orders():
    order_path = os.path.join("data", "orders.txt")
    with open(order_path, mode="r", encoding="utf-8") as order_txt:
        print(order_txt.read())

