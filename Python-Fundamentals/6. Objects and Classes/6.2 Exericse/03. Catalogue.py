class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        result_list = [x for x in self.products if str(x[0]).lower() == first_letter.lower()]
        return result_list

    def __repr__(self):
        self.products = sorted(self.products)
        res = f"Items in the {self.name} catalogue:\n"
        for x in range(len(self.products)):
            if x < len(self.products) - 1:
                res += f"{self.products[x]}\n"
            else:
                res += f"{self.products[x]}"
        return res


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
