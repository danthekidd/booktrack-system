"""Functions for creating the database schema and inserting starter records."""

from pathlib import Path
from src.db import get_connection

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_FILE = PROJECT_ROOT / "sql" / "schema.sql"
SAMPLE_DATA_FILE = PROJECT_ROOT / "sql" / "sample_data.sql"


def create_tables():
    """Create all tables using the SQL schema file."""
    try:
        with get_connection() as connection:
            schema_sql = SCHEMA_FILE.read_text(encoding="utf-8")
            connection.executescript(schema_sql)
            print("Tables created successfully.")
    except Exception as error:
        print(f"Error creating tables: {error}")


def insert_sample_data():
    """Insert sample records for testing reports and queries."""
    try:
        with get_connection() as connection:
            sample_sql = SAMPLE_DATA_FILE.read_text(encoding="utf-8")
            connection.executescript(sample_sql)
            print("Sample data inserted successfully.")
    except Exception as error:
        print(f"Error inserting sample data: {error}")
