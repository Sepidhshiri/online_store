from model.entity import *
from model.da import *
from model.da.user_da import UserDa
from model.entity.user import User
from tools.validators import name_validator, family_validator, phone_validator


class UserController:
    @classmethod
    def save(cls, name, family, birth_date, phone, email, address, role):
        try:
            user = User(name=name_validator(name, "invalid name"),
                        family=family_validator(family, "invalid family"),
                        birth_date=birth_date,  # Assuming birth_date is validated elsewhere
                        phone=phone_validator(phone, "invalid phone"),
                        email=email,  # Assuming email is validated elsewhere
                        address=address,  # Assuming address is validated elsewhere
                        role=role)

            da = UserDa()
            result = da.save(user)

            if result:
                return f"{user.name} {user.family} saved"
            else:
                return "Failed to save user"

        except Exception as e:
            return str(e)

    @classmethod
    def edit_by_user(cls, id, name, family, birth_date, phone, email, address, role):
        try:
            da = UserDa()
            user = da.find_by_id(id)  # Fetch user by id before editing

            if user:
                user.name = name_validator(name, "invalid name")
                user.family = family_validator(family, "invalid family")
                user.birth_date = birth_date  # Assuming birth_date is validated elsewhere
                user.phone = phone_validator(phone, "invalid phone")
                user.email = email  # Assuming email is validated elsewhere
                user.address = address  # Assuming address is validated elsewhere
                user.role = role

                da.edit(user)
                return f"{user.name} {user.family} edited successfully"
            else:
                return "User not found"

        except Exception as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = UserDa()
            result = da.remove(id)

            if result:
                return f"User with id {id} has been removed"
            else:
                return "Failed to remove user"

        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = UserDa()
            user = da.find_by_id(id)

            if user:
                return f"User found by id {id}"
            else:
                return "User not found"

        except Exception as e:
            return str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = UserDa()
            user = da.find_by_username(username)

            if user:
                return f"User found by username {username}"
            else:
                return "User not found"

        except Exception as e:
            return str(e)



