from model.entity import *
from model.da import *

from model.da.order_detail_da import OrderDetailDa
from model.entity.order_detail import OrderDetail
from validators.validator import id_validator, quantity_validator, price_validator

class OrderDetailController:
    def save(self, quantity, price, comment, product_id, order_id):
        try:
            order_detail = OrderDetail(quantity=quantity_validator(quantity, "invalid quantity"),
                                       price=price_validator(price, "invalid price"),
                                       comment=comment,
                                       product_id=id_validator(product_id, "invalid product ID"),
                                       order_id=id_validator(order_id, "invalid order ID"))

            da = OrderDetailDa()
            result = da.save(order_detail)

            if result:
                return f"Order detail for product ID {product_id} saved"
            else:
                return "Failed to save order detail"

        except Exception as e:
            return str(e)

    def edit_by_id(self, id, quantity, price, comment, product_id, order_id):
        try:
            da = OrderDetailDa()
            order_detail = da.find_by_id(id)

            if order_detail:
                order_detail.quantity = quantity_validator(quantity, "invalid quantity")
                order_detail.price = price_validator(price, "invalid price")
                order_detail.comment = comment
                order_detail.product_id = id_validator(product_id, "invalid product ID")
                order_detail.order_id = id_validator(order_id, "invalid order ID")

                da.edit(order_detail)
                return f"Order detail for product ID {product_id} edited successfully"
            else:
                return "Order detail not found"

        except Exception as e:
            return str(e)

    def remove_by_id(self, id):
        try:
            da = OrderDetailDa()
            result = da.remove_by_id(id)

            if result:
                return f"Order detail with id {id} has been removed"
            else:
                return "Failed to remove order detail"

        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            da = OrderDetailDa()
            order_detail = da.find_by_id(id)

            if order_detail:
                return f"Order detail found by id {id}"
            else:
                return "Order detail not found"

        except Exception as e:
            return str(e)

    # Implement other find methods similarly

