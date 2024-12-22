import sqlite3
import pandas as pd


def insert_table_from_csv(db_name, table_name, csv_path):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Leer el CSV en un DataFrame
        df = pd.read_csv(csv_path)

        # Insertar los datos en la tabla
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Tabla '{table_name}' insertada correctamente desde '{csv_path}'.")

    except Exception as e:
        print(f"Error al insertar la tabla '{table_name}': {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    # Rutas y nombres de los CSV y tablas
    db_name = "../data/nba_stats.db"

    csv_tables = {
        "total_stats_home": "../data/raw/total_stats_home.csv",
        "total_stats_away": "../data/raw/total_stats_away.csv"
    }

    # Insertar las tablas
    for table_name, csv_path in csv_tables.items():
        insert_table_from_csv(db_name, table_name, csv_path)
