"""Acceptance criteria for the pending task: "Implement CSV export".

These tests describe GET /products/export, which does not exist yet.
They are expected to fail until the endpoint is implemented.
"""

import copy
import csv
import io

import pytest
from fastapi.testclient import TestClient

from app import main
from app.main import app

client = TestClient(app)

EXPECTED_COLUMNS = ["name", "sku", "price", "stock"]


@pytest.fixture(autouse=True)
def restore_products():
    """Let each test mutate PRODUCTS and hand back the original afterwards."""
    original = copy.deepcopy(main.PRODUCTS)
    yield
    main.PRODUCTS[:] = copy.deepcopy(original)


def read_csv(response):
    return list(csv.reader(io.StringIO(response.text)))


def make_products(count):
    return [
        {
            "name": f"Product {index}",
            "sku": f"SKU-{index:03d}",
            "price": float(index),
            "stock": index,
        }
        for index in range(count)
    ]


def test_export_endpoint_exists():
    response = client.get("/products/export")

    assert response.status_code == 200


def test_export_returns_csv():
    response = client.get("/products/export")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    assert read_csv(response), "response body is not parsable CSV"


def test_export_has_exactly_the_expected_columns():
    response = client.get("/products/export")

    assert response.status_code == 200
    rows = read_csv(response)
    assert rows[0] == EXPECTED_COLUMNS


def test_export_with_zero_products_has_header_and_no_rows():
    main.PRODUCTS[:] = []

    response = client.get("/products/export")

    assert response.status_code == 200
    rows = read_csv(response)
    assert rows[0] == EXPECTED_COLUMNS
    assert len(rows) == 1


def test_export_with_100_products_has_100_data_rows():
    main.PRODUCTS[:] = make_products(100)

    response = client.get("/products/export")

    assert response.status_code == 200
    rows = read_csv(response)
    assert rows[0] == EXPECTED_COLUMNS
    assert len(rows) - 1 == 100
