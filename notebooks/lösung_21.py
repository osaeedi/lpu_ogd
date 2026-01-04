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
    df_fluntern = df_heizgradtage[df_heizgradtage["Standort"] == "Fluntern"]
    plt.figure(figsize=(12, 6))
    plt.scatter(
        df_fluntern["Heizgradtag"],
        df_fluntern["akkumulierteTemperaturdifferenz"],
    )
    plt.title("Heizgradtag vs. akkumulierte Temperaturdifferenz (Fluntern)")
    plt.xlabel("Heizgradtag")
    plt.ylabel("akkumulierte Temperaturdifferenz")
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
    plt.figure(figsize=(12, 6))
    plt.scatter(
        df_heubeeri["Heizgradtag"],
        df_heubeeri["akkumulierteTemperaturdifferenz"],
    )
    plt.title("Heizgradtag vs. akkumulierte Temperaturdifferenz (Heubeeribüel)")
    plt.xlabel("Heizgradtag")
    plt.ylabel("akkumulierte Temperaturdifferenz")
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
    plt.figure(figsize=(12, 6))
    plt.scatter(
        df_rosengarten["Heizgradtag"],
        df_rosengarten["akkumulierteTemperaturdifferenz"],
    )
    plt.title("Heizgradtag vs. akkumulierte Temperaturdifferenz (Rosengartenstrasse)")
    plt.xlabel("Heizgradtag")
    plt.ylabel("akkumulierte Temperaturdifferenz")
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
    plt.figure(figsize=(12, 6))
    plt.scatter(
        df_schimmelstr["Heizgradtag"],
        df_schimmelstr["akkumulierteTemperaturdifferenz"],
    )
    plt.title("Heizgradtag vs. akkumulierte Temperaturdifferenz (Schimmelstrasse)")
    plt.xlabel("Heizgradtag")
    plt.ylabel("akkumulierte Temperaturdifferenz")
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
    plt.figure(figsize=(12, 6))
    plt.scatter(
        df_stampfenbach["Heizgradtag"],
        df_stampfenbach["akkumulierteTemperaturdifferenz"],
    )
    plt.title("Heizgradtag vs. akkumulierte Temperaturdifferenz (Stampfenbachstrasse)")
    plt.xlabel("Heizgradtag")
    plt.ylabel("akkumulierte Temperaturdifferenz")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antwort zur Zusatzfrage

    **Unterschied zwischen Heizgradtag und akkumulierteTemperaturdifferenz:**

    - **Heizgradtag (HGT)**: Wird berechnet als `20 - T` wenn die Temperatur T < 12 °C ist, sonst 0. Dies ist ein Mass für den Heizbedarf, basierend auf der Annahme, dass bei Temperaturen unter 12 °C geheizt werden muss. Die Formel `20 - T` gibt an, wie viele Grad unter der Heizgrenze von 20 °C die Temperatur liegt.

    - **akkumulierteTemperaturdifferenz (ATD)**: Wird berechnet als `max(0, 12 - T)`. Dies ist die Differenz zwischen der Referenztemperatur von 12 °C und der tatsächlichen Temperatur, wenn diese unter 12 °C liegt. Die ATD akkumuliert die "Kälte" unterhalb der Referenztemperatur.

    Der Hauptunterschied liegt in der Referenztemperatur: Der Heizgradtag verwendet 20 °C als Referenz (typische Raumtemperatur), während die akkumulierte Temperaturdifferenz 12 °C als Referenz verwendet (Schwellenwert für Heizbedarf). Beide Werte sind positiv korreliert, da sie beide auf niedrige Temperaturen reagieren, aber der Heizgradtag ist in der Regel höher als die ATD.
    """)
    return


if __name__ == "__main__":
    app.run()
