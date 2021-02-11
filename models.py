from sqlalchemy import Column,Integer,ForeignKey,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://olex:1111@localhost/mydb", echo=True, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class pharmacy(Base):
    __tablename__ = "pharmacy"
    id = Column('id', Integer, primary_key=True, unique=True)
    name = Column('name', String)
    phone = Column('phone', String)
    branch = Column('branch', String)
    mail = Column('mail', String)
    address = Column('address', String)

class users(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True, unique=True)
    name = Column('name', String)
    phone = Column('phone', String)
    mail = Column('mail', String)
    password = Column('password', String)

class medicine(Base):
    __tablename__ = "medicine"
    id = Column('id', Integer, primary_key=True, unique=True)
    name = Column('name', String)
    description = Column('description', String)
    category = Column('category', String)
    pharmacy_id = Column('pharmacy_id', Integer, ForeignKey(pharmacy.id))

