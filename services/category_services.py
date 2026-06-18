from sqlalchemy.orm import Session
import models.databse_models as databse_models
from utils.response import success_response,error_response

class CategoryService:

    @staticmethod
    def create_category(category,db:Session):

        existing_category = db.query(
            databse_models.Category
        ).filter(
            databse_models.Category.name.ilike(category.name.strip())
        ).first()

        if existing_category:

            return error_response(
                message="Category already exists",
                status_code=409
            )

        db_category = databse_models.Category(
            name=category.name
        )

        db.add(db_category)

        db.commit()

        db.refresh(db_category)

        return success_response(
            data=db_category,
            message="Category created successfully",
            status_code=201
        )
    
    @staticmethod
    def get_all_categories(db:Session):

        categories = db.query(
            databse_models.Category
        ).all()

        return success_response(
            data=categories,
            message="Categories fetched successfully",
            status_code=200
        )
    
    @staticmethod
    def delete_category(id:int,db:Session):

        category = db.query(
            databse_models.Category
        ).filter(
            databse_models.Category.id == id
        ).first()

        if not category:

            return error_response(
                message="Category not found",
                status_code=404
            )

        db.delete(category)

        db.commit()

        return success_response(
            data=None,
            message="Category deleted successfully",
            status_code=200
        )