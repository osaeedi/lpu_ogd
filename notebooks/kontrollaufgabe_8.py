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

__generated_with = "0.19.1"
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
        df = pd.read_csv(io.BytesIO(resp.content), sep=None, engine="python", encoding="utf-8")
        return df
    return (csv_export_url_to_dataframe,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Diese Aufgabe basiert auf Kontrollaufgabe 3. Nehmen Sie den Standort, den Sie in dieser Aufgabe gewählt haben, und zeigen Sie mithilfe eines Boxplots, ob das **Nudging** bei dieser Messstelle funktioniert hat oder nicht.
    """)
    return


@app.cell
def load_smiley_stats(csv_export_url_to_dataframe):
    # URL zum Datensatz mit Statistiken
    # Bitte durch die gefilterte URL vom Portal ersetzen (nach Standort gefiltert)
    url_stats = "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100277/exports/csv"
    df_stats = csv_export_url_to_dataframe(url_stats)
    df_stats
    return


@app.cell
def create_boxplot():
    # Erstellen Sie hier einen Boxplot, der die Geschwindigkeiten nach Phasen gruppiert
    # Phasen: Vormessung, Betrieb, Nachmessung
    # Zeigen Sie, ob das Nudging funktioniert hat

    # Ihre Implementierung hier
    pass
    return


if __name__ == "__main__":
    app.run()
