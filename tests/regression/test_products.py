"""Regression tests: the behaviour that already exists must keep working."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

EXPECTED_FIELDS = ("name", "sku", "price", "stock")


def test_health_returns_200():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_products_returns_200():
    response = client.get("/products")

    assert response.status_code == 200


def test_products_returns_the_two_initial_products():
    response = client.get("/products")
    products = response.json()

    assert len(products) == 2
    assert products[0] == {
        "name": "Laptop",
        "sku": "LAP-001",
        "price": 3500.0,
        "stock": 10,
    }
    assert products[1] == {
        "name": "Mouse",
        "sku": "MOU-001",
        "price": 80.0,
        "stock": 25,
    }


def test_products_contain_the_expected_fields():
    response = client.get("/products")

    for product in response.json():
        for field in EXPECTED_FIELDS:
            assert field in product
