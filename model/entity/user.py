from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from model.entity import *


class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    birth_date = Column(Date)
    phone = Column(String(12))
    email = Column(String(50))
    address = Column(String(100))
    role = Column(String(20))  # Assuming role is a string attribute

    orders = relationship("Order",back_populates="user")

    def __init__(self, name, family, birth_date, phone, email, address, role):
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.role = role

