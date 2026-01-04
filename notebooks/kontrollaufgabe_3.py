# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.7",
#     "pandas==2.3.3",
#     "requests==2.32.5",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
 
    """)
    return


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt
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
def get_heizgradtage(csv_export_url_to_dataframe):
    url_hgt = "https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031/download/UMW103OD1031.csv"
    df_heizgradtage = csv_export_url_to_dataframe(url_hgt)
    df_heizgradtage
    return


@app.cell
def get_energieverbrauch(csv_export_url_to_dataframe):
    url_energie = "https://data.stadt-zuerich.ch/dataset/ugz_endenergiebilanz/download/ugz_endenergiebilanz.csv"
    df_energieverbrauch = csv_export_url_to_dataframe(url_energie)
    df_energieverbrauch
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Die Spalten `Holz_UW_BG_SK`, `Fernwaerme`, `Erdgas` und `Heizoel_EL` erfassen Energieträger zu Heizzwecken. Erstellen Sie aus `df_heizgradtage` und `df_energieverbrauch` ein DataFrame mit `Jahr`, `Heizgradtag`, `Heizenergieverbrauch`.
    """)
    return


if __name__ == "__main__":
    app.run()
