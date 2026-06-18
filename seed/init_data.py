# from schemas.product_schema import Product
# from database import session
# import models.databse_models as databse_models


# products = [
#     Product(name='Phone',desc="budget phone",price=99,quantity=10,category="Mobile"),
#     Product(name='Mackbook M1 air ',desc="M1 chip with 8 core gpu and cpu",price=8000,quantity=6,category="Laptop"),
#     Product(name='Phone2',desc="midrange phone",price=199,quantity=8,category="Mobile"),
#     Product(name='Mackbook M2',desc="10 core gpu and cpu",price=9990,quantity=4,category="Laptop"),
#     Product(name='Phone4',desc="budget phone",price=99,quantity=10,category="Mobile"),
# ]


# # def init_db():

# #     db = session()

# #     try:

# #         # Category Seed
# #         category_count = db.query(
# #             databse_models.Category
# #         ).count()

# #         if category_count == 0:

# #             for c in categories:

# #                 db_category = databse_models.Category(
# #                     id=c["id"],
# #                     name=c["name"]
# #                 )

# #                 db.add(db_category)

# #             db.commit()

# #         # Product Seed
# #         product_count = db.query(
# #             databse_models.Product
# #         ).count()

# #         if product_count == 0:

# #             for i in products:

# #                 db_product = databse_models.Product(
# #                     name=i.name,
# #                     desc=i.desc,
# #                     price=i.price,
# #                     quantity=i.quantity,
# #                     category_id=i.category_id
# #                 )

# #                 db.add(db_product)

# #             db.commit()

# #     finally:
# #         db.close()

# def init_db():

#     db = session()

#     try:

#         # Seed Categories
#         mobile = db.query(
#             databse_models.Category
#         ).filter(
#             databse_models.Category.name == "Mobile"
#         ).first()

#         if not mobile:

#             mobile = databse_models.Category(
#                 name="Mobile"
#             )

#             db.add(mobile)

#         laptop = db.query(
#             databse_models.Category
#         ).filter(
#             databse_models.Category.name == "Laptop"
#         ).first()

#         if not laptop:

#             laptop = databse_models.Category(
#                 name="Laptop"
#             )

#             db.add(laptop)

#         db.commit()

#         db.refresh(mobile)
#         db.refresh(laptop)

#         # Product Seed

#         product_count = db.query(
#             databse_models.Product
#         ).count()

#         if product_count == 0:

#             for p in products:

#                 category = db.query(
#                     databse_models.Category
#                 ).filter(
#                     databse_models.Category.name == p"category"
#                 ).first()

#                 db_product = databse_models.Product(
#                     name=p.name,
#                     desc=p.desc,
#                     price=p.price,
#                     quantity=p.quantity,
#                     category_id=category.id
#                 )

#                 db.add(db_product)

#             db.commit()

#     finally:
#         db.close()

from schemas.product_schema import Product
from database import session
import models.databse_models as databse_models

products = [
    Product(
        name="Phone",
        desc="budget phone",
        price=99,
        quantity=10,
        category_id=1
    ),
    Product(
        name="Mackbook M1 air",
        desc="M1 chip with 8 core gpu and cpu",
        price=8000,
        quantity=6,
        category_id=2
    ),
    Product(
        name="Phone2",
        desc="midrange phone",
        price=199,
        quantity=8,
        category_id=1
    ),
    Product(
        name="Mackbook M2",
        desc="10 core gpu and cpu",
        price=9990,
        quantity=4,
        category_id=2
    )
]

def init_db():

    db = session()

    try:

        # Create Categories

        mobile = db.query(
            databse_models.Category
        ).filter(
            databse_models.Category.name == "Mobile"
        ).first()

        if not mobile:

            mobile = databse_models.Category(
                name="Mobile"
            )

            db.add(mobile)

        laptop = db.query(
            databse_models.Category
        ).filter(
            databse_models.Category.name == "Laptop"
        ).first()

        if not laptop:

            laptop = databse_models.Category(
                name="Laptop"
            )

            db.add(laptop)

        db.commit()

        db.refresh(mobile)
        db.refresh(laptop)

        # Product Seed

        product_count = db.query(
            databse_models.Product
        ).count()

        if product_count == 0:

            for p in products:

                

                db_product = databse_models.Product(
                    name=p.name,
                    desc=p.desc,
                    price=p.price,
                    quantity=p.quantity,
                    category_id=p.category_id
                )

                db.add(db_product)

            db.commit()

    finally:
        db.close()