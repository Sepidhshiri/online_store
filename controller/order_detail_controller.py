from model.entity import *
from model.da import *



class OrderDetailController:
    @classmethod
    def save(cls, quantity, price, comment, product_id, order_id):
        try:
            order_detail = OrderDetail (
                quantity = quantity ,
                price = price,
                comment = comment,
                product_id = product_id ,
                order_id = order_id)

            print(order_detail)
            da = OrderDetailDa()
            result = da.save(order_detail)
            if result:
                return f"{order_detail} saved successfully"
        except Exception as e:
            return str(e)

    @classmethod
    def edit(cls, id, quantity, price, comment, product_id, order_id):
        try:
            da = OrderDetailDa()
            order_detail = da.edit(id)
            if order_detail:
                order_detail.quantity = quantity
                order_detail.price = price
                order_detail.comment = comment
                order_detail.product_id = product_id
                order_detail.order_id = order_id
                da.edit(order_detail)
                return f"Order detail with ID {id} edited successfully"
        except Exception as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = OrderDetailDa()
            result = da.remove(id)
            if result:
                return f"Order detail with ID {id} removed successfully"
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = OrderDetailDa()
            order_detail = da.find_by_id(id)
            if order_detail:
                return f"Order detail found with ID {id}: {order_detail}"
            else:
                return f"No order detail found with ID {id}"
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_order_id(cls, order_id):
        try:
            da = OrderDetailDa()
            order_details = da.find_by_order_id(order_id)
            if order_details:
                return f"Order details found for order ID {order_id}: {order_details}"
            else:
                return f"No order details found for order ID {order_id}"
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_product_id(cls, product_id):
        try:
            da = OrderDetailDa()
            order_details = da.find_by_product_id(product_id)
            if order_details:
                return f"Order details found for product ID {product_id}: {order_details}"
            else:
                return f"No order details found for product ID {product_id}"
        except Exception as e:
            return str(e)
