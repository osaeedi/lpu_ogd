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

__generated_with = "0.19.0"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt
    return io, pd, requests


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
        df = pd.read_csv(io.BytesIO(resp.content), sep=None, engine="python", encoding="utf-8")
        return df
    return (csv_export_url_to_dataframe,)


@app.cell
def load_smiley_data(csv_export_url_to_dataframe):
    # URL zum Datensatz (kann nach Standort/Zyklus gefiltert werden)
    # Beispiel-URL - bitte durch die gefilterte URL vom Portal ersetzen
    url_smiley = "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100268/exports/csv?lang=de&refine=zyklus%3A%226%22&refine=id_standort%3A%2244%22&facet=facet(name%3D%22id_standort%22%2C%20disjunctive%3Dtrue)&timezone=Europe%2FZurich&use_labels=true&delimiter=%3B"
    df_smiley = csv_export_url_to_dataframe(url_smiley)
    df_smiley
    return (df_smiley,)


@app.cell
def _(pd):
    # IQR-Methode aus Aufgabe 8 übernommen
    def find_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
        """
        Identifiziert Ausreisser in einer Series nach der IQR-Methode.

        Args:
            series: Numerische Series
            k: Multiplikator für IQR (Standard: 1.5)

        Returns:
            Boolean Series (True = Ausreisser)
        """
        s = series.astype("float64")  # robust gegen Int/Objekt
        q1 = s.quantile(0.25, interpolation="linear")
        q3 = s.quantile(0.75, interpolation="linear")
        iqr = q3 - q1
        lower = q1 - k * iqr
        upper = q3 + k * iqr
        # Erstelle die Maske für Ausreisser
        mask = (s < lower) | (s > upper)
        # NaN sollen nicht automatisch als Ausreisser zählen
        mask = mask.fillna(False)
        return mask
    return (find_outliers_iqr,)


@app.cell
def analyze_missing_values(df_smiley, pd):
    # Analyse fehlender Werte (wie in Aufgabe 8)
    missing_values = df_smiley.isnull().sum()
    missing_pct = (missing_values / len(df_smiley) * 100).round(2)

    df_missing_analysis = pd.DataFrame({
        'Spalte': missing_values.index,
        'Anzahl fehlend': missing_values.values,
        'Prozent fehlend': missing_pct.values
    })
    df_missing_analysis = df_missing_analysis[df_missing_analysis['Anzahl fehlend'] > 0].sort_values('Anzahl fehlend', ascending=False)
    df_missing_analysis
    return


@app.cell
def analyze_outliers(df_smiley, find_outliers_iqr, pd):
    # Analyse von Ausreißern mit verschiedenen k-Werten (wie in Aufgabe 9)
    for speed_col in ["Einfahrtstempo", "Ausfahrtstempo"]:
        # Vergleich verschiedener k-Werte
        outliers_k15 = find_outliers_iqr(df_smiley[speed_col], k=1.5)
        outliers_k25 = find_outliers_iqr(df_smiley[speed_col], k=2.5)
        outliers_k30 = find_outliers_iqr(df_smiley[speed_col], k=3.0)

        comparison = pd.DataFrame({
            'k-Wert': [1.5, 2.5, 3.0],
            'Anzahl Ausreisser': [
                outliers_k15.sum(),
                outliers_k25.sum(),
                outliers_k30.sum()
            ],
            'Prozent': [
                (outliers_k15.sum() / len(df_smiley) * 100).round(2),
                (outliers_k25.sum() / len(df_smiley) * 100).round(2),
                (outliers_k30.sum() / len(df_smiley) * 100).round(2)
            ]
        })
        comparison

        # Zeige die Ausreisser mit k=1.5
        df_outliers = df_smiley[outliers_k15].copy()
        print(f"\nAusreisser mit k=1.5: {len(df_outliers)} Zeilen für Spalte {speed_col}")

        # Zeige die Ausreisser mit k=2.5
        df_outliers = df_smiley[outliers_k25].copy()
        print(f"\nAusreisser mit k=2.5: {len(df_outliers)} Zeilen für Spalte {speed_col}")

        # Zeige die Ausreisser mit k=3
        df_outliers = df_smiley[outliers_k30].copy()
        print(f"\nAusreisser mit k=3.0: {len(df_outliers)} Zeilen für Spalte {speed_col}")
    return


@app.cell
def improve_data_quality(df_smiley):
    """
    Datenqualitätsverbesserungen basierend auf Vorwissen aus Aufgabe 8 und 9:
    Unrealistische Geschwindigkeiten entfernen (physikalische Grenzen)
    """
    df_improved = df_smiley.copy()

    print("=== Datenqualitätsverbesserung ===\n")
    print(f"Anfang: {len(df_improved)} Zeilen\n")

    # Physikalisch unrealistische Geschwindigkeiten entfernen
    # (nicht mit IQR, sondern mit absoluten Grenzen)
    for cols in ["Einfahrtstempo", "Ausfahrtstempo"]:
        before = len(df_improved)
        # Annahme: Geschwindigkeiten zwischen 0 und 200 km/h sind realistisch
        # (auch für Autobahnen in der Schweiz)
        df_improved = df_improved[
            (df_improved[cols] >= 0) & (df_improved[cols] <= 200)
        ]
        after = len(df_improved)
        print(f"Entfernt {before - after} Zeilen mit unrealistischen Geschwindigkeiten (< 0 oder > 200 km/h)\n")

    print(f"Finale Anzahl Zeilen: {len(df_improved)}")
    print(f"Entfernt insgesamt: {len(df_smiley) - len(df_improved)} Zeilen ({((len(df_smiley) - len(df_improved))/len(df_smiley)*100):.2f}%)")

    df_improved
    return


if __name__ == "__main__":
    app.run()
