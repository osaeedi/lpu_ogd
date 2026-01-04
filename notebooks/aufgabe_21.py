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
    ## Streudiagramm für alle Standorte

    Untersuchen Sie mithilfe eines Streudiagramms, ob `Heizgradtag` und `akkumulierteTemperaturdifferenz` zusammenhängen.

    Erstellen Sie für jeden der folgenden Standorte ein Streudiagramm:
    - Fluntern
    - Heubeeribüel
    - Rosengartenstrasse
    - Schimmelstrasse
    - Stampfenbachstrasse

    Was ist der Unterschied zwischen `Heizgradtag` und `akkumulierteTemperaturdifferenz`? Erklären Sie die beiden Konzepte und deren Berechnung.

    Hier eine kleine Intro zu matplotlib:
    ```python
    import matplotlib.pyplot as plt

    # Streudiagramm
    plt.figure()
    plt.scatter(demo["x"], demo["y"])
    plt.title("Streuung"); plt.xlabel("x"); plt.ylabel("y"); plt.grid(True)
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
    # TODO: Filtern Sie auf Standort "Fluntern" und erstellen Sie ein Streudiagramm
    df_fluntern = df_heizgradtage
    # TODO: Erstellen Sie das Streudiagramm
    plt.figure(figsize=(12, 6))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Heubeeribüel
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Heubeeribüel" und erstellen Sie ein Streudiagramm
    df_heubeeri = df_heizgradtage
    # TODO: Erstellen Sie das Streudiagramm
    plt.figure(figsize=(12, 6))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rosengartenstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Rosengartenstrasse" und erstellen Sie ein Streudiagramm
    df_rosengarten = df_heizgradtage
    # TODO: Erstellen Sie das Streudiagramm
    plt.figure(figsize=(12, 6))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Schimmelstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Schimmelstrasse" und erstellen Sie ein Streudiagramm
    df_schimmelstr = df_heizgradtage
    # TODO: Erstellen Sie das Streudiagramm
    plt.figure(figsize=(12, 6))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Stampfenbachstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    # TODO: Filtern Sie auf Standort "Stampfenbachstrasse" und erstellen Sie ein Streudiagramm
    df_stampfenbach = df_heizgradtage
    # TODO: Erstellen Sie das Streudiagramm
    plt.figure(figsize=(12, 6))
    plt.show()
    return


if __name__ == "__main__":
    app.run()
