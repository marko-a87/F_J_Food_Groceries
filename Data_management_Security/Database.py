class Database:
    """Stores user information"""

    def __init__(self, customer_info, delivery_info, order_info):
        self.customer_info = customer_info
        self.delivery_info = delivery_info
        self.order_info = order_info
