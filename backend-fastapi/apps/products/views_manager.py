from fastapi import HTTPException
from sqlalchemy.orm import Session
from apps.products.schemas import ProductCreate, ProductResponse
from apps.products.views import create_product, get_product_by_id
import json

def create_product_view(product: ProductCreate, db: Session) -> ProductResponse:
    try:
        return create_product(db, json.loads(product.model_dump_json()))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def get_product_view(product_id: str, db: Session) -> ProductResponse:
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product