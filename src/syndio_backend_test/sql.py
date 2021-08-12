"""Database interface."""
import atexit
import logging
import sqlite3
from pathlib import Path
from typing import Iterator

import httpx

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.ERROR)


def _get_db(name: str = "employees.db", force: bool = False) -> Path:
    """Fetch database."""
    db = Path(name)

    if db.exists() and not force:
        logging.debug(f"Database {db} exists.")
        return db

    logging.info(f"Downloading database {db}.")
    res = httpx.get(
        "https://drive.google.com/uc?export=download&id=1KOpKLtj-beaBt3IeaEU-gb_RSdWVKfiK"
    )
    with db.open("w+b") as fd:
        fd.write(res.content)
    return db


def _close_db(connection: sqlite3.connect) -> None:
    """Close connections."""
    logging.debug(f"Closing {str(connection)}.")
    connection.close()


def get_rows(connection: sqlite3.connect, row: str) -> Iterator:
    """Return iterator of rows as key values."""
    cmd = f"SELECT * FROM {row}"  # noqa: S608
    logging.debug(f"Executing `{cmd}`")
    data = connection.execute(cmd)
    return (dict(zip(row.keys(), row)) for row in data)


def get_db_conn() -> sqlite3.connect:
    """Return connection to database."""
    con = sqlite3.connect(_get_db())
    con.row_factory = sqlite3.Row
    atexit.register(_close_db, con)
    return con
