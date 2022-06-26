
from shop.order import generate_order



def run_homework():
    first_order = generate_order()
    print(first_order)
    second_order = generate_order()
    print(second_order)

    print(f"liczba elementow pierwszego zamowienia: {len(first_order)}")
    print(f"liczba elementow drugiego zamowienia: {len(second_order)}")
if __name__ == '__main__':
    run_homework()
