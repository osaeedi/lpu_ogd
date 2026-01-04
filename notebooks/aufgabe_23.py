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
def get_heizgradtage(csv_export_url_to_dataframe):
    url_heizgradtage = "https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031/download/UMW103OD1031.csv"
    df_heizgradtage = csv_export_url_to_dataframe(url_heizgradtage)
    df_heizgradtage
    return (df_heizgradtage,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wählen Sie für jeden der folgenden Standorte den Monat mit dem höchsten Mittelwert (aus Aufgabe 22):
    - Fluntern
    - Heubeeribüel
    - Rosengartenstrasse
    - Schimmelstrasse
    - Stampfenbachstrasse

    iltern Sie den Datensatz auf diesen Monat und visualisieren Sie die Entwicklung der `Heizgradtag`-Werte über die Jahre hinweg als **Liniendiagramm** für jeden Standort. Beurteilen Sie knapp: Ist über die Zeit eher ein **Rückgang**, **Anstieg** oder **kein klarer Trend** zu erkennen? Gibt es genug Messungen, um eine aussagekräftige Analyse durchzuführen? Begründen Sie Ihre Antwort.

    Hier eine kleine Intro zu matplotlib:
    ```python
    import matplotlib.pyplot as plt

    # Liniendiagramm
    plt.figure()
    plt.plot(demo["x"], demo["y"], marker="o")
    plt.title("Linie"); plt.xlabel("x"); plt.ylabel("y"); plt.grid(True)
    plt.show()
    ```
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Fluntern
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Fluntern", bestimmen Sie den Monat mit dem höchsten Mittelwert,
    # filtern Sie auf diesen Monat und erstellen Sie ein Liniendiagramm
    df_fluntern = df_heizgradtage
    # TODO: Bestimmen Sie den Monat mit dem höchsten Mittelwert (aus Aufgabe 22)
    monat_fluntern = 1  # Platzhalter - ersetzen Sie dies
    # TODO: Filtern Sie auf diesen Monat
    df_fluntern_monat = df_fluntern
    # TODO: Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.grid(True)
    plt.show()
    # TODO: Beurteilen Sie knapp, ob über die Jahre eher Rückgang, Anstieg oder kein klarer Trend erkennbar ist
    # TODO: Haben sich die Heizgradtage über die Jahre geändert? Falls ja, in welche Richtung?
    # TODO: Gibt es genug Messungen, um eine aussagekräftige Analyse durchzuführen? Begründen Sie Ihre Antwort.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Heubeeribüel
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Heubeeribüel", bestimmen Sie den Monat mit dem höchsten Mittelwert,
    # filtern Sie auf diesen Monat und erstellen Sie ein Liniendiagramm
    df_heubeeri = df_heizgradtage
    # TODO: Bestimmen Sie den Monat mit dem höchsten Mittelwert (aus Aufgabe 22)
    monat_heubeeri = 1  # Platzhalter - ersetzen Sie dies
    # TODO: Filtern Sie auf diesen Monat
    df_heubeeri_monat = df_heubeeri
    # TODO: Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.grid(True)
    plt.show()
    # TODO: Beurteilen Sie knapp, ob über die Jahre eher Rückgang, Anstieg oder kein klarer Trend erkennbar ist
    # TODO: Haben sich die Heizgradtage über die Jahre geändert? Falls ja, in welche Richtung?
    # TODO: Gibt es genug Messungen, um eine aussagekräftige Analyse durchzuführen? Begründen Sie Ihre Antwort.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rosengartenstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Rosengartenstrasse", bestimmen Sie den Monat mit dem höchsten Mittelwert,
    # filtern Sie auf diesen Monat und erstellen Sie ein Liniendiagramm
    df_rosengarten = df_heizgradtage
    # TODO: Bestimmen Sie den Monat mit dem höchsten Mittelwert (aus Aufgabe 22)
    monat_rosengarten = 1  # Platzhalter - ersetzen Sie dies
    # TODO: Filtern Sie auf diesen Monat
    df_rosengarten_monat = df_rosengarten
    # TODO: Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.grid(True)
    plt.show()
    # TODO: Beurteilen Sie knapp, ob über die Jahre eher Rückgang, Anstieg oder kein klarer Trend erkennbar ist
    # TODO: Haben sich die Heizgradtage über die Jahre geändert? Falls ja, in welche Richtung?
    # TODO: Gibt es genug Messungen, um eine aussagekräftige Analyse durchzuführen? Begründen Sie Ihre Antwort.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Schimmelstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Schimmelstrasse", bestimmen Sie den Monat mit dem höchsten Mittelwert,
    # filtern Sie auf diesen Monat und erstellen Sie ein Liniendiagramm
    df_schimmelstr = df_heizgradtage
    # TODO: Bestimmen Sie den Monat mit dem höchsten Mittelwert (aus Aufgabe 22)
    monat_schimmelstr = 1  # Platzhalter - ersetzen Sie dies
    # TODO: Filtern Sie auf diesen Monat
    df_schimmelstr_monat = df_schimmelstr
    # TODO: Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.grid(True)
    plt.show()
    # TODO: Beurteilen Sie knapp, ob über die Jahre eher Rückgang, Anstieg oder kein klarer Trend erkennbar ist
    # TODO: Haben sich die Heizgradtage über die Jahre geändert? Falls ja, in welche Richtung?
    # TODO: Gibt es genug Messungen, um eine aussagekräftige Analyse durchzuführen? Begründen Sie Ihre Antwort.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Stampfenbachstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Stampfenbachstrasse", bestimmen Sie den Monat mit dem höchsten Mittelwert,
    # filtern Sie auf diesen Monat und erstellen Sie ein Liniendiagramm
    df_stampfenbach = df_heizgradtage
    # TODO: Bestimmen Sie den Monat mit dem höchsten Mittelwert (aus Aufgabe 22)
    monat_stampfenbach = 1  # Platzhalter - ersetzen Sie dies
    # TODO: Filtern Sie auf diesen Monat
    df_stampfenbach_monat = df_stampfenbach
    # TODO: Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.grid(True)
    plt.show()
    # TODO: Beurteilen Sie knapp, ob über die Jahre eher Rückgang, Anstieg oder kein klarer Trend erkennbar ist
    # TODO: Haben sich die Heizgradtage über die Jahre geändert? Falls ja, in welche Richtung?
    # TODO: Gibt es genug Messungen, um eine aussagekräftige Analyse durchzuführen? Begründen Sie Ihre Antwort.
    return


if __name__ == "__main__":
    app.run()
