from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from model.entity import *


class Product(Base):
    __tablename__ = "product_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    brand = Column(String(30))
    buy_price = Column(Float)
    sell_price = Column(Float)

    category_id = Column(Integer, ForeignKey('category_tbl.id'))
    category = relationship("Category")

    order_details = relationship("OrderDetail")

    def __init__(self, name, brand, buy_price, sell_price, category_id):
        self.name = name
        self.brand = brand
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.category_id = category_id


