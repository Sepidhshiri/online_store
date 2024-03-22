from sqlalchemy import Column, Integer, String, Boolean, Date
from model.entity.base import Base

class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    birth_date = Column(Date)
    phone = Column(String(12))
    email = Column(String(50))
    address = Column(String(100))
    role = Column(String(20))  # Assuming role is a string attribute

    def __init__(self, name, family, birth_date, phone, email, address, role):
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.role = role

    def save(self, session):
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to save. {str(e)}")

    def edit(self, session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to edit. {str(e)}")

    def remove(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def add(cls, session, name, family, birth_date, phone, email, address, role):
        user = cls(name=name, family=family, birth_date=birth_date, phone=phone, email=email, address=address, role=role)
        try:
            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: Failed to add. {str(e)}")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, family={self.family}, birth_date={self.birth_date}, phone={self.phone}, email={self.email}, address={self.address}, role={self.role})"
