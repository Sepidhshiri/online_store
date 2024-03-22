from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.entity.stuff import Stuff

class Storage(Base):
    __tablename__ = "storage_tbl"
    id = Column(Integer, primary_key=True)
    stuff_id = Column(Integer, ForeignKey("stuff_tbl.id"))
    stuff = relationship("Stuff")
    quantity_available = Column(Integer)
    product_status_product_id = Column(Integer, ForeignKey("product_status_product_tbl.id"))

    def __init__(self, stuff_id, quantity_available, product_status_product_id):
        self.stuff_id = stuff_id
        self.quantity_available = quantity_available
        self.product_status_product_id = product_status_product_id

    def __repr__(self):
        return f"<Storage(id={self.id}, stuff_id={self.stuff_id}, quantity_available={self.quantity_available}, product_status_product_id={self.product_status_product_id})>"
