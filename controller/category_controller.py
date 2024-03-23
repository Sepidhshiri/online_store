from model.entity import *
from model.da import *
from model.da.category_da import CategoryDa
from model.entity.category import Category
from validators.validator import name_validator, description_validator


class CategoryController:
    def save(self, name, description, sub_category=None):
        try:
            category = Category(name=name_validator(name, "invalid name"),
                                description=description_validator(description, "invalid description"),
                                sub_category=sub_category)

            da = CategoryDa()
            result = da.save(category)

            if result:
                return f"Category {category.name} saved"
            else:
                return "Failed to save category"

        except Exception as e:
            return str(e)

    def edit_by_id(self, id, name, description, sub_category=None):
        try:
            da = CategoryDa()
            category = da.find_by_id(id)

            if category:
                category.name = name_validator(name, "invalid name")
                category.description = description_validator(description, "invalid description")
                category.sub_category = sub_category

                da.edit(category)
                return f"Category {category.name} edited successfully"
            else:
                return "Category not found"

        except Exception as e:
            return str(e)

    def remove_by_id(self, id):
        try:
            da = CategoryDa()
            result = da.remove_by_id(id)

            if result:
                return f"Category with id {id} has been removed"
            else:
                return "Failed to remove category"

        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            da = CategoryDa()
            category = da.find_by_id(id)

            if category:
                return f"Category found by id {id}"
            else:
                return "Category not found"

        except Exception as e:
            return str(e)


