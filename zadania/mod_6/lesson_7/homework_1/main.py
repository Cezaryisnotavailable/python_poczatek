from shop import user_interface
from shop.persistence import load_products_from_csv
from shop.store import Store



def run_homework():
    Store.AVAILABLE_PRODUCTS = load_products_from_csv()
    user_interface.handle_customer()


if __name__ == '__main__':
    run_homework()
