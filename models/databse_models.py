from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name = Column(String,unique=True,nullable=False, index=True)
    desc = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category_id=Column(Integer,ForeignKey('category.id',ondelete='CASCADE'),nullable=False)
    category=relationship('Category',back_populates="products")


class Category(Base):
    __tablename__ = "category"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True,nullable=False)
    
    products=relationship('Product',back_populates='category',cascade='all,delete')