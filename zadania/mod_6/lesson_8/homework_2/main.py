import json

from shop import user_interface
from shop.persistence import load_store, save_store
from shop.store import Store


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()
    save_store(Store.AVAILABLE_PRODUCTS)




    # # moje sprawdzanko
    # file_name = "orders.json"
    # with open(file_name, "r") as orders_file:
    #     orders_by_client_data = json.load(orders_file).get("orders", {})
    #     print(orders_by_client_data)
    #     print(orders_by_client_data[1])
    #     if "cezary" in orders_by_client_data[1].values():
    #         print(orders_by_client_data[1].values())

if __name__ == '__main__':
    run_homework()
