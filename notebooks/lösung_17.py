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
    return io, mo, np, pd, requests


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
    return (csv_export_url_to_dataframe,)


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
    - Die MeteoSwiss CSV-Dateien verwenden `;` als Trennzeichen
    - Die Tagesmitteltemperatur steht in der Spalte `tre200d0` (Temperatur in 2m Höhe)
    """)
    return


@app.cell
def _(csv_export_url_to_dataframe):
    # Beispiel: Basel (BAS)
    station_abbr = "BAS"
    url = f"https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/{station_abbr.lower()}/ogd-smn_{station_abbr.lower()}_d_historical.csv"
    df_meteoswiss = csv_export_url_to_dataframe(url)
    df_meteoswiss
    return (df_meteoswiss,)


@app.cell
def _(df_meteoswiss, pd):
    # Extrahieren Sie die Tagesmitteltemperaturen
    # Konvertieren Sie reference_timestamp zu datetime
    df_temp = df_meteoswiss[["station_abbr", "reference_timestamp", "tre200d0"]].copy()
    df_temp["reference_timestamp"] = pd.to_datetime(df_temp["reference_timestamp"], format="%d.%m.%Y %H:%M")
    df_temp["Datum"] = df_temp["reference_timestamp"].dt.date
    df_temp = df_temp.rename(columns={"tre200d0": "Temperatur"})
    # Entfernen Sie Zeilen mit fehlenden Temperaturwerten
    df_temp = df_temp.dropna(subset=["Temperatur"])
    df_temp
    return (df_temp,)


@app.cell
def _(df_temp, np):
    # Berechnen Sie Heizgradtag und akkumulierteTemperaturdifferenz
    # (wie in Aufgabe 14)
    df_temp_calculated = df_temp.copy()
    df_temp_calculated["Heizgradtag"] = np.where(df_temp_calculated["Temperatur"] < 12, 20 - df_temp_calculated["Temperatur"], 0)
    df_temp_calculated["akkumulierteTemperaturdifferenz"] = np.maximum(0, 12 - df_temp_calculated["Temperatur"])
    df_temp_calculated
    return (df_temp_calculated,)


@app.cell
def _(df_temp_calculated, pd):
    # Aggregieren Sie die Daten nach Monat und Jahr
    # (wie in Aufgabe 15)
    df_temp_calculated["Datum"] = pd.to_datetime(df_temp_calculated["Datum"])
    df_temp_calculated["Jahr"] = df_temp_calculated["Datum"].dt.year
    df_temp_calculated["Monat"] = df_temp_calculated["Datum"].dt.month
    df_temp_calculated["Jahr_Monat"] = df_temp_calculated["Datum"].dt.to_period("M")

    df_monthly = df_temp_calculated.groupby(["Jahr_Monat", "station_abbr"]).agg({
        "Heizgradtag": "sum",
        "akkumulierteTemperaturdifferenz": "sum"
    }).reset_index()
    df_monthly
    return


if __name__ == "__main__":
    app.run()
