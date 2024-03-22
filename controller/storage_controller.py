from model.entity import *
from model.da import *


class StorageController:
    @classmethod
    def add(cls, session, quantity, product_status, product_id):
        storage = Storage(quantity=quantity, product_status=product_status, product_id=product_id)
        try:
            pass
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")
