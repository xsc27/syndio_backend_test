#!/usr/bin/env python3
"""Starts web application."""
import os

import uvicorn

from syndio_backend_test import api


def main():
    """Start web application."""
    port = os.environ.get("PORT", "")
    port = int(port) if port.isdigit() else 5000
    uvicorn.run(api.API, host="127.0.0.1", port=port, log_level="info")


if __name__ == "__main__":
    main()
