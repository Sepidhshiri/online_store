from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity import *


class Storage(Base):
    __tablename__ = "storage_tbl"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    product_status = Column(String(50))

    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    product = relationship("Product")

    def __init__(self, quantity, product_status, product_id):
        self.quantity = quantity
        self.product_status = product_status
        self.product_id = product_id


    # @classmethod
    # def add(cls, session, quantity, product_status, product_id):
    #     storage = cls(quantity=quantity, product_status=product_status, product_id=product_id)
    #     try:
    #         session.add(storage)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print(f"Error: Failed to add. {str(e)}")


