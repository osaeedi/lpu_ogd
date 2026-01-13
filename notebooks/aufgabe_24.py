# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.7",
#     "numpy==2.3.4",
#     "pandas==2.3.3",
#     "requests==2.32.5",
# ]
# ///

import marimo

__generated_with = "0.19.2"
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
def get_heizgradtage(csv_export_url_to_dataframe):
    url_heizgradtage = "https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031/download/UMW103OD1031.csv"
    df_heizgradtage = csv_export_url_to_dataframe(url_heizgradtage)
    df_heizgradtage
    return (df_heizgradtage,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Diese Aufgabe baut auf Aufgabe 23 auf.

    Ziel ist es zu prüfen, ob sich die Verteilung der `Heizgradtag`-Werte in **Fluntern** über die Zeit verändert hat.

    1. Filtern Sie den Datensatz auf den Standort **Fluntern**.
    2. Verwenden Sie denselben Monat wie in Aufgabe 23 (der Monat mit dem höchsten Mittelwert in Fluntern) und filtern Sie auf genau diesen Monat.
    3. Erstellen Sie aus dem Jahr eine **30-Jahres-Gruppe** (Klimaperiode), z. B. als Kategorien
       1966--1995, 1996--2025, ...
       (je nach Datenverfügbarkeit; wichtig ist die Gruppierung in 30-Jahres-Blöcke).
    4. Zeichnen Sie einen **Boxplot** der `Heizgradtag`-Werte pro 30-Jahres-Gruppe.
    5. Interpretieren Sie den Plot in 3--5 Stichworten:
       - Hat sich der **Median** verschoben?
       - Hat sich die **Streuung** (IQR) verändert?
       - Gibt es mehr/weniger **Ausreisser**?

    **Hinweis (pandas):** Eine 30-Jahres-Gruppe kann man z. B. über ganzzahlige Division bauen:
    `periode_start = (Jahr // 30) * 30`
    und danach als Label `start--start+29` formatieren.

    Hier eine kleine Intro zu matplotlib:
    ```python
    import matplotlib.pyplot as plt

    # Boxplot
    plt.figure()
    plt.boxplot([data1, data2], labels=["Gruppe 1", "Gruppe 2"])
    plt.title("Boxplot"); plt.xlabel("Gruppe"); plt.ylabel("Wert"); plt.grid(True)
    plt.show()
    ```
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(df_heizgradtage):
    # TODO: Filtern Sie auf Standort "Fluntern"
    df_fluntern = df_heizgradtage
    # TODO: Bestimmen Sie den Monat mit dem höchsten Mittelwert (aus Aufgabe 23)
    # Hinweis: Sie können dies aus Aufgabe 23 übernehmen oder hier neu berechnen
    monat_fluntern = 1  # Platzhalter - ersetzen Sie dies
    return (df_fluntern,)


@app.cell
def _(df_fluntern):
    # TODO: Filtern Sie auf diesen Monat
    df_fluntern_monat = df_fluntern
    # TODO: Erstellen Sie eine 30-Jahres-Gruppe (Klimaperiode) aus dem Jahr
    # Hinweis: Verwenden Sie ganzzahlige Division: periode_start = (Jahr // 30) * 30
    # Formatieren Sie dann als "start--start+29"
    df_fluntern_monat = df_fluntern_monat.copy()
    # TODO: Berechnen Sie periode_start
    # TODO: Erstellen Sie das Label als "start--start+29"
    return


@app.cell
def _(plt):
    # TODO: Erstellen Sie einen Boxplot der Heizgradtag-Werte pro 30-Jahres-Gruppe
    plt.figure(figsize=(12, 6))
    # TODO: Erstellen Sie den Boxplot
    plt.title("Heizgradtag-Verteilung nach 30-Jahres-Gruppen (Fluntern)")
    plt.xlabel("30-Jahres-Gruppe (Klimaperiode)")
    plt.ylabel("Heizgradtag")
    plt.grid(True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interpretation des Boxplots

    Beantworten Sie die folgenden Fragen in 3--5 Stichworten:

    - **Hat sich der Median verschoben?** (z. B. "Median gesunken", "Median gestiegen", "Median stabil")
    - **Hat sich die Streuung (IQR) verändert?** (z. B. "IQR größer geworden", "IQR kleiner geworden", "IQR ähnlich")
    - **Gibt es mehr/weniger Ausreisser?** (z. B. "Mehr Ausreisser in späteren Perioden", "Weniger Ausreisser", "Ähnliche Anzahl")
    """)
    return


@app.cell
def _(mo):
    # TODO: Geben Sie Ihre Interpretation hier ein (3-5 Stichworte)
    interpretation = mo.md(r"""
    **Median:** 

    **Streuung (IQR):** 

    **Ausreisser:** 
    """)
    interpretation
    return


if __name__ == "__main__":
    app.run()
