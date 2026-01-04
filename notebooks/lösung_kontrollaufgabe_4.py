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

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt
    return io, mo, pd, plt, requests


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
    return (df_heizgradtage,)


@app.cell
def get_energieverbrauch(csv_export_url_to_dataframe):
    url_energie = "https://data.stadt-zuerich.ch/dataset/ugz_endenergiebilanz/download/ugz_endenergiebilanz.csv"
    df_energieverbrauch = csv_export_url_to_dataframe(url_energie)
    df_energieverbrauch
    return (df_energieverbrauch,)


@app.cell
def transform_and_merge(df_energieverbrauch, df_heizgradtage, pd):
    heiz_cols = ["Holz_UW_BG_SK", "Fernwaerme", "Erdgas", "Heizoel_EL"]
    df_heiz = (
        df_energieverbrauch[["Jahr", *heiz_cols]]
        .assign(Heizenergieverbrauch=lambda d: d[heiz_cols].sum(axis=1, numeric_only=True))
        [["Jahr", "Heizenergieverbrauch"]]
    )
    df_hgt_jahr = df_heizgradtage.groupby("Jahr", as_index=False)["Heizgradtag"].sum()
    df_merged = pd.merge(df_heiz, df_hgt_jahr, on="Jahr", how="left")
    df_merged
    return (df_merged,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Visualisieren Sie den Zusammenhang zwischen Heizgradtagen und Heizenergieverbrauch mittels Scatterplot. Entspricht das Ihrer Erwartung? Begründen Sie. Welche Informationen fehlen für eine Beurteilung?
    """)
    return


@app.cell
def plot(df_merged, plt):
    plt.figure(figsize=(8, 6))
    plt.scatter(df_merged["Heizgradtag"], df_merged["Heizenergieverbrauch"], alpha=0.7)
    plt.title("Heizgradtage vs. Heizenergieverbrauch")
    plt.xlabel("Heizgradtage [Tage]")
    plt.ylabel("Heizenergieverbrauch [GWh]")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Hinweis: Die Bevölkerungsentwicklung verändert den Vergleich über die Jahre. "
        "Frühere Jahre hatten mehr Heizgradtage, aber eine kleinere Bevölkerung.
    """)
    return


if __name__ == "__main__":
    app.run()
