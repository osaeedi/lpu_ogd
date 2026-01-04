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
    df_tagesmittelwerte
    return (df_tagesmittelwerte,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Filtern Sie in `df_tagesmittelwerte` die Zeilen mit **Tagesmittel der Lufttemperatur**.

    **pandas-Konzepte:**
    - `DataFrame.loc[mask, :]` oder `query()` zum Filtern
    """)
    return


@app.cell
def filter_temperature_rows(df_tagesmittelwerte):
    # TODO: Filterung nach Tagesmittel der Lufttemperatur in df_tagesmittelwerte
    df_temp = df_tagesmittelwerte
    df_temp
    return


if __name__ == "__main__":
    app.run()
