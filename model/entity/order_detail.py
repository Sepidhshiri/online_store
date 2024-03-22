from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

from model.entity import *



class OrderDtail(Base):
    __tablename__ = "order_detail_tbl"
    id = Column(Integer,primary_key=True)
    quantity= Column(String(30))
    price = Column(Integer)
    comment = Column(String(30))

    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    product = relationship("Product")

    order_id = Column(Integer, ForeignKey("order_tbl.id"))
    order = relationship("Order")

    def