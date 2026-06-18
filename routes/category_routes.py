from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from schemas.category_schema import Category
from database import session
from services.category_services import CategoryService

def get_db():

    db=session()

    try:
        yield db

    finally:
        db.close()


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/")
def create_category(
    category:Category,
    db:Session=Depends(get_db)
):

    return CategoryService.create_category(
        category,
        db
    )


#update category name
@router.put("/{id}")
def update_category(
    id: int,
    category: Category,
    db: Session = Depends(get_db)
):

    return CategoryService.update_category(
        id,
        category,
        db
    )



@router.get("/")
def get_categories(
    db:Session=Depends(get_db)
):

    return CategoryService.get_all_categories(
        db
    )


@router.delete("/{id}")
def delete_category(
    id:int,
    db:Session=Depends(get_db)
):

    return CategoryService.delete_category(
        id,
        db
    )