from model.entity import *
from model.da import *
from model.da.order_detail_da import OrderDetailDa
from model.entity.order_detail import OrderDetail
from validators.validator import quantity_validator, price_validator, comment_validator


class OrderDetailController:
    @classmethod
    def save(cls, quantity, price, comment, product_id, order_id):
        try:
            order_detail = OrderDetail(
                quantity_validator(quantity, "Invalid quantity"),
                price_validator(price, "Invalid price"),
                comment_validator(comment, "Invalid comment"),
                product_id,
                order_id
            )
            print(order_detail)
            da = OrderDetailDa()
            result = da.save(order_detail)
            if result:
                return f"{order_detail} saved successfully"
        except Exception as e:
            return str(e)

    def edit_by_id(self, id, quantity, price, comment, product_id, order_id):
        try:
            da = OrderDetailDa()
            order_detail = da.edit_by_id(id)
            if order_detail:
                order_detail.quantity = quantity_validator(quantity, "Invalid quantity")
                order_detail.price = price_validator(price, "Invalid price")
                order_detail.comment = comment_validator(comment, "Invalid comment")
                order_detail.product_id = product_id
                order_detail.order_id = order_id
                da.edit(order_detail)
                return f"Order detail with ID {id} edited successfully"
        except Exception as e:
            return str(e)

    def remove_by_id(self, id):
        try:
            da = OrderDetailDa()
            result = da.remove_by_id(id)
            if result:
                return f"Order detail with ID {id} removed successfully"
        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            da = OrderDetailDa()
            order_detail = da.find_by_id(id)
            if order_detail:
                return f"Order detail found with ID {id}: {order_detail}"
            else:
                return f"No order detail found with ID {id}"
        except Exception as e:
            return str(e)

    def find_by_order_id(self, order_id):
        try:
            da = OrderDetailDa()
            order_details = da.find_by_order_id(order_id)
            if order_details:
                return f"Order details found for order ID {order_id}: {order_details}"
            else:
                return f"No order details found for order ID {order_id}"
        except Exception as e:
            return str(e)

    def find_by_product_id(self, product_id):
        try:
            da = OrderDetailDa()
            order_details = da.find_by_product_id(product_id)
            if order_details:
                return f"Order details found for product ID {product_id}: {order_details}"
            else:
                return f"No order details found for product ID {product_id}"
        except Exception as e:
            return str(e)
