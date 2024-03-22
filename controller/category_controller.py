from model.entity import *
from model.da import *


class CategoryController:

    @classmethod
    def add(cls, session, name, description, sub_category):
        category = Category(name=name, description=description, sub_category=sub_category)
        try:
            pass
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")
