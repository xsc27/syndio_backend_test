import json

from starlette.testclient import TestClient

from syndio_backend_test import api, main, sql

DATA = [
    {"id": 1, "gender": "male"},
    {"id": 2, "gender": "male"},
    {"id": 3, "gender": "male"},
    {"id": 4, "gender": "female"},
    {"id": 5, "gender": "female"},
    {"id": 6, "gender": "female"},
]


def test_sql():
    assert list(sql.get_rows(sql.get_db_conn(), "employees")) == DATA


def test_api():
    res = TestClient(api.API).get("employees")
    assert res.status_code == 200
    assert res.json() == DATA
