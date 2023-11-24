class Product:
    def __init__(self, name, description, cost):
        self.name = str(name)
        self.description = str(description)
        self.cost = float(cost)


def main():
    product_type = Product("KSAD", "works for now", 2500)
    print(product_type.cost)


if __name__ == "__main__":
    main()
