import streamlit as st
from database import get_engine, get_tables, get_columns
import pandas as pd
from sqlalchemy import text, insert


# Cache data with TTL
@st.cache_data(ttl=300)
def fetch_data(table_name, _engine):
    """Fetch data from a specific table."""
    query = text(f"SELECT * FROM [{table_name}]")
    try:
        with _engine.connect() as conn:
            result = conn.execute(query).fetchall()
    except Exception as e:
        raise Exception(f"Error fetching data for table `{table_name}`: {str(e)}")
    return pd.DataFrame(result)


@st.cache_data(ttl=300)
def fetch_columns(table_name, _engine):
    """Fetch column names for a given table."""
    query = text(f"PRAGMA table_info([{table_name}]);")
    try:
        with _engine.connect() as conn:
            result = conn.execute(query).fetchall()
    except Exception as e:
        raise Exception(f"Error fetching columns for table `{table_name}`: {str(e)}")
    return pd.DataFrame(result, columns=["cid", "name", "type", "notnull", "dflt_value", "pk"])


def explore_database_page(engine):
    """Page for exploring the database."""
    st.title("📊 Database Explorer")
    st.markdown("Explore tables, data, and metadata in your SQLite database.")

    # Step 1: Retrieve tables
    try:
        tables = get_tables(engine)
        table_names = tables['name'].tolist()
        if not table_names:
            st.warning("No tables found in the database.")
            return
    except Exception as e:
        st.error(f"Error fetching table list: {str(e)}")
        return

    # Step 2: Table selector
    selected_table = st.selectbox("Select a table to explore:", table_names)

    # Step 3: Fetch and display columns
    try:
        columns = get_columns(selected_table, engine)
        st.subheader(f"Table Schema for `{selected_table}`")
        st.dataframe(columns)
    except Exception as e:
        st.error(f"Error fetching table columns: {str(e)}")
        return

    # Step 4: Fetch data
    try:
        data = fetch_data(selected_table, engine)
        st.subheader(f"Data from `{selected_table}`")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")


def add_data_page(engine):
    """Page for adding data to the database."""
    st.title("➕ Add Data to Database")
    st.markdown("Fill out the form below to add a row to a table in the database.")

    # Step 1: Get available tables
    try:
        tables = get_tables(engine)
        table_names = tables['name'].tolist()
        if not table_names:
            st.warning("No tables found in the database.")
            return
    except Exception as e:
        st.error(f"Error fetching table list: {str(e)}")
        return

    # Step 2: Select a table to add data to
    selected_table = st.selectbox("Select a table to add data to:", table_names)

    # Step 3: Fetch column metadata for the selected table
    try:
        columns_metadata = fetch_columns(selected_table, engine)
        column_names = columns_metadata["name"].tolist()
        column_types = columns_metadata["type"].tolist()
    except Exception as e:
        st.error(f"Error fetching table columns: {str(e)}")
        return

    # Step 4: Dynamically generate input fields for each column
    new_row = {}
    st.markdown(f"### Add a new row to `{selected_table}`:")
    for name, col_type in zip(column_names, column_types):
        if col_type.lower() in ["integer", "int"]:
            new_row[name] = st.number_input(f"{name} (Integer):", step=1, format="%d")
        elif col_type.lower() in ["real", "float", "double"]:
            new_row[name] = st.number_input(f"{name} (Float):", format="%f")
        elif col_type.lower() in ["text", "varchar", "char", "string"]:
            new_row[name] = st.text_input(f"{name} (Text):")
        else:
            new_row[name] = st.text_input(f"{name} (Unknown type `{col_type}`):")

    # Step 5: Submit Button
    if st.button("Submit"):
        try:
            with engine.connect() as conn:
                conn.execute(text(
                    f"INSERT INTO [{selected_table}] ({', '.join(new_row.keys())}) VALUES ({', '.join([':val_' + k for k in new_row.keys()])})"),
                             **{f"val_{k}": v for k, v in new_row.items()})
                st.success(f"New row added successfully to `{selected_table}`!")
        except Exception as e:
            st.error(f"Error inserting row into `{selected_table}`: {str(e)}")


def main():
    st.sidebar.title("🗂 Database App")
    page = st.sidebar.radio("Select a Page:", ["Explore Database", "Add Data"])

    # Get database engine
    try:
        engine = get_engine()
    except Exception as e:
        st.error(f"Error establishing database connection: {str(e)}")
        return

    # Navigate to the selected page
    if page == "Explore Database":
        explore_database_page(engine)
    elif page == "Add Data":
        add_data_page(engine)


if __name__ == "__main__":
    main()
