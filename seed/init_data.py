from schemas.product_schema import Product
from database import session
import models.databse_models as databse_models


products = [
    Product(id=1,name='Phone',desc="budget phone",price=99,quantity=10),
    Product(id=2,name='Phone1',desc="expensive phone",price=909,quantity=6),
    Product(id=3,name='Phone2',desc="midrange phone",price=199,quantity=8),
    Product(id=4,name='Phone3',desc="flagship phone",price=999,quantity=4),
    Product(id=5,name='Phone4',desc="budget phone",price=99,quantity=10),
]


def init_db():

    db = session()

    try:

        count = db.query(
            databse_models.Product
        ).count()

        if count == 0:

            for i in products:

                db_product = databse_models.Product(
                    name=i.name,
                    desc=i.desc,
                    price=i.price,
                    quantity=i.quantity
                )

                db.add(db_product)

            db.commit()

    finally:
        db.close()