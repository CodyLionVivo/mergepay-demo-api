"""mergepay-demo-api: a minimal product catalogue service."""

import csv
import io

from fastapi import FastAPI, Response

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


@app.get("/products/export")
def export_products():
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=["name", "sku", "price", "stock"])
    writer.writeheader()
    writer.writerows(PRODUCTS)
    return Response(content=output.getvalue(), media_type="text/csv")
