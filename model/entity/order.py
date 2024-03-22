from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity import *


class Order(Base):
    __tablename__ = "order_tbl"
    id = Column(Integer, primary_key=True)
    order_type = Column(String(50))
    order_status = Column(String(50))
    total_cost = Column(Integer)

    shipping_id = Column(Integer, ForeignKey("shipping_tbl.id"))
    shipping = relationship("Shipping")

    customer_id = Column(Integer,ForeignKey( "user_tbl.id"))
    user = relationship("User")

    order_details = relationship("OrderDetail")

    def __init__(self, order_type, order_status, total_cost, customer_id, shipping_id):
        self.order_type = order_type
        self.order_status = order_status
        self.total_cost = total_cost
        self.customer_id = customer_id
        self.shipping_id = shipping_id


    # @classmethod
    # def add(cls, session, order_type, order_status, total_cost, customer_id, shipping_id):
    #     order = cls(order_type=order_type, order_status=order_status, total_cost=total_cost, customer_id=customer_id,
    #                 shipping_id=shipping_id)
    #     try:
    #         session.add(order)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print(f"Error: Failed to add. {str(e)}")
