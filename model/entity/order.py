from sqlalchemy import Column, Integer, String
from model.entity.base import Base

class Shipping(Base):
    __tablename__ = "shipping_tbl"
    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(50))
    address = Column(String(100))
    city = Column(String(50))
    postalcode = Column(String(20))

    def __init__(self, recipient_name, address, city, postalcode):
        self.recipient_name = recipient_name
        self.address = address
        self.city = city
        self.postalcode = postalcode

    def __repr__(self):
        return f"<Shipping(id={self.id}, recipient_name='{self.recipient_name}', address='{self.address}', city='{self.city}', postalcode='{self.postalcode}')>"
