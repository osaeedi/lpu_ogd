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

__generated_with = "0.17.5"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Kontrollaufgaben
    """)
    return


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
def get_heizgradtage(csv_export_url_to_dataframe):
    url_hgt = "https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031/download/UMW103OD1031.csv"
    df_heizgradtage = csv_export_url_to_dataframe(url_hgt)
    df_heizgradtage
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kontrollaufgabe 1

    Die Heizgradtage (HGT) sind ein Mass für den Einfluss des Wetters auf den Heizenergieverbrauch eines Gebäudes. Gibt es einen Datensatz, der belegen könnte, dass weniger geheizt wird, wenn die Heizgradtage kleiner sind?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kontrollaufgabe 2

    Was fällt Ihnen an den Werten der Spalte `Holz_UW_BG_SK` auf? Identifizieren Sie Ausreisser (Outliers). Warum werden so viele Werte als Ausreisser erkannt?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Kontrollaufgabe 3
    Die Spalten `Holz_UW_BG_SK`, `Fernwaerme`, `Erdgas` und `Heizoel_EL` erfassen Energieträger zu Heizzwecken. Erstellen Sie aus `df_heizgradtage` und `df_energieverbrauch` ein DataFrame mit `Jahr`, `Heizgradtag`, `Heizenergieverbrauch`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kontrollaufgabe 4

    Visualisieren Sie den Zusammenhang zwischen Heizgradtagen und Heizenergieverbrauch mittels Scatterplot. Entspricht das Ihrer Erwartung? Begründen Sie. Welche Informationen fehlen für eine Beurteilung?
    """)
    return


if __name__ == "__main__":
    app.run()
