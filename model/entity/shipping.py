from sqlalchemy import Column, Integer, String, ForeignKey
from model.entity.base import Base

class Shipping(Base):
    __tablename__ = "shipping_tbl"
    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(50))
    address = Column(String(100))
    city = Column(String(50))
    postal_code = Column(String(20))

    def __init__(self, recipient_name, address, city, postal_code):
        self.recipient_name = recipient_name
        self.address = address
        self.city = city
        self.postal_code = postal_code

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
    def add(cls, session, recipient_name, address, city, postal_code):
        shipping = cls(recipient_name=recipient_name, address=address, city=city, postal_code=postal_code)
        try:
            session.add(shipping)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")

    def __repr__(self):
        return f"Shipping(id={self.id}, recipient_name={self.recipient_name}, address={self.address}, city={self.city}, postal_code={self.postal_code})"
