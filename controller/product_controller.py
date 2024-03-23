from model.entity import *
from model.da import *
from model.da.product_da import ProductDa
from model.entity.product import Product
from tools.validators import name_validator, price_validator, id_validator


class ProductController:
    @classmethod
    def save(cls, name, brand, buy_price, sell_price, category_id):
        try:
            product = Product(name=name_validator(name, "invalid name"),
                              brand=brand,
                              buy_price=price_validator(buy_price, "invalid buy price"),
                              sell_price=price_validator(sell_price, "invalid sell price"),
                              category_id=id_validator(category_id, "invalid category ID"))

            da = ProductDa()
            result = da.save(product)

            if result:
                return f"Product {product.name} saved"
            else:
                return "Failed to save product"

        except Exception as e:
            return str(e)

    @classmethod
    def edit(cls, id, name, brand, buy_price, sell_price, category_id):
        try:
            da = ProductDa()
            product = da.find_by_id(id)

            if product:
                product.name = name_validator(name, "invalid name")
                product.brand = brand
                product.buy_price = price_validator(buy_price, "invalid buy price")
                product.sell_price = price_validator(sell_price, "invalid sell price")
                product.category_id = id_validator(category_id, "invalid category ID")

                da.edit(product)
                return f"Product {product.name} edited successfully"
            else:
                return "Product not found"

        except Exception as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ProductDa()
            result = da.remove(id)

            if result:
                return f"Product with id {id} has been removed"
            else:
                return "Failed to remove product"

        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ProductDa()
            product = da.find_by_id(id)

            if product:
                return f"Product found by id {id}"
            else:
                return "Product not found"

        except Exception as e:
            return str(e)


