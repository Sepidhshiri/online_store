from model.entity import *
from model.da import *
from model.da.user_da import UserDa
from model.entity.user import User
from validators.validator import name_validator, family_validator, phone_validator, username_validator, \
    password_validator


class UserController:
    def save(self, name, family, birth_date, phone, email, address, role):
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

    def edit_by_user(self, id, name, family, birth_date, phone, email, address, role):
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

    def remove_by_id(self, id):
        try:
            da = UserDa()
            result = da.remove_by_id(id)

            if result:
                return f"User with id {id} has been removed"
            else:
                return "Failed to remove user"

        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            da = UserDa()
            user = da.find_by_id(id)

            if user:
                return f"User found by id {id}"
            else:
                return "User not found"

        except Exception as e:
            return str(e)

    def find_by_username(self, username):
        try:
            if username_validator(username, "invalid username"):
                da = UserDa()
                user = da.find_by_username(username)

                if user:
                    return f"User found by username {username}"
                else:
                    return "User not found"

        except Exception as e:
            return str(e)



