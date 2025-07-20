from fastapi import FastAPI
from app.routes import order,product
from app.routes import product,health,order
app=FastAPI()


app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(health.router, tags=["Health"])