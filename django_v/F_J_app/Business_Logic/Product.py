"""Product class and class methods"""


class Product:
    def __init__(self, name: str, description: str, cost: int):
        """Product class constructor"""
        self.name = str(name)
        self.description = str(description)
        self.cost = float(cost)

    def AddtoCart():
        """Adds an item to the shopping cart"""
        print("Item added to cart")