import sqlite3

# Conectar a la base de datos
connection = sqlite3.connect("../data/nba_stats.db")

# Crear un cursor
cursor = connection.cursor()

# Verificar los datos de la tabla "per_game_stats_home"
print("Datos de 'per_game_stats_home':")
for row in cursor.execute("SELECT * FROM per_game_stats_home LIMIT 5"):
    print(row)

# Verificar los datos de la tabla "per_game_stats_away"
print("\nDatos de 'per_game_stats_away':")
for row in cursor.execute("SELECT * FROM per_game_stats_away LIMIT 5"):
    print(row)

# Cerrar la conexión
connection.close()
