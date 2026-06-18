from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name = Column(String,unique=True,nullable=False, index=True)
    desc = Column(String)
    price = Column(Float)
    quantity = Column(Integer)