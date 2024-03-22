from model.entity import *
from model.da import *


class CategoryController:
    @classmethod
    def add(cls, session, name, brand, buy_price, sell_price, category_id):
        product = Product(name=name, brand=brand, buy_price=buy_price, sell_price=sell_price, category_id=category_id)
        try:
            pass
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add product. {str(e)}")