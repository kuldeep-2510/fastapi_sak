from fastapi import FastAPI
from database import engine
import models.databse_models as databse_models

from routes.product_routes import router
from seed import init_data
from seed.init_data import init_db

app = FastAPI()

databse_models.Base.metadata.create_all(bind=engine)

init_db()

app.include_router(router)

@app.get("/")
def greet():
    return "Welcome"
# from fastapi import FastAPI,Depends
# from schemas.product_schema import Product
# from database import session,engine
# import models.databse_models as databse_models
# from sqlalchemy.orm import Session
# from services import product_service


# app=FastAPI()

# databse_models.Base.metadata.create_all(bind=engine)


# @app.get("/")
# def greet():
#     return "Welcome"


# products=[
#     Product(id=1,name='Phone',desc="budget phone",price=99,quantity=10),

#     Product(id=2,name='Phone1',desc="expensive phone",price=909,quantity=6),
#     Product(id=3,name='Phone2',desc="midrange phone",price=199,quantity=8),
#     Product(id=4,name='Phone3',desc="flagship phone",price=999,quantity=4),
#     Product(id=5,name='Phone4',desc="budget phone",price=99,quantity=10),

# ]
# def get_db():
#     db=session()
#     try:
#         yield db
#     finally:
#         db.close()
# def init_db():

#     db=session()
#     count=db.query(databse_models.Product).count()
#     if count==0:
#         for i in products:
#             db_product=databse_models.Product(id=i.id,name=i.name,desc=i.desc,price=i.price,quantity=i.quantity)
#             db.add(db_product)
#         db.commit()
# init_db()




# @app.get('/products')
# def show_all_products(db:Session=Depends(get_db)):
#     db_products=db.query(databse_models.Product).all()
#     return db_products

# @app.get('/products/{id}')
# #db connection and query to fetch product by id

# def show_product_by_id(id:int,db:Session=Depends(get_db)):
#         db_product=db.query(databse_models.Product).filter(databse_models.Product.id==id).first()
    

#         if db_product:
#             return db_product
#         return "product not found"


# @app.post("/products")
# def add_product(product:Product,db:Session=Depends(get_db)):
#     db.add(databse_models.Product(**product.model_dump()))
#     db.commit()
#     return "product added"


# @app.delete('/products/{id}')
# def delete_product(id:int,db:Session=Depends(get_db)):
#     db_product=db.query(databse_models.Product).filter(databse_models.Product.id==id).first()
# #above line is for fetching the product with the given id from the database using SQLAlchemy's query interface. It filters the products based on the id and retrieves the first matching product.
#     if db_product:
#         db.delete(db_product)
#         db.commit()
#         return "product removed"
#     return "product not found"


# @app.put('/products/{id}' )
# def update_product(id:int,product:Product,db:Session=Depends(get_db)):
#     db_product=db.query(databse_models.Product).filter(databse_models.Product.id==id).first()
#     if db_product:
#         db_product.name=product.name
#         db_product.desc=product.desc
#         db_product.price=product.price
#         db_product.quantity=product.quantity
#         db.commit()
#         return "product updated"
#     return "product not found"
