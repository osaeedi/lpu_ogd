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
    Berechnen Sie den Monatsdurchschnitt der `Heizgradtag`-Werte für jeden der folgenden Standorte:

    - Fluntern
    - Heubeeribüel
    - Rosengartenstrasse
    - Schimmelstrasse
    - Stampfenbachstrasse

    Gruppieren Sie dazu nach dem Monat (nicht Jahr!), also nach dem Kalendermonat (1 bis 12).
    Visualisieren Sie die resultierenden 12 Mittelwerte als **Balkendiagramm** für jeden Standort.
    Welcher Monat weist für jeden Standort den **höchsten Durchschnitt** auf?

    Hier eine kleine Intro zu matplotlib:
    ```python
    import matplotlib.pyplot as plt

    # Balkendiagramm
    plt.figure()
    plt.bar(demo["kategorie"], demo["y"])
    plt.title("Balken"); plt.xlabel("Kategorie"); plt.ylabel("Wert")
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
    df_fluntern = df_heizgradtage[df_heizgradtage["Standort"] == "Fluntern"]
    avg_fluntern = df_fluntern.groupby("Monat")["Heizgradtag"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(
        avg_fluntern["Monat"],
        avg_fluntern["Heizgradtag"],
    )
    plt.title("Durchschnittliche Heizgradtage pro Monat (Fluntern)")
    plt.xlabel("Monat (1–12)")
    plt.ylabel("Durchschnittliche Heizgradtage")
    plt.show()
    # Monat mit dem höchsten Mittelwert
    monat_hoechster_fluntern = avg_fluntern.loc[avg_fluntern["Heizgradtag"].idxmax(), "Monat"]
    print(f"Fluntern: Monat mit höchstem Mittelwert = {monat_hoechster_fluntern}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Heubeeribüel
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    df_heubeeri = df_heizgradtage[df_heizgradtage["Standort"] == "Heubeeribüel"]
    avg_heubeeri = df_heubeeri.groupby("Monat")["Heizgradtag"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(
        avg_heubeeri["Monat"],
        avg_heubeeri["Heizgradtag"],
    )
    plt.title("Durchschnittliche Heizgradtage pro Monat (Heubeeribüel)")
    plt.xlabel("Monat (1–12)")
    plt.ylabel("Durchschnittliche Heizgradtage")
    plt.show()
    # Monat mit dem höchsten Mittelwert
    monat_hoechster_heubeeri = avg_heubeeri.loc[avg_heubeeri["Heizgradtag"].idxmax(), "Monat"]
    print(f"Heubeeribüel: Monat mit höchstem Mittelwert = {monat_hoechster_heubeeri}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rosengartenstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    df_rosengarten = df_heizgradtage[df_heizgradtage["Standort"] == "Rosengartenstrasse"]
    avg_rosengarten = df_rosengarten.groupby("Monat")["Heizgradtag"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(
        avg_rosengarten["Monat"],
        avg_rosengarten["Heizgradtag"],
    )
    plt.title("Durchschnittliche Heizgradtage pro Monat (Rosengartenstrasse)")
    plt.xlabel("Monat (1–12)")
    plt.ylabel("Durchschnittliche Heizgradtage")
    plt.show()
    # Monat mit dem höchsten Mittelwert
    monat_hoechster_rosengarten = avg_rosengarten.loc[avg_rosengarten["Heizgradtag"].idxmax(), "Monat"]
    print(f"Rosengartenstrasse: Monat mit höchstem Mittelwert = {monat_hoechster_rosengarten}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Schimmelstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    df_schimmelstr = df_heizgradtage[df_heizgradtage["Standort"] == "Schimmelstrasse"]
    avg_schimmelstr = df_schimmelstr.groupby("Monat")["Heizgradtag"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(
        avg_schimmelstr["Monat"],
        avg_schimmelstr["Heizgradtag"],
    )
    plt.title("Durchschnittliche Heizgradtage pro Monat (Schimmelstrasse)")
    plt.xlabel("Monat (1–12)")
    plt.ylabel("Durchschnittliche Heizgradtage")
    plt.show()
    # Monat mit dem höchsten Mittelwert
    monat_hoechster_schimmelstr = avg_schimmelstr.loc[avg_schimmelstr["Heizgradtag"].idxmax(), "Monat"]
    print(f"Schimmelstrasse: Monat mit höchstem Mittelwert = {monat_hoechster_schimmelstr}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Stampfenbachstrasse
    """)
    return


@app.cell
def _(df_heizgradtage, plt):
    df_stampfenbach = df_heizgradtage[df_heizgradtage["Standort"] == "Stampfenbachstrasse"]
    avg_stampfenbach = df_stampfenbach.groupby("Monat")["Heizgradtag"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(
        avg_stampfenbach["Monat"],
        avg_stampfenbach["Heizgradtag"],
    )
    plt.title("Durchschnittliche Heizgradtage pro Monat (Stampfenbachstrasse)")
    plt.xlabel("Monat (1–12)")
    plt.ylabel("Durchschnittliche Heizgradtage")
    plt.show()
    # Monat mit dem höchsten Mittelwert
    monat_hoechster_stampfenbach = avg_stampfenbach.loc[avg_stampfenbach["Heizgradtag"].idxmax(), "Monat"]
    print(f"Stampfenbachstrasse: Monat mit höchstem Mittelwert = {monat_hoechster_stampfenbach}")
    return


if __name__ == "__main__":
    app.run()
