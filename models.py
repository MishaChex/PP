from sqlalchemy import Column,Integer,ForeignKey,String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True, unique=True)
    login = Column(String, unique=True)
    password = Column('password', String)
    name = Column('name', String)
    email = Column('email', String)
    phone = Column('phone', String)

    def __init__(self, login, password, name, email, phone):
        self.login = login
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone


class Pharmacy(Base):
    __tablename__ = "pharmacy"
    id = Column('id', Integer, primary_key=True, unique=True)
    name = Column('name', String)
    phone = Column('phone', String)
    branch = Column('branch', String)
    email = Column('email', String)
    address = Column('address', String)

    def __init__(self, name, phone, branch, email, address):
        self.name = name
        self.phone = phone
        self.branch = branch
        self.email = email
        self.address = address


class Medicine(Base):
    __tablename__ = "medicine"
    id = Column('id', Integer, primary_key=True, unique=True)
    name = Column('name', String)
    description = Column('description', String)
    category = Column('category', String)
    pharmacy_id = Column('pharmacy_id', Integer, ForeignKey(Pharmacy.id))

    def __init__(self, name, description, category, pharmacy_id):
        self.name = name
        self.description = description
        self.category = category
        self.pharmacy_id = pharmacy_id

