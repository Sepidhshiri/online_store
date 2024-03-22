from model.entity import *
from model.da import *


class OrderController:
    @classmethod
    def add(cls, session, order_type, order_status, total_cost, customer_id, shipping_id):
        order = Order(order_type=order_type, order_status=order_status, total_cost=total_cost, customer_id=customer_id,
                      shipping_id=shipping_id)
        try:
            pass
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")
