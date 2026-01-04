# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "pandas==2.3.3",
#     "requests==2.32.5",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    return io, mo, pd, requests


@app.cell
def _(io, pd, requests):
    def csv_export_url_to_dataframe(url: str) -> pd.DataFrame:
        """
        Lädt eine CSV von einer direkten HTTP(s)-URL und gibt ein DataFrame zurück.

        Args:
            url: Direkte Download-URL zur CSV.

        Returns:
            pd.DataFrame
        """
        resp = requests.get(url)
        resp.raise_for_status()
        df = pd.read_csv(io.BytesIO(resp.content), sep=None, engine="python", encoding="utf-8")
        return df
    return (csv_export_url_to_dataframe,)


@app.cell
def _(csv_export_url_to_dataframe):
    url = "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100112/exports/csv?lang=de&timezone=Europe%2FZurich&use_labels=true&delimiter=%3B"
    df = csv_export_url_to_dataframe(url)
    df
    return (df,)


@app.cell
def _(df):
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fehlende Werte & Ausreisser (Geschwindigkeitsmonitoring)

    Übernehmen Sie die implementierte IQR-Methode (`find_outliers_iqr`) aus Aufgabe 8 und nutzen Sie diese auf den Datensatz **Geschwindigkeitsmonitoring: Kennzahlen pro Mess-Standort**.

    1. Welche Spalten können auf fehlende Werte und Ausreisser untersucht werden? Erklären Sie, welche Spalten für eine solche Analyse geeignet sind und warum.

    2. Ist es eine gute Idee, fehlende Werte auszusortieren? Untersuchen Sie, ob es sinnvoll ist, fehlende Werte zu entfernen.

    3. IQR-Methode mit Standardparametern: Erklären Sie, warum die IQR-Methode mit $k=1.5$ und den Quantilen $0.25$ und $0.75$ fehlerlose Werte aussortiert.

    4. Anpassung der IQR-Methode: Erklären Sie, wie Sie die IQR-Methode anpassen können, um wirklich nur problematische Werte auszusortieren.
    """)
    return


if __name__ == "__main__":
    app.run()
