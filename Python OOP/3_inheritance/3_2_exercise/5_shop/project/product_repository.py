from project.food import Food
from project.drink import Drink
from project.product import Product

class ProductRepository():

    def __init__(self):
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> [None, str]:
        try:
            pdct = next(filter(lambda p:p.name == product_name, self.products))
            return pdct

        except StopIteration:
            pass

    def remove(self, product_name):
        try:
            pdct = next(filter(lambda p:p.name == product_name, self.products))
            self.products.remove(pdct)

        except StopIteration:
            pass

    def __repr__(self):

        result = []
        [result.append(f'{p.name}: {p.quantity}') for p in self.products]
        return '\n'.join(result)

