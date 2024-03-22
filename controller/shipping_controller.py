from model.entity import *
from model.da import *


class ShippingController:

    @classmethod
    def add(cls, session, recipient_name, address, city, postal_code):
        shipping = Shipping(recipient_name=recipient_name, address=address, city=city, postal_code=postal_code)
        try:
            pass
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")
