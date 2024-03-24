from model.entity import *
from model.da import *



class OrderController:
    @classmethod
    def save(cls, order_type, order_status, total_cost, customer_id, shipping_id):
        try:
            order = Order(order_type=order_type,
                          order_status=order_status,
                          total_cost=total_cost,
                          customer_id=customer_id,
                          shipping_id=shipping_id )


            da = OrderDa()
            result = da.save(order)

            if result:
                return f"Order with ID {order.id} saved"
            else:
                return "Failed to save order"

        except Exception as e:
            return str(e)

    @classmethod
    def edit(cls, id, order_type, order_status, total_cost, customer_id, shipping_id):
        try:
            da = OrderDa()
            order = da.find_by_id(id)

            if order:
                order.order_type = order_type
                order.order_status = order_status
                order.total_cost = total_cost
                order.customer_id = customer_id
                order.shipping_id = shipping_id

                da.edit(order)
                return f"Order with ID {order.id} edited successfully"
            else:
                return "Order not found"

        except Exception as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = OrderDa()
            result = da.remove(id)

            if result:
                return f"Order with ID {id} has been removed"
            else:
                return "Failed to remove order"

        except Exception as e:
            return str(e)

    @classmethod
    def find_all(cls, id):
        try:
            da = OrderDa()
            order = da.find_all(Order)

            if order:
                return f"Order found by ID {id}"
            else:
                return "Order not found"

        except Exception as e:
            return str(e)


    @classmethod
    def find_by_id(cls, id):
        try:
            da = OrderDa()
            order = da.find_by_id(Order, id)

            if order:
                return f"Order found by ID {id}"
            else:
                return "Order not found"

        except Exception as e:
            return str(e)

