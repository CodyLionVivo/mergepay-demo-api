# mergepay-demo-api

Demo repository used to test MergePay. It is a small FastAPI service that
stands in for a client application whose work will later be verified by
MergePay. It is not MergePay itself.

## Stack

- Python 3.13
- FastAPI
- pytest + FastAPI TestClient
- Uvicorn

No database, no authentication.

## Running

```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## Endpoints

| Method | Path        | Description                     |
| ------ | ----------- | ------------------------------- |
| GET    | `/health`   | Service health check            |
| GET    | `/products` | List the in-memory products     |

Products live in a mutable in-memory list, `PRODUCTS`, in `app/main.py`.

## Tests

```bash
python -m pytest tests/regression -q   # must pass
python -m pytest tests/acceptance -q   # fails until the task below is done
```

## Pending task

**Implement CSV export**

Add `GET /products/export`, which returns the products as a CSV file.

### Acceptance criteria

- GET /products/export exists
- response is valid CSV
- columns are name, sku, price, stock
- works with zero products
- works with 100 products
- existing tests continue passing

The acceptance tests in `tests/acceptance/test_export_csv.py` already describe
these criteria and currently fail, because the endpoint does not exist yet.

## Protected files

For this task MergePay treats the following as protected. The developer
implementing the task must not modify them:

- `.github/workflows/mergepay-ci.yml`
- `tests/regression/**`
- `tests/acceptance/**`
- `requirements.txt`

## CI

`.github/workflows/mergepay-ci.yml` runs on pull requests targeting `main` and
publishes three check runs: `build`, `regression-tests` and `acceptance-tests`.

## Verification test

This branch is used to test MergePay pull request inspection.
