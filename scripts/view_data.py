import sqlite3
import streamlit as st
import pandas as pd

def load_table_data(db_name, table_name):
    try:
        conn = sqlite3.connect(db_name)
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql_query(query, conn)
        conn.close()
        return data
    except sqlite3.Error as e:
        st.error(f"Error al cargar la tabla '{table_name}': {e}")
        return None

st.title("Datos de la NBA")

# Base de datos y tablas
db_name = "./data/nba_stats.db"
tables = ["per_game_stats_home", "per_game_stats_away", "total_stats_home", "total_stats_away"]

# Mostrar tablas
for table in tables:
    st.subheader(f"Tabla: {table}")
    data = load_table_data(db_name, table)
    if data is not None:
        st.dataframe(data)
