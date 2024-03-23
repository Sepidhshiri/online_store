from model.entity import *
from model.da import *


class OrderDa(DatabaseManager):
    def find_by_id(self, order_id):
        pass

    def find_by_customer_id(self, customer_id):
        pass

    def find_by_shipping_id(self, shipping_id):
        pass

    def save(self, order):
        pass

    def update(self, order):
        pass

    def remove_by_id(self, order_id):
        pass
