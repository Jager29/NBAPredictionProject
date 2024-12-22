import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_and_save(url, table_id, filename):
    """
    Scrapes a specific table from a webpage and saves it as a CSV file.

    Args:
    - url (str): URL of the webpage.
    - table_id (str): The ID of the table to scrape.
    - filename (str): The name of the output CSV file.
    """
    print(f"Procesando: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar la tabla por ID
    table = soup.find('table', {'id': table_id})
    if table is not None:
        # Convertir la tabla en un DataFrame
        df = pd.read_html(str(table))[0]

        # Guardar el DataFrame como CSV
        df.to_csv(f"../data/raw/{filename}.csv", index=False)
        print(f"Tabla '{table_id}' guardada como ../data/raw/{filename}.csv")
    else:
        print(f"No se encontró la tabla con ID '{table_id}' en {url}")


# URLs y IDs de las tablas a descargar
urls_and_table_ids = [
    ("https://www.basketball-reference.com/leagues/NBA_2024.html", "per_game-team", "per_game_stats_home"),
    ("https://www.basketball-reference.com/leagues/NBA_2024.html", "per_game-opponent", "per_game_stats_away")
]

# Ejecutar el scraping para cada tabla
for url, table_id, filename in urls_and_table_ids:
    scrape_and_save(url, table_id, filename)
