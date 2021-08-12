"""OpenAPI."""
from fastapi import FastAPI

from syndio_backend_test import sql

API = FastAPI(
    title="Syndio Backend Test",
    description="Demo an API with data read from a sqlite.",
)


@API.get("/")
def read_root():
    """Display status."""
    return {"status": "up"}


@API.get("/employees")
@API.get("/employees/")
def read_employees():
    """Get employees."""
    return list(sql.get_rows(sql.get_db_conn(), "employees"))
