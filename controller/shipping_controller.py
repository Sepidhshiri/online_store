from model.entity import *
from model.da import *
from model.da.shipping_da import ShippingDa
from model.entity.shipping import Shipping
from tools.validators import name_validator, address_validator, city_validator, postalcode_validator


class ShippingController:
    @classmethod
    def save(cls, recipient_name, address, city, postalcode):
        try:
            shipping = Shipping(recipient_name=name_validator(recipient_name, "invalid recipient name"),
                                address=address_validator(address, "invalid address"),
                                city=city_validator(city, "invalid city"),
                                postalcode=postalcode_validator(postalcode, "invalid postal code"))

            da = ShippingDa()
            result = da.save(shipping)

            if result:
                return f"Shipping details for {shipping.recipient_name} saved"
            else:
                return "Failed to save shipping details"

        except Exception as e:
            return str(e)

    @classmethod
    def edit(cls, id, recipient_name, address, city, postalcode):
        try:
            da = ShippingDa()
            shipping = da.find_by_id(id)

            if shipping:
                shipping.recipient_name = name_validator(recipient_name, "invalid recipient name")
                shipping.address = address_validator(address, "invalid address")
                shipping.city = city_validator(city, "invalid city")
                shipping.postalcode = postalcode_validator(postalcode, "invalid postal code")

                da.edit(shipping)
                return f"Shipping details for {shipping.recipient_name} edited successfully"
            else:
                return "Shipping details not found"

        except Exception as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ShippingDa()
            result = da.remove(id)

            if result:
                return f"Shipping details with id {id} have been removed"
            else:
                return "Failed to remove shipping details"

        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ShippingDa()
            shipping = da.find_by_id(id)

            if shipping:
                return f"Shipping details found by id {id}"
            else:
                return "Shipping details not found"

        except Exception as e:
            return str(e)


