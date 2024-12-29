import pandas as pd
from sqlalchemy import create_engine, text
from config import DATABASE_URL


def get_engine():
    """Create and return the database engine."""
    return create_engine(DATABASE_URL)


def get_tables(engine):
    """
    Dynamically fetch available tables from the database.
    Works with SQLite and adapts if no tables are found.
    """
    query = text("SELECT name FROM sqlite_master WHERE type='table';")  # Query for SQLite tables

    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            tables = result.fetchall()

        if not tables:
            raise ValueError("No tables found in the database.")  # Handle empty database gracefully

        # Dynamically build DataFrame
        return pd.DataFrame(tables, columns=['name'])

    except Exception as ex:
        raise Exception(f"Error fetching tables: {str(ex)}")


def get_columns(table_name, engine):
    """
    Dynamically fetch column names for a given table.
    Uses PRAGMA for SQLite databases to retrieve metadata.
    """
    query = text(f"PRAGMA table_info([{table_name}]);")  # SQLite-specific query for column metadata

    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            columns_metadata = result.fetchall()  # Fetch metadata for columns

        # Extract the columns from the metadata
        if not columns_metadata:
            raise ValueError(f"No columns found for table '{table_name}'.")

        # Dynamically build DataFrame
        return pd.DataFrame(columns_metadata, columns=['cid', 'name', 'type', 'notnull', 'dflt_value', 'pk'])

    except Exception as ex:
        raise Exception(f"Error fetching columns for table '{table_name}': {str(ex)}")
