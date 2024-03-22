from sqlalchemy import Column, Integer, String
from model.entity.base import Base

class Category(Base):
    __tablename__ = "category_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    sub_category = Column(String(50))  # Assuming sub_category is a string attribute

    def __init__(self, name, description, sub_category):
        self.name = name
        self.description = description
        self.sub_category = sub_category

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
    def add(cls, session, name, description, sub_category):
        category = cls(name=name, description=description, sub_category=sub_category)
        try:
            session.add(category)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, description={self.description}, sub_category={self.sub_category})"
