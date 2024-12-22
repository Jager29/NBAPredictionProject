import sqlite3

# Crear la conexión a la base de datos
connection = sqlite3.connect("../data/nba_stats.db")

# Crear un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Crear las tablas para almacenar los datos
cursor.execute("""
CREATE TABLE IF NOT EXISTS per_game_stats_home (
    Rk INTEGER,
    Team TEXT,
    G INTEGER,
    MP REAL,
    FG REAL,
    FGA REAL,
    FG_percent REAL,
    ThreeP REAL,
    ThreePA REAL,
    ThreeP_percent REAL,
    TwoP REAL,
    TwoPA REAL,
    TwoP_percent REAL,
    FT REAL,
    FTA REAL,
    FT_percent REAL,
    ORB REAL,
    DRB REAL,
    TRB REAL,
    AST REAL,
    STL REAL,
    BLK REAL,
    TOV REAL,
    PF REAL,
    PTS REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS per_game_stats_away (
    Rk INTEGER,
    Team TEXT,
    G INTEGER,
    MP REAL,
    FG REAL,
    FGA REAL,
    FG_percent REAL,
    ThreeP REAL,
    ThreePA REAL,
    ThreeP_percent REAL,
    TwoP REAL,
    TwoPA REAL,
    TwoP_percent REAL,
    FT REAL,
    FTA REAL,
    FT_percent REAL,
    ORB REAL,
    DRB REAL,
    TRB REAL,
    AST REAL,
    STL REAL,
    BLK REAL,
    TOV REAL,
    PF REAL,
    PTS REAL
)
""")

# Confirmar los cambios y cerrar la conexión
connection.commit()
connection.close()

print("Base de datos y tablas configuradas correctamente.")
