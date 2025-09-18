"""
Ingestion météo - Paris (via Open-Meteo)

But :
- Récupérer les données météo quotidiennes de Paris pour une période choisie
- Sauvegarder un CSV brut dans data/raw/
- Fonctionner aussi bien pour une seule année (ex: 2013) que pour plusieurs (ex: 2013-2024)
"""

import requests
import pandas as pd
from pathlib import Path

# -------- PARAMÈTRES À ADAPTER --------
LAT, LON = 48.8566, 2.3522   # Coordonnées Paris
ANNEE_DEBUT = 2013
ANNEE_FIN = 2013            # tu peux mettre 2013 = 2013-2013, ou 2024 = 2013-2024

# Construction des dates automatiquement
START_DATE = f"{ANNEE_DEBUT}-01-01"
END_DATE = f"{ANNEE_FIN}-12-31"

# URL API Open-Meteo
URL = (
    "https://archive-api.open-meteo.com/v1/archive"
    f"?latitude={LAT}&longitude={LON}"
    f"&start_date={START_DATE}&end_date={END_DATE}"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,windspeed_10m_max"
    "&timezone=Europe/Paris"
)

# -------- SORTIE --------
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)
OUTFILE = RAW_DIR / f"meteo_paris.csv"

def main():
    print(f"➡️ Téléchargement météo de {START_DATE} à {END_DATE}...")

    response = requests.get(URL)
    response.raise_for_status()

    data = response.json()

    # Transformation en DataFrame
    df = pd.DataFrame(data["daily"])
    df.to_csv(OUTFILE, index=False)

    print(f"💾 Fichier météo brut sauvegardé : {OUTFILE.resolve()}")
    print("\n✅ Aperçu :")
    print(df.head())

if __name__ == "__main__":
    main()
