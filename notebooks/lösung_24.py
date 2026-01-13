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
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(df_heizgradtage):
    # Filtern auf Standort "Fluntern"
    df_fluntern = df_heizgradtage[df_heizgradtage["Standort"] == "Fluntern"]
    # Bestimmen Sie den Monat mit dem höchsten Mittelwert (aus Aufgabe 23)
    avg_fluntern = df_fluntern.groupby("Monat")["Heizgradtag"].mean().reset_index()
    monat_fluntern = avg_fluntern.loc[avg_fluntern["Heizgradtag"].idxmax(), "Monat"]
    return df_fluntern, monat_fluntern


@app.cell
def _(df_fluntern, monat_fluntern):
    # Filtern Sie auf diesen Monat
    df_fluntern_monat = df_fluntern[df_fluntern["Monat"] == monat_fluntern].copy()
    print(f"Monat mit höchstem Mittelwert in Fluntern: {monat_fluntern}")
    # Erstellen Sie eine 30-Jahres-Gruppe (Klimaperiode) aus dem Jahr
    # Verwenden Sie ganzzahlige Division: periode_start = (Jahr // 30) * 30
    df_fluntern_monat["periode_start"] = (df_fluntern_monat["Jahr"] // 30) * 30
    # Formatieren Sie dann als "start--start+29"
    df_fluntern_monat["periode_label"] = (
        df_fluntern_monat["periode_start"].astype(str) 
        + "--" 
        + (df_fluntern_monat["periode_start"] + 29).astype(str)
    )
    # Sortieren nach periode_start für bessere Darstellung
    df_fluntern_monat = df_fluntern_monat.sort_values("periode_start")
    return (df_fluntern_monat,)


@app.cell
def _(df_fluntern_monat, plt):
    # Erstellen Sie einen Boxplot der Heizgradtag-Werte pro 30-Jahres-Gruppe
    # Gruppieren nach periode_label
    perioden = df_fluntern_monat["periode_label"].unique()
    perioden = sorted(perioden)  # Sortieren für chronologische Reihenfolge

    # Daten für jede Periode sammeln
    data_per_periode = [
        df_fluntern_monat[df_fluntern_monat["periode_label"] == periode]["Heizgradtag"].values
        for periode in perioden
    ]

    plt.figure(figsize=(12, 6))
    bp = plt.boxplot(
        data_per_periode,
        labels=perioden,
        patch_artist=True,
    )
    # Farben für bessere Visualisierung
    colors = plt.cm.Set3(range(len(perioden)))
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    plt.title(f"Heizgradtag-Verteilung nach 30-Jahres-Gruppen (Fluntern, Monat {df_fluntern_monat['Monat'].iloc[0]})")
    plt.xlabel("30-Jahres-Gruppe (Klimaperiode)")
    plt.ylabel("Heizgradtag")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Median:**

    Der Median zeigt tendenziell einen **Rückgang** über die Zeit. In früheren 30-Jahres-Perioden liegt der Median höher als in späteren Perioden (ausser 1950 -1979, in denen er wieder steigt), was auf wärmere Winter in jüngerer Zeit hindeutet.

    **Streuung (IQR):**

    Die Streuung (IQR) **variiert**, aber es ist kein Trend über die Zeit erkennbar. Der 75%-Quantil sinkt deutlich.

    **Ausreisser:**

    Die Anzahl der Ausreisser variiert zwischen den Perioden, aber es gibt **keinen eindeutigen Trend** zu mehr oder weniger Ausreissern. Einige Perioden zeigen mehr extreme Werte als andere, was natürliche Klimavariabilität widerspiegeln kann.

    **Zusammenfassung:**

    Der Boxplot zeigt einen **Rückgang des Medians** über die Zeit, was auf wärmere Winter hindeutet. Die Streuung bleibt relativ konstant, und die Ausreisser zeigen keine klare zeitliche Tendenz.
    """)
    return


if __name__ == "__main__":
    app.run()
