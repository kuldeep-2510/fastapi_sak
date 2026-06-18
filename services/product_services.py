from sqlalchemy.orm import Session
import models.databse_models as databse_models
from schemas.product_schema import Product
from utils.response import (
    success_response,
    error_response
)
# def get_all_products(db: Session):
#     return db.query(databse_models.Product).all()

class Productservices:

    @staticmethod
    def get_all_products(
        db: Session,
        search: str = None,
        category: str = None,
        page: int = 1,
        limit: int = 3
    ):

        query = db.query(databse_models.Product)

        if search:

            query = query.filter(
                databse_models.Product.name.ilike(
                    f"%{search}%"
                )
            )

        if category:

            query = query.join(
                databse_models.Category
            ).filter(
                databse_models.Category.name.ilike(
                    category
                )
            )

        products = query.offset(
            (page - 1) * limit
        ).limit(
            limit
        ).all()
        total_records = query.count()

        return success_response(
        message="Products fetched successfully",
        status_code=200,
        pagination={
            "page": page,
            "limit": limit,
            "total_records": total_records
        },
        data=products
    )


    @staticmethod
    def add_product(product: Product, db: Session):

        existing_product = db.query(
            databse_models.Product
        ).filter(
            databse_models.Product.name.ilike(
                product.name
            )
        ).first()

        if existing_product:

            return error_response(
                message="Product already exists",
                status_code=409
            )

        # Category validation
        category = db.query(
            databse_models.Category
        ).filter(
            databse_models.Category.name.ilike(
                product.category.strip()
            )
        ).first()

        if not category:

            return error_response(
                message="Category not found",
                status_code=404
            )

        db_product = databse_models.Product(
            name=product.name,
            desc=product.desc,
            price=product.price,
            quantity=product.quantity,
            category_id=category.id
        )

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return success_response(
            data=db_product,
            message="Product added successfully",
            status_code=201
        )


    
    @staticmethod
    def delete_product(id: int, db: Session):

        db_product = db.query(databse_models.Product).filter(databse_models.Product.id == id).first()

        if not db_product:

            return error_response(message="Product not found",status_code=404)

        db.delete(db_product)
        db.commit()

        return success_response(message="Product removed successfully",status_code=200)


    
    @staticmethod
    def update_product(id: int,product: Product,db: Session):

        db_product = db.query(databse_models.Product).filter(databse_models.Product.id == id).first()

        if not db_product:

            return error_response(message="Product not found",status_code=404)

        db_product.name = product.name
        db_product.desc = product.desc
        db_product.price = product.price
        db_product.quantity = product.quantity

        db.commit()
        db.refresh(db_product)

        return success_response(data=db_product,message="Product updated successfully",status_code=200)