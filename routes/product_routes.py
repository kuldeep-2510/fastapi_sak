from itertools import product

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.product_schema import Product
from database import session
from services.product_services import Productservices

router = APIRouter()


def get_db():
    db = session()

    try:
        yield db

    finally:
        db.close()


@router.get("/products")
def show_all_products(search: str = None,
                      page:int=1,
                      limit:int=3,
                      db: Session = Depends(get_db)):
    return Productservices.get_all_products(db,search,page,limit)


@router.get("/products/{id}")
def show_product_by_id(id: int,db: Session = Depends(get_db)):
    product = Productservices.get_product_by_id(id,db)
    if product:
        return product
    return "product not found"


@router.post("/products")
def add_product(product: Product,db: Session = Depends(get_db)):
    return Productservices.add_product(product,db)


@router.delete("/products/{id}")
def delete_product(id: int,db: Session = Depends(get_db)):
    return Productservices.delete_product(id,db)


@router.put("/products/{id}")
def update_product(id: int,product: Product,db: Session = Depends(get_db)):
    return Productservices.update_product(id,product,db)