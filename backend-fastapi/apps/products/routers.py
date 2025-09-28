from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from apps.products.schemas import ProductCreate, ProductResponse
from setup import get_db
from apps.products.views_manager import create_product_view, get_product_view


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=ProductResponse)
def create_Product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product_view(product, db)

@router.get("/", response_model=ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)):
    return get_product_view(product_id, db)
