class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        only_f = []
        for product in self.products:
            if product.startswith(first_letter):
                only_f.append(product)
        return only_f

    def __repr__(self):
        res = f"Items in the {self.name} catalogue:"
        for item in sorted(self.products):
            res += "\n" + item

        return res


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

