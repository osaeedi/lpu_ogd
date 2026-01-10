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
def get_energieverbrauch(csv_export_url_to_dataframe):
    url_energie = "https://data.stadt-zuerich.ch/dataset/ugz_endenergiebilanz/download/ugz_endenergiebilanz.csv"
    df_energieverbrauch = csv_export_url_to_dataframe(url_energie)
    df_energieverbrauch
    return (df_energieverbrauch,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Was fällt Ihnen an den Werten der Spalte `Holz_UW_BG_SK` auf? Identifizieren Sie Ausreisser (Outliers). Warum werden so viele Werte als Ausreisser erkannt?
    """)
    return


@app.cell
def outlier_function(pd):
    def is_outlier_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
        """
        IQR-basierte Ausreisser-Erkennung.

        Args:
            series: Numerische Werte.
            k: Multiplikator für die IQR-Bandbreite (Standard 1.5).

        Returns:
            Boolesche Maske gleicher Länge (True = Ausreisser).
        """
        s = pd.to_numeric(series, errors="coerce")
        q1 = s.quantile(0.25, interpolation="linear")
        q3 = s.quantile(0.75, interpolation="linear")
        iqr = q3 - q1
        lower = q1 - k * iqr
        upper = q3 + k * iqr
        mask = (s < lower) | (s > upper)
        return mask.fillna(False)
    return (is_outlier_iqr,)


@app.cell
def get_outliers(df_energieverbrauch, is_outlier_iqr):
    df_outliers = df_energieverbrauch[is_outlier_iqr(df_energieverbrauch["Holz_UW_BG_SK"])]
    df_outliers
    return


if __name__ == "__main__":
    app.run()
