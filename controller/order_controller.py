from model.entity import *
from model.da import *

from model.da.order_da import OrderDa
from model.entity.order import Order
from validators.validator import id_validator, order_type_validator, order_status_validator, cost_validator


class OrderController:
    def save(self, order_type, order_status, total_cost, customer_id, shipping_id):
        try:
            order = Order(order_type=order_type_validator(order_type, "invalid order type"),
                          order_status=order_status_validator(order_status, "invalid order status"),
                          total_cost=cost_validator(total_cost, "invalid total cost"),
                          customer_id=id_validator(customer_id, "invalid customer ID"),
                          shipping_id=id_validator(shipping_id, "invalid shipping ID"))

            da = OrderDa()
            result = da.save(order)

            if result:
                return f"Order with ID {order.id} saved"
            else:
                return "Failed to save order"

        except Exception as e:
            return str(e)

    def edit_by_id(self, id, order_type, order_status, total_cost, customer_id, shipping_id):
        try:
            da = OrderDa()
            order = da.find_by_id(id)

            if order:
                order.order_type = order_type_validator(order_type, "invalid order type")
                order.order_status = order_status_validator(order_status, "invalid order status")
                order.total_cost = cost_validator(total_cost, "invalid total cost")
                order.customer_id = id_validator(customer_id, "invalid customer ID")
                order.shipping_id = id_validator(shipping_id, "invalid shipping ID")

                da.edit(order)
                return f"Order with ID {order.id} edited successfully"
            else:
                return "Order not found"

        except Exception as e:
            return str(e)

    def remove_by_id(self, id):
        try:
            da = OrderDa()
            result = da.remove_by_id(id)

            if result:
                return f"Order with ID {id} has been removed"
            else:
                return "Failed to remove order"

        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            da = OrderDa()
            order = da.find_by_id(id)

            if order:
                return f"Order found by ID {id}"
            else:
                return "Order not found"

        except Exception as e:
            return str(e)


