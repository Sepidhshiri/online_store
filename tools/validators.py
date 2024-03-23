import re

def name_validator(name, message):
    if isinstance(name, str) and re.match("^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)

def family_validator(family, message):
    if isinstance(family, str) and re.match("^[a-zA-Z\s]{3,30}$", family):
        return family
    else:
        raise ValueError(message)

def email_validator(email, message):
    if isinstance(email, str) and re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return email
    else:
        raise ValueError(message)

def date_validator(date, message):
    if isinstance(date, str) and re.match("^([1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/((19|20)\d\d)$", date):
        return date
    else:
        raise ValueError(message)

def phone_validator(phone, message):
    if isinstance(phone, str) and re.match(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone):
        return phone
    else:
        raise ValueError(message)

def address_validator(address, message):

    if isinstance(address, str) and len(address) > 0:
        return address
    else:
        raise ValueError(message)

def recipient_name_validator(recipient_name, message):
    if isinstance(recipient_name, str) and len(recipient_name) > 0:
        return recipient_name
    else:
        raise ValueError(message)

def city_validator(city, message):
    if isinstance(city, str) and len(city) > 0:
        return city
    else:
        raise ValueError(message)

def category_name_validator(category_name, message):
    if isinstance(category_name, str) and len(category_name) > 0:
        return category_name
    else:
        raise ValueError(message)

def product_name_validator(product_name, message):
    if isinstance(product_name, str) and len(product_name) > 0:
        return product_name
    else:
        raise ValueError(message)

def brand_validator(brand, message):
    if isinstance(brand, str) and len(brand) > 0:
        return brand
    else:
        raise ValueError(message)
