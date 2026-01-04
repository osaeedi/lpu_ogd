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
        df = pd.read_csv(io.BytesIO(resp.content), encoding="utf-8")
        return df
    return (csv_export_url_to_dataframe,)


@app.cell
def get_tagesmittelwerte_2024(csv_export_url_to_dataframe, np):
    url_tagesmittelwerte = "https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_tagesmittelwerte/download/ugz_ogd_meteo_d1_2024.csv"
    df_tagesmittelwerte = csv_export_url_to_dataframe(url_tagesmittelwerte)
    # Schritt 1: Filterung nach Tagesmittel der Lufttemperatur (aus Aufgabe 12)
    df_temp = df_tagesmittelwerte.loc[df_tagesmittelwerte['Parameter'] == 'T']
    # Schritt 2: Standort manipulieren (aus Aufgabe 13)
    df_temp_manipulated = df_temp.replace({"Standort": {"Zch_": ""}}, regex=True)
    # Schritt 3: Heizgradtag & akkumulierte Temperaturdifferenz berechnen (aus Aufgabe 14)
    df_temp_calculated = df_temp_manipulated.copy()
    df_temp_calculated["Heizgradtag"] = np.where(df_temp_calculated["Wert"] < 12, 20 - df_temp_calculated["Wert"], 0)
    df_temp_calculated["akkumulierteTemperaturdifferenz"] = np.maximum(0, 12 - df_temp_calculated["Wert"])
    return (df_temp_calculated,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aggregieren Sie den Datensatz `df_temp_calculated` nach `Monat`, `Jahr` und `Standort`.

    **pandas-Konzepte:**
    - `groupby(...).agg()`
    - `pd.to_datetime()` und `.dt.to_period("M")`
    """)
    return


@app.cell
def aggregate_monthly(df_temp_calculated, pd):
    df_monthly = df_temp_calculated
    df_monthly["Datum"] = pd.to_datetime(df_monthly["Datum"])
    df_monthly["Jahr_Monat"] = df_monthly["Datum"].dt.to_period("M")
    df_monthly = df_temp_calculated.groupby(["Jahr_Monat", "Standort"]).agg({
        "Heizgradtag": "sum",
        "akkumulierteTemperaturdifferenz": "sum"
    }).reset_index()
    df_monthly
    return


if __name__ == "__main__":
    app.run()
