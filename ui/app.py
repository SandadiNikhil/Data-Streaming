import streamlit as st
import time
import psycopg2
from psycopg2 import OperationalError
import logging
import pandas as pd
from streamlit_autorefresh import st_autorefresh


# Configure logging
logging.basicConfig(level=logging.INFO)

# Database connection parameters
DB_HOST = "postgres"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"

def fetch_data():
    """Fetch data from the PostgreSQL database."""
    try:
        logging.info("Attempting to connect to the database...")
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        logging.info("Connected to the database successfully.")
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, city, average_temperature 
                       FROM weather
                       """)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        logging.info("Fetched data successfully.")
        logging.info(rows)
        return pd.DataFrame(
            rows,
            columns=["id", "city", "average_temperature"]
        )
    except OperationalError as e:
        logging.error(f"Error fetching data: {e}")
        st.error(f"OperationalError: {e}")
        return pd.DataFrame()

st.set_page_config(page_title="Weather Dashboard", layout="centered")
st.title("🌡️ Live Weather Averages")

refresh_rate = st.slider("Refresh interval (seconds)", 2, 15, 5)
st_autorefresh(interval=refresh_rate * 1000, key="refresh")

data = fetch_data()

if not data.empty:
    st.table(data)
else:
    st.write("No data available.")