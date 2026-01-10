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

__generated_with = "0.19.0"
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
    ## Kontrollaufgabe 3: Datenqualität Smiley-Geschwindigkeitsanzeigen

    Der Datensatz [Einzelmessungen der Smiley-Geschwindigkeitsanzeigen](https://data.bs.ch/explore/dataset/100268/) zeigt die Messungen von Verkehrsteilnehmenden, die bei einer Smiley-Geschwindigkeitsanzeige vorbeifahren. Smiley-Geschwindigkeitsanzeigen ist eine Nudging-Methode, die auf einem Display ein Smiley (meist Grün) oder ein trauriges Gesicht (meist rot) anzeigt, je nach dem, ob die Person zu schnell gefahren ist.

    **Hinweis:** Wenn Sie den Datensatz auf dem Portal nach Standort und Zyklus filtern, können Sie im **Export**-Register die URL zum gefilterten Datensatz erhalten.
    """)
    return


@app.cell
def load_smiley_data(csv_export_url_to_dataframe):
    # URL zum Datensatz (kann nach Standort/Zyklus gefiltert werden)
    # Beispiel-URL - bitte durch die gefilterte URL vom Portal ersetzen
    url_smiley = "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100268/exports/csv"
    df_smiley = csv_export_url_to_dataframe(url_smiley)
    df_smiley
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wie könnte man bei diesem Datensatz die Datenqualität verbessern? Wählen Sie einen Smiley-Standort in einem Zyklus Ihrer Wahl und implementieren Sie Ihre Idee.
    """)
    return


@app.cell
def improve_data_quality(df_filtered):
    # Implementieren Sie hier Ihre Ideen zur Datenqualitätsverbesserung
    # Mögliche Ansätze:
    # - Fehlende Werte behandeln
    # - Ausreisser identifizieren und behandeln
    # - Inkonsistenzen korrigieren
    # - Datentypen korrigieren
    # - Duplikate entfernen
    # etc.

    df_improved = df_filtered.copy()
    # Ihre Implementierung hier

    df_improved
    return


if __name__ == "__main__":
    app.run()
