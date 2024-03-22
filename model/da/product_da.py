from model.da.database_manager import DatabaseManager
from model.entity.product import Product


class ProductDa (DatabaseManager):
    pass

    def find_by_product_name(self, name):
        pass

    def find_by_product_brand(self, brand):
        pass

    def find_by_product_type(self, model):
        pass

    def find_by_product_id(self, id):
        pass

    def find_all(self, **kwargs):
        pass
