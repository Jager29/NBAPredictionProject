import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Definir las URLs de las nuevas tablas
URLS = {
    "total_stats_home": "https://www.basketball-reference.com/leagues/NBA_2024.html#totals-team",
    "total_stats_away": "https://www.basketball-reference.com/leagues/NBA_2024.html#totals-opponent",
}

# Crear la carpeta de salida si no existe
output_dir = "../data/raw"
os.makedirs(output_dir, exist_ok=True)


def fetch_and_save_table(url, table_id, output_file):
    """Función para obtener una tabla HTML y guardarla como CSV."""
    print(f"Procesando: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Buscar la tabla correspondiente
    table = soup.find("table", {"id": table_id})
    if table:
        print(f"Tabla '{table_id}' encontrada.")
        df = pd.read_html(str(table))[0]
        # Guardar el DataFrame como CSV
        output_path = os.path.join(output_dir, output_file)
        df.to_csv(output_path, index=False)
        print(f"Tabla '{table_id}' guardada como {output_file}")
    else:
        print(f"Tabla '{table_id}' no encontrada en la página.")


def main():
    # Scrape y guarda solo las nuevas tablas
    fetch_and_save_table(URLS["total_stats_home"], "totals-team", "total_stats_home.csv")
    fetch_and_save_table(URLS["total_stats_away"], "totals-opponent", "total_stats_away.csv")


if __name__ == "__main__":
    main()
