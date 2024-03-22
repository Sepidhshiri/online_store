from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base

class Order(Base):
    __tablename__ = "order_tbl"
    id = Column(Integer, primary_key=True)
    order_type = Column(String(50))
    order_status = Column(String(50))
    total_cost = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customer_tbl.id"))
    shipping_id = Column(Integer, ForeignKey("shipping_tbl.id"))

    def __init__(self, order_type, order_status, total_cost, customer_id, shipping_id):
        self.order_type = order_type
        self.order_status = order_status
        self.total_cost = total_cost
        self.customer_id = customer_id
        self.shipping_id = shipping_id

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
    def add(cls, session, order_type, order_status, total_cost, customer_id, shipping_id):
        order = cls(order_type=order_type, order_status=order_status, total_cost=total_cost, customer_id=customer_id, shipping_id=shipping_id)
        try:
            session.add(order)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")

    def __repr__(self):
        return f"Order(id={self.id}, order_type={self.order_type}, order_status={self.order_status}, total_cost={self.total_cost}, customer_id={self.customer_id}, shipping_id={self.shipping_id})"
