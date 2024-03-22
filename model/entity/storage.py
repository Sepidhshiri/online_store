from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base

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
    def add(cls, session, quantity, product_status, product_id):
        storage = cls(quantity=quantity, product_status=product_status, product_id=product_id)
        try:
            session.add(storage)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")

    def __repr__(self):
        return f"Storage(id={self.id}, quantity={self.quantity}, product_status={self.product_status}, product_id={self.product_id})"
