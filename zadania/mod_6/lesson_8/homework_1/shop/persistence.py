import csv
import json

from shop.product import ProductCategory
from shop.store import AvailableProduct


def save_store(available_products, file_name="store.csv"):
    with open(file_name, mode="w", newline="") as store_file:
        headers = ["name", "category", "unit_price", "identifier", "quantity"]
        csv_writer = csv.DictWriter(store_file, fieldnames=headers)
        csv_writer.writeheader()
        for available_product in available_products:
            product = available_product.product
            csv_writer.writerow(
                {
                    "name": product.name,
                    "category": product.category.name,
                    "unit_price": product.unit_price,
                    "identifier": product.identifier,
                    "quantity": available_product.quantity,
                }
            )


def load_store(file_name="store.csv"):
    with open(file_name, newline="") as store_file:
        csv_reader = csv.DictReader(store_file)
        return [
            AvailableProduct(
                name=row["name"],
                category=ProductCategory[row["category"]],
                unit_price=float(row["unit_price"]),
                identifier=int(row["identifier"]),
                quantity=int(row["quantity"]),
            )
            for row in csv_reader
        ]


def save_order(order, file_name="orders.json"):
    new_order_data = {
        "client_first_name": order.client_first_name,
        "client_last_name": order.client_last_name,
        "order_elements": [
            {
                "product": {
                    "name": order_element.product.name,
                    "category": order_element.product.category.name,
                    "unit_price": order_element.product.unit_price,
                    "identifier": order_element.product.identifier
                },
                "quantity": order_element.quantity
            } for order_element in order.order_elements

        ]
    }

    try:
        with open(file_name, "r") as orders_file:
            orders_data = json.load(orders_file).get("orders", [])
    except FileNotFoundError:
        orders_data = []

    orders_data.append(new_order_data)
    with open(file_name, "w") as orders_file:
        json.dump({"orders": orders_data}, orders_file, indent=4)











