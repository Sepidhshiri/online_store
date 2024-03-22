from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.entity import *


class Shipping(Base):
    __tablename__ = "shipping_tbl"
    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(50))
    address = Column(String(100))
    city = Column(String(50))
    postal_code = Column(String(20))

    order = relationship("Order")

    def __init__(self, recipient_name, address, city, postal_code):
        self.recipient_name = recipient_name
        self.address = address
        self.city = city
        self.postal_code = postal_code


    # @classmethod
    # def add(cls, session, recipient_name, address, city, postal_code):
    #     shipping = cls(recipient_name=recipient_name, address=address, city=city, postal_code=postal_code)
    #     try:
    #         session.add(shipping)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print(f"Error: Failed to add. {str(e)}")

