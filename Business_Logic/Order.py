class Order:
    def __init__(self, order_number, date_ordered, date_shipped, status, customer_name):
        self.order_number = order_number
        self.date_ordered = date_ordered
        self.date_shipped = date_shipped
        self.status = status
        self.customer_name = customer_name


def main():
    order_type = Order(25, "Thursday", "Saturday", "Shipped", "Shamar")


if __name__ == "__main__":
    main()
