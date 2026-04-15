"""Database connection utilities for the BookTrack system."""

import sqlite3
from pathlib import Path

# Store the SQLite file in the project root for easy access.
DB_PATH = Path(__file__).resolve().parent.parent / "booktrack.db"


def get_connection():
    """Create and return a SQLite connection with row access by column name."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection
