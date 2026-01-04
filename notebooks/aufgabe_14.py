# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy==2.3.4",
#     "pandas==2.3.3",
#     "requests==2.32.5",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    import numpy as np
    return io, mo, pd, requests


@app.cell
def csv_export_url_to_dataframe(io, pd, requests):
    def csv_export_url_to_dataframe(url: str) -> pd.DataFrame:
        """
        Lädt eine CSV von einer direkten HTTP(s)-URL und gibt ein DataFrame zurück.
        Erkennt das Trennzeichen automatisch.

        Args:
            url: Direkte Download-URL zur CSV.

        Returns:
            pd.DataFrame
        """
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        df = pd.read_csv(io.BytesIO(resp.content), encoding="utf-8")
        return df
    return (csv_export_url_to_dataframe,)


@app.cell
def get_tagesmittelwerte_2024(csv_export_url_to_dataframe):
    url_tagesmittelwerte = "https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_tagesmittelwerte/download/ugz_ogd_meteo_d1_2024.csv"
    df_tagesmittelwerte = csv_export_url_to_dataframe(url_tagesmittelwerte)
    # Schritt 1: Filterung nach Tagesmittel der Lufttemperatur (aus Aufgabe 12)
    df_temp = df_tagesmittelwerte.loc[df_tagesmittelwerte['Parameter'] == 'T']
    # Schritt 2: Standort manipulieren (aus Aufgabe 13)
    df_temp_manipulated = df_temp.replace({"Standort": {"Zch_": ""}}, regex=True)
    return (df_temp_manipulated,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Berechnen Sie `Heizgradtag` und `akkumulierteTemperaturdifferenz` nach der Definition im Datensatz [**"Heizgradtage und akkumulierte Temperaturdifferenzen für verschiedene Standorte in der Stadt Zürich"**](https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031).

    - **Heizgradtag (HGT)** pro Tag: Wenn T < 12 °C, dann `20 - T`, sonst 0
    - **ATD (akk. Temp.-Differenz)** pro Tag: `max(0, 12 - T)`

    **pandas-Konzepte:**
    - Neue Spalten via `df["neue_spalte"] = ...`
    - Bedingte Logik via `np.where()`
    - Maximum-Funktion via `np.maximum(...)`
    """)
    return


@app.cell
def compute_hgt_and_monthly(df_temp_manipulated):
    # TODO: Berechnen Sie `Heizgradtag` und `akkumulierteTemperaturdifferenz` als neue Spalten
    df_temp_calculated = df_temp_manipulated
    df_temp_calculated["Heizgradtag"] = 0
    df_temp_calculated["akkumulierteTemperaturdifferenz"] = 0
    df_temp_calculated
    return


if __name__ == "__main__":
    app.run()
