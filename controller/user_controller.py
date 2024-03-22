from model.entity import *
from model.da import *


class UserController:
    @classmethod
    def add(cls, name, family, birth_date, phone, email, address, role):
        user = User(name=name, family=family, birth_date=birth_date, phone=phone, email=email, address=address,
                    role=role)
        try:
            pass
        except Exception as e:

            print(f"Error: Failed to add. {str(e)}")
