"""
Ingestion RATP - trafic annuel entrant par station (métro/RER)

But :
- Télécharger le CSV depuis l’open data RATP
- Sauvegarder une copie brute dans data/raw/
- Afficher un aperçu pour vérifier
"""

import pandas as pd
from pathlib import Path

# 1) URL du dataset
URL = (
    "https://data.ratp.fr/explore/dataset/"
    "trafic-annuel-entrant-par-station-du-reseau-ferre/download/"
    "?format=csv&timezone=Europe/Berlin&lang=fr"
)

# 2) Préparer le dossier de sortie
RAW_DIR = Path("data/raw")               # dossier data/raw
RAW_DIR.mkdir(parents=True, exist_ok=True)  # crée data/raw si absent
OUTFILE = RAW_DIR / "ratp_trafic_annuel.csv"  # nom du fichier de sortie

def main():
    print("➡️ Téléchargement des données RATP…")

    # 3) Charger les données depuis l’URL
    df = pd.read_csv(URL, sep=";")  # important : CSV FR utilise souvent ";"

    # 4) Sauvegarder une copie brute en local
    df.to_csv(OUTFILE, index=False)
    print(f"💾 Fichier brut sauvegardé : {OUTFILE.resolve()}")

    # 5) Aperçu rapide
    print("\n✅ Aperçu des données :")
    print(df.head())

if __name__ == "__main__":
    main()
