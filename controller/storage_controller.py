from model.entity import *
from model.da import *
from model.da.storage_da import StorageDa
from model.entity.storage import Storage
from validators.validator import id_validator, quantity_validator, product_status_validator


class StorageController:
    def save(self, quantity, product_status, product_id):
        try:
            storage = Storage(quantity=quantity_validator(quantity, "invalid quantity"),
                              product_status=product_status_validator(product_status, "invalid product status"),
                              product_id=id_validator(product_id, "invalid product ID"))

            da = StorageDa()
            result = da.save(storage)

            if result:
                return f"Storage record for product ID {product_id} saved"
            else:
                return "Failed to save storage record"

        except Exception as e:
            return str(e)

    def edit_by_id(self, id, quantity, product_status, product_id):
        try:
            da = StorageDa()
            storage = da.find_by_id(id)

            if storage:
                storage.quantity = quantity_validator(quantity, "invalid quantity")
                storage.product_status = product_status_validator(product_status, "invalid product status")
                storage.product_id = id_validator(product_id, "invalid product ID")

                da.edit(storage)
                return f"Storage record for product ID {product_id} edited successfully"
            else:
                return "Storage record not found"

        except Exception as e:
            return str(e)

    def remove_by_id(self, id):
        try:
            da = StorageDa()
            result = da.remove_by_id(id)

            if result:
                return f"Storage record with id {id} has been removed"
            else:
                return "Failed to remove storage record"

        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            da = StorageDa()
            storage = da.find_by_id(id)

            if storage:
                return f"Storage record found by id {id}"
            else:
                return "Storage record not found"

        except Exception as e:
            return str(e)



