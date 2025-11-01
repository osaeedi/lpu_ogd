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

__generated_with = "0.17.6"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Aufgabe 12 — Daten visualisieren

    In dieser Aufgabe arbeiten Sie mit Heizgradtagen der Stadt Zürich und erstellen drei Diagrammtypen:
    **Linie**, **Balken** und **Streudiagramm**. Hier eine kleine Intro zu matplotlib:
    ```python
    import matplotlib.pyplot as plt

    # kleines Demo-Dataset für die drei Diagrammtypen
    demo = pd.DataFrame({
        "x": np.arange(1, 7),
        "y": np.array([3, 5, 2, 6, 4, 7]),
        "kategorie": ["A", "B", "C", "D", "E", "F"],
    })
    demo

    # 1) Liniendiagramm
    plt.figure()
    plt.plot(demo["x"], demo["y"], marker="o")
    plt.title("Linie"); plt.xlabel("x"); plt.ylabel("y"); plt.grid(True)
    plt.show()

    # 2) Balkendiagramm
    plt.figure()
    plt.bar(demo["kategorie"], demo["y"])
    plt.title("Balken"); plt.xlabel("Kategorie"); plt.ylabel("Wert")
    plt.show()

    # 3) Streudiagramm
    plt.figure()
    plt.scatter(demo["x"], demo["y"])
    plt.title("Streuung"); plt.xlabel("x"); plt.ylabel("y"); plt.grid(True)
    plt.show()
    ```
    """)
    return


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
    ## Daten visualisieren (Heizgradtage, Standort **Fluntern**)

    1. Filtern Sie auf `Standort == "Fluntern"`. Wandeln Sie `Jahr_Monat` in `datetime` (`YYYY-MM`) um, sortieren Sie nach Zeit.

    2. Untersuchen Sie mithilfe eines Streudiagramms, ob `Heizgradtag` und `akkumulierteTemperaturdifferenz` zusammenhängen.

    3. Bilden Sie den Monatsdurchschnitt von `Heizgradtag` (Gruppe: `Monat`). Balkendiagramm der 12 Monatsmittel. Nennen Sie den Monat mit dem **höchsten** Mittelwert.

    4. Wählen Sie den Monat aus 3 (mit dem höchsten Mittelwert), filtern Sie auf diesen Monat und visualisieren Sie `Heizgradtag` über die Jahre (Liniendiagramm mit Markern). Beurteilen Sie knapp, ob über die Jahre eher **Rückgang**, **Anstieg** oder **kein klarer Trend** erkennbar ist.
    """)
    return


@app.cell
def _(df_heizgradtage):
    df_heizgradtage_fluntern = df_heizgradtage[df_heizgradtage["Standort"] == "Fluntern"]
    df_heizgradtage_fluntern
    return (df_heizgradtage_fluntern,)


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(df_heizgradtage_fluntern, plt):
    plt.figure(figsize=(12, 6))
    plt.scatter(
        df_heizgradtage_fluntern["Heizgradtag"],
        df_heizgradtage_fluntern["akkumulierteTemperaturdifferenz"],
    )
    plt.title("Heizgradtag vs. akkumulierte Temperaturdifferenz (Fluntern)")
    plt.xlabel("Heizgradtag")
    plt.ylabel("akkumulierte Temperaturdifferenz")
    plt.show()
    return


@app.cell
def _(df_heizgradtage_fluntern, plt):
    avg_heizgradtage_per_month = df_heizgradtage_fluntern.groupby("Monat")["Heizgradtag"].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(
        avg_heizgradtage_per_month["Monat"],
        avg_heizgradtage_per_month["Heizgradtag"],
    )
    plt.title("Durchschnittliche Heizgradtage pro Monat (Fluntern)")
    plt.xlabel("Monat (1–12)")
    plt.ylabel("Durchschnittliche Heizgradtage")
    plt.show()
    return


@app.cell
def _(df_heizgradtage_fluntern, plt):
    df_heizgradtage_fluntern_monat = df_heizgradtage_fluntern[df_heizgradtage_fluntern["Monat"] == 1]
    plt.figure(figsize=(12, 6))
    plt.plot(
        df_heizgradtage_fluntern_monat["Jahr"],
        df_heizgradtage_fluntern_monat["Heizgradtag"],
        marker="o",
    )
    plt.title(f"Heizgradtage im Monat .... über die Jahre (Fluntern)")
    plt.xlabel("Jahr")
    plt.ylabel("Heizgradtage")
    plt.grid(True)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
