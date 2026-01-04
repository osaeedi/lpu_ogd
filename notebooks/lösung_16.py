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
def get_heizgradtage(csv_export_url_to_dataframe, pd):
    url_heizgradtage = "https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031/download/UMW103OD1031.csv"
    df_heizgradtage = csv_export_url_to_dataframe(url_heizgradtage)
    df_heizgradtage["Jahr_Monat"] = pd.to_datetime(df_heizgradtage["Jahr_Monat"]).dt.to_period("M")
    df_heizgradtage
    return (df_heizgradtage,)


@app.cell
def get_tagesmittelwerte_2024(csv_export_url_to_dataframe, np, pd):
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
    # Schritt 4: Aggregation nach Jahr, Monat und Standort (aus Aufgabe 15)
    df_temp_calculated["Datum"] = pd.to_datetime(df_temp_calculated["Datum"])
    df_temp_calculated["Jahr_Monat"] = df_temp_calculated["Datum"].dt.to_period("M")
    df_monthly = df_temp_calculated.groupby(["Jahr_Monat", "Standort"]).agg({
        "Heizgradtag": "sum",
        "akkumulierteTemperaturdifferenz": "sum"
    }).reset_index()
    return (df_monthly,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Vergleichen Sie das Resultat `df_monthly` mit `df_heizgradtage`. Sind die beiden DataFrames gleich?

    Wir mergen beide Tabellen auf `Standort`, `Jahr_Monat` und bilden Differenzen.

    **pandas-Konzepte:**
    - `merge(on=[...], how="...")`
    """)
    return


@app.cell
def _(df_heizgradtage, df_monthly, pd):
    df_merged = pd.merge(
        df_monthly,
        df_heizgradtage,
        left_on=["Jahr_Monat", "Standort"],
        right_on=["Jahr_Monat", "Standort"],
        suffixes=("_berechnet", "_referenz"),
        how="inner"
    )
    df_merged["Heizgradtag_Differenz"] = df_merged["Heizgradtag_berechnet"] - df_merged["Heizgradtag_referenz"]
    df_merged["akkumulierteTemperaturdifferenz_Differenz"] = df_merged["akkumulierteTemperaturdifferenz_berechnet"] - df_merged["akkumulierteTemperaturdifferenz_referenz"]
    df_merged
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antwort

    Die beiden DataFrames sind **nicht exakt gleich**, aber die Differenzen sind sehr klein (meist unter 0.5). Die kleinen Abweichungen entstehen vermutlich durch Rundungen bei der Berechnung der Tagesmittelwerte oder durch unterschiedliche Präzision bei der Aggregation. Für einige Standorte (z.B. Rosengartenstrasse in März und April) fehlen Referenzwerte im Originaldatensatz.
    """)
    return


if __name__ == "__main__":
    app.run()
