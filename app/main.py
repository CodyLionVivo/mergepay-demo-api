"""mergepay-demo-api: a minimal product catalogue service."""

from fastapi import FastAPI

app = FastAPI(title="mergepay-demo-api")

PRODUCTS = [
    {
        "name": "Laptop",
        "sku": "LAP-001",
        "price": 3500.0,
        "stock": 10,
    },
    {
        "name": "Mouse",
        "sku": "MOU-001",
        "price": 80.0,
        "stock": 25,
    },
]


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products")
def list_products():
    return PRODUCTS
