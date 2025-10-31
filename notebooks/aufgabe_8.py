# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas==2.3.3",
#     "requests==2.32.5",
# ]
# ///

import marimo

__generated_with = "0.17.5"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    return io, mo, pd, requests


@app.cell
def csv_export_url_to_dataframe(io, pd, requests):
    def csv_export_url_to_dataframe(url: str) -> pd.DataFrame:
        """
        Lädt eine CSV von einer direkten HTTP(s)-URL und gibt ein DataFrame zurück.

        Args:
            url: Direkte Download-URL zur CSV.

        Returns:
            pd.DataFrame
        """
        resp = requests.get(url)
        resp.raise_for_status()
        df = pd.read_csv(io.BytesIO(resp.content), sep=None, engine="python", encoding="utf-8")
        return df
    return (csv_export_url_to_dataframe,)


@app.cell
def get_heizgradtage(csv_export_url_to_dataframe):
    url = "https://data.stadt-zuerich.ch/dataset/umw_heizgradtage_standort_jahr_monat_od1031/download/UMW103OD1031.csv"
    df = csv_export_url_to_dataframe(url)
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fehlende Werte & Ausreisser (Heizgradtage)

    Fehlende Werte werden in CSVs oft als leere Felder dargestellt. Beim Einlesen in ein DataFrame werden diese automatisch als `NaN` (Not a Number) erkannt.
    Weitere mögliche Darstellungen für fehlende Werte sind z.B. `-9999`, `n/a`, `null`, etc.
    Wenn sie im CSV nicht leer sind, müssen diese beim Einlesen explizit angegeben werden (z.B. mit dem Parameter `na_values` in `pd.read_csv`).
    Wenn in den Metadaten nichts steht, gehen wir davon aus, dass fehlende Werte als leere Felder dargestellt sind.

    In pandas können fehlende Werte mit `pd.isna()` oder `series.isna()` erkannt werden.

    Ausreisser sind Werte die weit ausserhalb des normalen Bereichs liegen.
    Es gibt verschiedene Methoden, um etwas als Ausreisser zu definieren.
    Eine gängige Methode ist die **Interquartilsabstand-Methode (IQR-Methode)**.

    **IQR-Methode (robust, standard):**
    - \(Q1 := 25\%\)-Quantil, \(Q3 := 75\%\)-Quantil, \(IQR := Q3 - Q1\)
    - Untere Grenze: \(Q1 - k \cdot IQR\)
    - Obere Grenze: \(Q3 + k \cdot IQR\)
    - $k$ ist der Faktor zur Anpassung der Empfindlichkeit (üblich: $k=1.5$)
    - Werte ausserhalb sind Ausreisser.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fehlende Werte & Ausreisser (Heizgradtage)

    1. Zeige alle Zeilen mit fehlenden Werten in der Spalte `Heizgradtag` im DataFrame `df_missing_heizgradtage` an.
    2. Zeige alle Zeilen mit fehlenden Werten in der Spalte `akkumulierteTemperaturdifferenz` im DataFrame `df_missing_temperaturdiff` an.
    3. Sind die beiden DataFrames `df_missing_heizgradtage` und `df_missing_temperaturdiff` identisch?
    4. Implementiere die Funktion `find_outliers_iqr`, die Ausreisser in einer `pd.Series` nach der IQR-Methode (wie oben beschrieben) findet.

    ```python
    def find_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    ```
    """)
    return


@app.cell
def get_missing_heizgradtage(df):
    # TODO: Ergänze den Code so, dass alle Zeilen mit fehlenden Werten in "Heizgradtag" im DataFrame `df_missing_heizgradtage` gespeichert werden.
    df_missing_heizgradtage = df
    df_missing_heizgradtage
    return (df_missing_heizgradtage,)


@app.cell
def get_missing_temperaturdifferenzen(df):
    # TODO: Ergänze den Code so, dass alle Zeilen mit fehlenden Werten in "akkumulierteTemperaturdifferenz" im DataFrame `df_missing_temperaturdiff` gespeichert werden.
    df_missing_temperaturdiff = df
    df_missing_temperaturdiff
    return (df_missing_temperaturdiff,)


@app.cell
def outlier_function_placeholder(pd):
    def find_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
        s = series.astype("float64")  # robust gegen Int/Objekt
        q1 = s.quantile(0.25, interpolation="linear")
        q3 = s.quantile(0.75, interpolation="linear")
        # TODO: Definiere die IQR-Methode korrekt
        iqr = 20
        lower = -500
        upper = 500
        # Erstelle die Maske für Ausreisser. 
        # Alle Werte, die ausserhalb der Grenzen liegen.
        mask = (s < lower) | (s > upper)
        # NaN sollen nicht automatisch als Ausreisser zählen
        mask = mask.fillna(False)
        return mask
    return (find_outliers_iqr,)


@app.cell
def get_outlier_heizgradtage(df, find_outliers_iqr):
    # TODO: Wende deine Funktion auf "Heizgradtag" an und speichere nur die Ausreisser-Zeilen.
    mask = find_outliers_iqr(df["Heizgradtag"], k=1.5)
    df_outlier_heizgradtage = df[mask]
    df_outlier_heizgradtage
    return (df_outlier_heizgradtage,)


@app.cell
def _(df, find_outliers_iqr):
    # TODO: Wende deine Funktion auf "akkumulierteTemperaturdifferenz" an und speichere nur die Ausreisser-Zeilen.
    mask_temparaturdiff = find_outliers_iqr(df["akkumulierteTemperaturdifferenz"], k=1.5)
    df_outlier_temparaturdiff = df[mask_temparaturdiff]
    df_outlier_temparaturdiff
    return (df_outlier_temparaturdiff,)


@app.cell
def _(
    df,
    df_missing_heizgradtage,
    df_missing_temperaturdiff,
    df_outlier_heizgradtage,
    df_outlier_temparaturdiff,
    pd,
):
    summary = pd.Series({
        "Rows total": len(df),
        "NaN Heizgradtag": len(df_missing_heizgradtage),
        "NaN Temperaturdiff": len(df_missing_temperaturdiff),
        "Outlier Heizgradtag (k=1.5)": len(df_outlier_heizgradtage),
        "Outlier Temperaturdiff (k=1.5)": len(df_outlier_temparaturdiff),
    })
    summary.to_frame("count")
    return


if __name__ == "__main__":
    app.run()
