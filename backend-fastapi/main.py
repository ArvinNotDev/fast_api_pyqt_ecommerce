from fastapi import FastAPI
from setup import Base, engine
from apps.accounts.routers import router as accounts_router
from apps.accounts.models import *
# from apps.cart.routers import router as cart_router
# from apps.order.routers import router as order_router
# from apps.products.routers import router as products_router

app = FastAPI(title="Backend FastAPI Project")
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(accounts_router, tags=["accounts"])
# app.include_router(cart_router, prefix="/cart", tags=["cart"])
# app.include_router(order_router, prefix="/orders", tags=["orders"])
# app.include_router(products_router, prefix="/products", tags=["products"])



# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Backend FastAPI"}
