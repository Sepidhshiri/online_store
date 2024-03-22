from model.entity import *
from model.da import *


class cController:
    @classmethod
    def add(cls, session, quantity, price, comment, product_id, order_id):
        order_detail = OrderDetail(quantity=quantity, price=price, comment=comment, product_id=product_id, order_id=order_id)
        try:
            session.add(order_detail)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")
