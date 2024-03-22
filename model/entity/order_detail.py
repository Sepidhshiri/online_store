from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity import *


class OrderDetail(Base):
    __tablename__ = "order_detail_tbl"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Integer)
    comment = Column(String(100))

    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    product = relationship("Product")

    order_id = Column(Integer, ForeignKey("order_tbl.id"))
    order = relationship("Order")

    def __init__(self, quantity, price, comment, product_id, order_id):
        self.quantity = quantity
        self.price = price
        self.comment = comment
        self.product_id = product_id
        self.order_id = order_id

    #
    # @classmethod
    # def add(cls, session, quantity, price, comment, product_id, order_id):
    #     order_detail = cls(quantity=quantity, price=price, comment=comment, product_id=product_id, order_id=order_id)
    #     try:
    #         session.add(order_detail)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print(f"Error: Failed to add. {str(e)}")
    #

