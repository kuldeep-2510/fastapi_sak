from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
engine=create_engine  (db_url,echo=True)

session=sessionmaker(autocommit=False,autoflush=False,bind=engine)