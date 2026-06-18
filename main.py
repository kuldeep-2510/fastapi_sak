from fastapi import FastAPI
from database import engine
import models.databse_models as databse_models

from routes.product_routes import router
from seed import init_data
from seed.init_data import init_db
from routes.category_routes import router as category_router

app = FastAPI()

databse_models.Base.metadata.create_all(bind=engine)

init_db()

app.include_router(router)
app.include_router(category_router)

@app.get("/")
def greet():
    return "Welcome"


