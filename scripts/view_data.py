import sqlite3
import pandas as pd
import streamlit as st

# Conexión a la base de datos
conn = sqlite3.connect('data/nba_stats.db')

# Consultar tablas
st.title("Datos de la NBA")
st.header("Tabla: per_game_stats_home")

# Leer datos de la tabla `per_game_stats_home`
query_home = "SELECT * FROM per_game_stats_home"
df_home = pd.read_sql_query(query_home, conn)
st.dataframe(df_home)  # Mostrar tabla en Streamlit

st.header("Tabla: per_game_stats_away")

# Leer datos de la tabla `per_game_stats_away`
query_away = "SELECT * FROM per_game_stats_away"
df_away = pd.read_sql_query(query_away, conn)
st.dataframe(df_away)  # Mostrar tabla en Streamlit

# Cierra la conexión a la base de datos
conn.close()
