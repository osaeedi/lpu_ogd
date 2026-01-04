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
    df_fluntern = df_heizgradtage[df_heizgradtage["Standort"] == "Fluntern"]
    # Bestimmen Sie den Monat mit dem höchsten Mittelwert
    avg_fluntern = df_fluntern.groupby("Monat")["Heizgradtag"].mean().reset_index()
    monat_fluntern = avg_fluntern.loc[avg_fluntern["Heizgradtag"].idxmax(), "Monat"]
    # Filtern Sie auf diesen Monat
    df_fluntern_monat = df_fluntern[df_fluntern["Monat"] == monat_fluntern]
    # Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.plot(
        df_fluntern_monat["Jahr"],
        df_fluntern_monat["Heizgradtag"],
        marker="o",
    )
    plt.title(f"Heizgradtage im Monat {monat_fluntern} über die Jahre (Fluntern)")
    plt.xlabel("Jahr")
    plt.ylabel("Heizgradtage")
    plt.grid(True)
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
    df_heubeeri = df_heizgradtage[df_heizgradtage["Standort"] == "Heubeeribüel"]
    # Bestimmen Sie den Monat mit dem höchsten Mittelwert
    avg_heubeeri = df_heubeeri.groupby("Monat")["Heizgradtag"].mean().reset_index()
    monat_heubeeri = avg_heubeeri.loc[avg_heubeeri["Heizgradtag"].idxmax(), "Monat"]
    # Filtern Sie auf diesen Monat
    df_heubeeri_monat = df_heubeeri[df_heubeeri["Monat"] == monat_heubeeri]
    # Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.plot(
        df_heubeeri_monat["Jahr"],
        df_heubeeri_monat["Heizgradtag"],
        marker="o",
    )
    plt.title(f"Heizgradtage im Monat {monat_heubeeri} über die Jahre (Heubeeribüel)")
    plt.xlabel("Jahr")
    plt.ylabel("Heizgradtage")
    plt.grid(True)
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
    df_rosengarten = df_heizgradtage[df_heizgradtage["Standort"] == "Rosengartenstrasse"]
    # Bestimmen Sie den Monat mit dem höchsten Mittelwert
    avg_rosengarten = df_rosengarten.groupby("Monat")["Heizgradtag"].mean().reset_index()
    monat_rosengarten = avg_rosengarten.loc[avg_rosengarten["Heizgradtag"].idxmax(), "Monat"]
    # Filtern Sie auf diesen Monat
    df_rosengarten_monat = df_rosengarten[df_rosengarten["Monat"] == monat_rosengarten]
    # Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.plot(
        df_rosengarten_monat["Jahr"],
        df_rosengarten_monat["Heizgradtag"],
        marker="o",
    )
    plt.title(f"Heizgradtage im Monat {monat_rosengarten} über die Jahre (Rosengartenstrasse)")
    plt.xlabel("Jahr")
    plt.ylabel("Heizgradtage")
    plt.grid(True)
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
    df_schimmelstr = df_heizgradtage[df_heizgradtage["Standort"] == "Schimmelstrasse"]
    # Bestimmen Sie den Monat mit dem höchsten Mittelwert
    avg_schimmelstr = df_schimmelstr.groupby("Monat")["Heizgradtag"].mean().reset_index()
    monat_schimmelstr = avg_schimmelstr.loc[avg_schimmelstr["Heizgradtag"].idxmax(), "Monat"]
    # Filtern Sie auf diesen Monat
    df_schimmelstr_monat = df_schimmelstr[df_schimmelstr["Monat"] == monat_schimmelstr]
    # Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.plot(
        df_schimmelstr_monat["Jahr"],
        df_schimmelstr_monat["Heizgradtag"],
        marker="o",
    )
    plt.title(f"Heizgradtage im Monat {monat_schimmelstr} über die Jahre (Schimmelstrasse)")
    plt.xlabel("Jahr")
    plt.ylabel("Heizgradtage")
    plt.grid(True)
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
    df_stampfenbach = df_heizgradtage[df_heizgradtage["Standort"] == "Stampfenbachstrasse"]
    # Bestimmen Sie den Monat mit dem höchsten Mittelwert
    avg_stampfenbach = df_stampfenbach.groupby("Monat")["Heizgradtag"].mean().reset_index()
    monat_stampfenbach = avg_stampfenbach.loc[avg_stampfenbach["Heizgradtag"].idxmax(), "Monat"]
    # Filtern Sie auf diesen Monat
    df_stampfenbach_monat = df_stampfenbach[df_stampfenbach["Monat"] == monat_stampfenbach]
    # Erstellen Sie das Liniendiagramm
    plt.figure(figsize=(12, 6))
    plt.plot(
        df_stampfenbach_monat["Jahr"],
        df_stampfenbach_monat["Heizgradtag"],
        marker="o",
    )
    plt.title(f"Heizgradtage im Monat {monat_stampfenbach} über die Jahre (Stampfenbachstrasse)")
    plt.xlabel("Jahr")
    plt.ylabel("Heizgradtage")
    plt.grid(True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antworten zu den Zusatzfragen

    **Haben sich die Heizgradtage über die Jahre geändert?**

    Bei Standorten wie Fluntern zeigt sich über die Jahre ein leichter **Rückgang** der Heizgradtage, was auf wärmere Winter hindeuten könnte (möglicherweise ein Zeichen des Klimawandels).

    **Gibt es genug Messungen, um eine aussagekräftige Analyse durchzuführen?**

    Nein, die Datenbasis ist nicht ausreichend für eine aussagekräftige Analyse. Klima kann man erst nach 30 Jahren Messungen bewerten und in den meisten Standort existieren weniger Messungen.
    """)
    return


if __name__ == "__main__":
    app.run()
