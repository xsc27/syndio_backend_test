#!/usr/bin/env python3
"""Starts web application."""
import os

import uvicorn


def main():
    """Start web application."""
    host = os.environ.get("HOST")
    if not host:
        host = "0.0.0.0" if os.getenv("DYNO") else "127.0.0.1"  # noqa: S104
    port = os.getenv("PORT", "")
    port = int(port) if port.isdigit() else 5000
    uvicorn.run("syndio_backend_test.api:API", host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
