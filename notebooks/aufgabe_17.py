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
        df = pd.read_csv(io.BytesIO(resp.content), encoding="utf-8", sep=";")
        return df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Heizgradtage aus MeteoSwiss-Daten berechnen

    In dieser Aufgabe laden Sie Daten von einer Wetterstation Ihrer Wahl von MeteoSwiss und berechnen die Heizgradtage.

    **Schritte:**
    1. Wählen Sie eine Wetterstation von [MeteoSwiss](https://www.meteoswiss.admin.ch/services-and-publications/applications/ext/download-data-without-coding-skills.html) aus.
    2. Laden Sie die historischen Daten der Station (CSV-Format).
    3. Extrahieren Sie die Tagesmitteltemperaturen.
    4. Berechnen Sie die Heizgradtage und akkumulierte Temperaturdifferenz (wie in Aufgabe 14).
    5. Optional: Aggregieren Sie die Daten nach Monat und Jahr (wie in Aufgabe 15).

    **Hinweise:**
    - Die Tagesmitteltemperatur steht in der Spalte `tre200d0` (Temperatur in 2m Höhe)
    """)
    return


@app.cell
def _(pd):
    # TODO: Wählen Sie eine Wetterstation und laden Sie die Daten
    # Beispiel: Basel (BAS)
    # station_abbr = "BAS"  # Ändern Sie dies für Ihre gewählte Station
    # url = f"https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/{station_abbr.lower()}/ogd-smn_{station_abbr.lower()}_d_historical.csv"
    # df_meteoswiss = csv_export_url_to_dataframe(url)
    df_meteoswiss = pd.DataFrame()  # Platzhalter
    df_meteoswiss
    return (df_meteoswiss,)


@app.cell
def _(df_meteoswiss):
    # TODO: Extrahieren Sie die Tagesmitteltemperaturen
    # Konvertieren Sie `reference_timestamp` zu datetime
    # Filtern Sie auf die relevante Spalte (tre200d0)
    df_temp = df_meteoswiss
    df_temp
    return (df_temp,)


@app.cell
def _(df_temp):
    # TODO: Berechnen Sie Heizgradtag und akkumulierteTemperaturdifferenz
    # (wie in Aufgabe 14)
    df_temp_calculated = df_temp
    df_temp_calculated["Heizgradtag"] = 0
    df_temp_calculated["akkumulierteTemperaturdifferenz"] = 0
    df_temp_calculated
    return (df_temp_calculated,)


@app.cell
def _(df_temp_calculated):
    # TODO (optional): Aggregieren Sie die Daten nach Monat und Jahr
    # (wie in Aufgabe 15)
    df_monthly = df_temp_calculated
    df_monthly
    return


if __name__ == "__main__":
    app.run()
