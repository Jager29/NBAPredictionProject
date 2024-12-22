import pandas as pd
import sqlite3

# Conectar a la base de datos
connection = sqlite3.connect("../data/nba_stats.db")

# Leer los CSV
home_stats = pd.read_csv("../data/raw/per_game_stats_home.csv")
away_stats = pd.read_csv("../data/raw/per_game_stats_away.csv")

# Guardar los datos en las tablas correspondientes
home_stats.to_sql("per_game_stats_home", connection, if_exists="replace", index=False)
away_stats.to_sql("per_game_stats_away", connection, if_exists="replace", index=False)

print("Datos cargados correctamente en la base de datos.")

# Cerrar la conexión
connection.close()
