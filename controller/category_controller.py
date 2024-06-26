from model.entity import *
from model.da import *

from tools.validators import name_validator


class CategoryController:
    @classmethod
    def save(cls, name, description, sub_category=None):
        try:
            category = Category(name=name_validator(name, "invalid name"),
                                description=description,
                                sub_category=sub_category)

            da = CategoryDa()
            result = da.save(category)

            if result:
                return f"Category {category.name} saved"
            else:
                return "Failed to save category"

        except Exception as e:
            return str(e)

    @classmethod
    def edit(cls, id, name, description, sub_category=None):
        try:
            da = CategoryDa()
            category = da.find_by_id(id)

            if category:
                category.name = name_validator(name, "invalid name")
                category.description = description
                category.sub_category = sub_category

                da.edit(category)
                return f"Category {category.name} edited successfully"
            else:
                return "Category not found"

        except Exception as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = CategoryDa()
            result = da.remove(id)

            if result:
                return f"Category with id {id} has been removed"
            else:
                return "Failed to remove category"

        except Exception as e:
            return str(e)

    @classmethod
    def find_all(cls):
        try:
            da = CategoryDa()
            category = da.find_all(Category)

            if category:
                return f"Category found by id {id}"
            else:
                return "Category not found"

        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = CategoryDa()
            category = da.find_by_id(id)

            if category:
                return f"Category found by id {id}"
            else:
                return "Category not found"

        except Exception as e:
            return str(e)