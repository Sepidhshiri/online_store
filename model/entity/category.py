from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.entity import *

class Category(Base):
    __tablename__ = "category_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    sub_category = Column(String(50))  # Assuming sub_category is a string attribute

    products = relationship("Product")

    def __init__(self, name, description, sub_category):
        self.name = name
        self.description = description
        self.sub_category = sub_category

    # @classmethod
    # def add(cls, session, name, description, sub_category):
    #     category = cls(name=name, description=description, sub_category=sub_category)
    #     try:
    #         session.add(category)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print(f"Error: Failed to add. {str(e)}")

