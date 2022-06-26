import csv

from shop.product import Product, ProductCategory
from shop.store import AvailableProduct


def load_products_from_csv(file_name="store.csv"):
    with open(file_name, newline="") as store_file:
        csv_reader = csv.reader(store_file)
        headers = next(csv_reader)
        return [
            AvailableProduct(
                name=row[0],
                category=ProductCategory[row[1]],
                unit_price=float(row[2]),
                identifier=int(row[3]),
                quantity=int(row[4])
            )
            for row in csv_reader
        ]