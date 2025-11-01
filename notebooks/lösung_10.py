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

__generated_with = "0.17.6"
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
def get_tagesmittelwerte_2024(csv_export_url_to_dataframe):
    url_tagesmittelwerte = "https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_tagesmittelwerte/download/ugz_ogd_meteo_d1_2024.csv"
    df_tagesmittelwerte = csv_export_url_to_dataframe(url_tagesmittelwerte)
    df_tagesmittelwerte
    return (df_tagesmittelwerte,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Daten transformieren (Tagesmittelwerte zu Heizgradtage)

    1. Filtern Sie in `df_tagesmittelwerte` die Zeilen mit **Tagesmittel der Lufttemperatur**.
    2. Manipulieren Sie `Standort` in `df_tagesmittelwerte`, sodass die Namen zu `df_heizgradtage` passen (einheitliche Schreibweise).
    3. Berechnen Sie `Heizgradtag` und `akkumulierteTemperaturdifferenz` nach der Definition im Datensatz [**"Heizgradtage und akkumulierte Temperaturdifferenzen für verschiedene Standorte in der Stadt Zürich"**](https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031).
    4. Aggregieren Sie den Datensatz `df_tagesmittelwerte` nach `Monat`, `Jahr` und `Standort`.
    5. Vergleichen Sie das Resultat mit `df_heizgradtage`. Was fällt Ihnen auf?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1) Relevante Zeilen auswählen (Temperatur-Mittelwerte)

    **pandas-Konzepte:**
    - `DataFrame.loc[mask, :]` oder `query()` zum Filtern
    """)
    return


@app.cell
def filter_temperature_rows(df_tagesmittelwerte):
    df_temp = df_tagesmittelwerte.loc[df_tagesmittelwerte['Parameter'] == 'T']
    df_temp
    return (df_temp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2) Spalte `Standort` manipulieren (Tagesdaten ↔ Referenzdatensatz)

    **pandas-Konzepte:**
    - string-Operationen via `DataFrame.replace()`
    """)
    return


@app.cell
def manipulate_standort(df_temp):
    df_temp_manipulated = df_temp.replace({"Standort": {"Zch_": ""}}, regex=True)
    df_temp_manipulated
    return (df_temp_manipulated,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3) Heizgradtag & akkumulierte Temperaturdifferenz berechnen

    - **Heizgradtag (HGT)** pro Tag: Wenn T < 12 °C, dann `20 - T`, sonst 0
    - **ATD (akk. Temp.-Differenz)** pro Tag: `max(0, 12 - T)`

    **pandas-Konzepte:**
    - Neue Spalten via `df["neue_spalte"] = ...`
    - Bedingte Logik via `np.where()`
    - Maximum-Funktion via `np.maximum(...)`
    """)
    return


@app.cell
def compute_hgt_and_monthly(df_temp_manipulated, np):
    df_temp_calculated = df_temp_manipulated
    df_temp_calculated["Heizgradtag"] = np.where(df_temp_calculated["Wert"] < 12, 20 - df_temp_calculated["Wert"], 0)
    df_temp_calculated["akkumulierteTemperaturdifferenz"] = np.maximum(0, 12 - df_temp_calculated["Wert"])
    df_temp_calculated
    return (df_temp_calculated,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4) Aggregation nach `Jahr`, `Monat` und `Standort`

    **pandas-Konzepte:**
    - `groupby(...).agg()`
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
    return (df_monthly,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 5) Vergleich mit Referenz (Heizgradtage-Monatsdatensatz)

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


if __name__ == "__main__":
    app.run()
