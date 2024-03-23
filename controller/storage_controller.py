from model.entity import *
from model.da import *


class StorageController:
    @classmethod
    def save(cls, quantity, product_status, product_id):
        try:
            storage = Storage(quantity=quantity,
                              product_status=product_status,
                              product_id=product_id)

            da = StorageDa()
            result = da.save(storage)

            if result:
                return f"Storage record for product ID {product_id} saved"
            else:
                return "Failed to save storage record"

        except Exception as e:
            return str(e)

    @classmethod
    def edit(cls, id, quantity, product_status, product_id):
        try:
            da = StorageDa()
            storage = da.find_by_id(id)

            if storage:
                storage.quantity = quantity
                storage.product_status = product_status
                storage.product_id = product_id

                da.edit(storage)
                return f"Storage record for product ID {product_id} edited successfully"
            else:
                return "Storage record not found"

        except Exception as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = StorageDa()
            result = da.remove(id)

            if result:
                return f"Storage record with id {id} has been removed"
            else:
                return "Failed to remove storage record"

        except Exception as e:
            return str(e)

    @classmethod
    def find_all(cls, id):
        try:
            da = StorageDa()
            storage = da.find_by_id(id)

            if storage:
                return f"Storage record found by id {id}"
            else:
                return "Storage record not found"

        except Exception as e:
            return str(e)



