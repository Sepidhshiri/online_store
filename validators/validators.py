import re

def id_validator(id, message):
    if isinstance(id, int) and id > 0:
        return id
    else:
        raise ValueError(message)

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

def birth_date_validator(birth_date, message):
    if isinstance(birth_date, str) and re.match("^([1-9][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", birth_date):
        return birth_date
    else:
        raise ValueError(message)

def phone_validator(phone, message):
    if re.match("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone):
        return phone
    else:
        raise ValueError(message)

def email_validator(email, message):
    if isinstance(email, str) and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return email
    else:
        raise ValueError(message)

def address_validator(address, message):
    if isinstance(address, str) and len(address) <= 100:
        return address
    else:
        raise ValueError(message)

def role_validator(role, message):
    if isinstance(role, str) and len(role) <= 50:
        return role
    else:
        raise ValueError(message)
