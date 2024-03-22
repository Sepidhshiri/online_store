from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base

class Order(Base):
    __tablename__ = "order_tbl"
    id = Column(Integer, primary_key=True)
    order_type = Column(String(30))
    order_status = Column(String(30))
    total_cost = Column(Float)
    customer_id = Column(Integer, ForeignKey('customer_tbl.id'))
    customer = relationship("Customer", back_populates="orders")
    shipping_id = Column(Integer, ForeignKey('shipping_tbl.id'))
    shipping = relationship("Shipping", back_populates="orders")

    def __init__(self, order_type, order_status, total_cost, customer_id, shipping_id):
        self.order_type = order_type
        self.order_status = order_status
        self.total_cost = total_cost
        self.customer_id = customer_id
        self.shipping_id = shipping_id

    def __repr__(self):
        return f"<Order(id={self.id}, order_type='{self.order_type}', order_status='{self.order_status}', total_cost={self.total_cost}, customer_id={self.customer_id}, shipping_id={self.shipping_id})>"
