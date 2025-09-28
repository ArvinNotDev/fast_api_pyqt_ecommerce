from sqlalchemy.orm import Session
from apps.products.models import Product

def create_product(db: Session, product_data: dict) -> Product:
    """
    Create a new product in the database.
    """
    product = Product(**product_data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product_by_id(db: Session, product_id: str) -> Product | None:
    """
    Retrieve an product by its ID.
    Returns None if not found.
    """
    return db.query(Product).filter(Product.id == product_id).first()

def get_all_products(db: Session) -> list[Product]:
    """
    Retrieve all accounts from the database.
    """
    return db.query(Product).all()

def delete_account(db: Session, product_id: str) -> bool:
    """
    Delete an product by its ID.
    Returns True if deleted, False if not found.
    """
    product = get_product_by_id(db, product_id)
    if product:
        db.delete(product)
        db.commit()
        return True
    return False
