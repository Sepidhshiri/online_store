from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base

class OrderDetail(Base):
    __tablename__ = "order_detail_tbl"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Integer)
    comment = Column(String(100))
    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    order_id = Column(Integer, ForeignKey("order_tbl.id"))

    product = relationship("Product")
    order = relationship("Order")

    def __init__(self, quantity, price, comment, product_id, order_id):
        self.quantity = quantity
        self.price = price
        self.comment = comment
        self.product_id = product_id
        self.order_id = order_id

    def save(self, session):
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to save. {str(e)}")

    def edit(self, session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to edit. {str(e)}")

    def remove(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def add(cls, session, quantity, price, comment, product_id, order_id):
        order_detail = cls(quantity=quantity, price=price, comment=comment, product_id=product_id, order_id=order_id)
        try:
            session.add(order_detail)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")

    def __repr__(self):
        return f"OrderDetail(id={self.id}, quantity={self.quantity}, price={self.price}, comment={self.comment}, product_id={self.product_id}, order_id={self.order_id})"
