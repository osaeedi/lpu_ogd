# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "pandas==2.3.3",
#     "requests==2.32.5",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    return io, mo, pd, requests


@app.cell
def _(io, pd, requests):
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
def _(csv_export_url_to_dataframe):
    url = "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100112/exports/csv?lang=de&timezone=Europe%2FZurich&use_labels=true&delimiter=%3B"
    df = csv_export_url_to_dataframe(url)
    df
    return (df,)


@app.cell
def _(df):
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fehlende Werte & Ausreisser (Geschwindigkeitsmonitoring)

    Übernehmen Sie die implementierte IQR-Methode (`find_outliers_iqr`) aus Aufgabe 8 und nutzen Sie diese auf den Datensatz **Geschwindigkeitsmonitoring: Kennzahlen pro Mess-Standort**.

    1. Welche Spalten können auf fehlende Werte und Ausreisser untersucht werden? Erklären Sie, welche Spalten für eine solche Analyse geeignet sind und warum.

    2. Ist es eine gute Idee, fehlende Werte auszusortieren? Untersuchen Sie, ob es sinnvoll ist, fehlende Werte zu entfernen.

    3. IQR-Methode mit Standardparametern: Erklären Sie, warum die IQR-Methode mit $k=1.5$ und den Quantilen $0.25$ und $0.75$ fehlerlose Werte aussortiert.

    4. Anpassung der IQR-Methode: Erklären Sie, wie Sie die IQR-Methode anpassen können, um wirklich nur problematische Werte auszusortieren.
    """)
    return


@app.cell
def _(pd):
    # IQR-Methode aus Aufgabe 8 übernommen
    def find_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
        s = series.astype("float64")  # robust gegen Int/Objekt
        q1 = s.quantile(0.25, interpolation="linear")
        q3 = s.quantile(0.75, interpolation="linear")
        iqr = q3 - q1
        lower = q1 - k * iqr
        upper = q3 + k * iqr
        # Erstelle die Maske für Ausreisser. 
        # Alle Werte, die ausserhalb der Grenzen liegen.
        mask = (s < lower) | (s > upper)
        # NaN sollen nicht automatisch als Ausreisser zählen
        mask = mask.fillna(False)
        return mask
    return (find_outliers_iqr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. Welche Spalten können auf fehlende Werte und Ausreisser untersucht werden?

    Für die Untersuchung auf fehlende Werte und Ausreisser sind **numerische Spalten** geeignet, die messbare Geschwindigkeitskennzahlen enthalten.

    **Geeignete Spalten im Geschwindigkeitsmonitoring-Datensatz:**

    - `V50 Richtung 1` / `V50 Richtung 2` (Median-Geschwindigkeit)
    - `V85 Richtung 1` / `V85 Richtung 2` (85%-Perzentil-Geschwindigkeit)
    - `Fahrzeuge Richtung 1` / `Fahrzeuge Richtung 2` (Anzahl gemessener Fahrzeuge)
    - `Übertretungsquote Richtung 1` / `Übertretungsquote Richtung 2` (Anteil der Geschwindigkeitsübertretungen)
    - `Zone` (Zonennummer)

    **Nicht geeignet** sind:
    - Kategorische Spalten: `Messung-ID`, `Messbeginn`, `Messende`, `Strasse`, `Hausnummer`, `Ort`, `Richtung 1`, `Richtung 2`, `Koordinaten`, `Einzelmessungen`, `geo_point_2d`
    - Identifikatoren: `Messbeginn Jahr` (obwohl numerisch, ist es ein kategorischer Wert)

    Diese numerischen Spalten enthalten messbare Werte, die statistisch analysiert werden können und bei denen Ausreisser und fehlende Werte sinnvoll interpretiert werden können.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Ist es eine gute Idee, fehlende Werte auszusortieren?

    **Nein, es ist in diesem Fall keine gute Idee, fehlende Werte einfach auszusortieren.**

    **Begründung:**

    Im Geschwindigkeitsmonitoring-Datensatz gibt es **zwei Fahrtrichtungen** (`Richtung 1` und `Richtung 2`). Nicht alle Mess-Standorte haben Messungen für beide Richtungen. Wenn eine Richtung nicht existiert, erscheinen die entsprechenden Werte als fehlend (`NaN`).

    **Beobachtungen:**
    - Es gibt Messungen, die nur `Richtung 1` haben (keine `Richtung 2`)
    - Es gibt Messungen, die nur `Richtung 2` haben (keine `Richtung 1`)
    - Es gibt Messungen mit beiden Richtungen
    - Die Spalten `Fahrzeuge Richtung 2`, `V50 Richtung 2`, `V85 Richtung 2` und `Übertretungsquote Richtung 2` haben deutlich mehr fehlende Werte als die entsprechenden Spalten für Richtung 1

    **Probleme beim Aussortieren:**
    - **Informationsverlust:** Wenn wir Zeilen mit fehlenden Werten entfernen, verlieren wir Informationen über Standorte, die nur eine Richtung haben.
    - **Verzerrte Analyse:** Die Datenstruktur wird unvollständig, da nicht alle Standorte gleich behandelt werden.
    - **Semantisch korrekt:** Fehlende Werte für eine nicht-existierende Richtung sind **keine Fehler**, sondern eine korrekte Darstellung der Realität (z.B. Einbahnstrassen haben nur eine Richtung).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. IQR-Methode mit Standardparametern: Warum sortiert sie fehlerlose Werte aus?

    Die IQR-Methode mit den Standardparametern $k=1.5$ und den Quantilen $0.25$ und $0.75$ ist eine **statistische Methode**, die auf der Verteilung der Daten basiert, nicht auf der tatsächlichen Korrektheit der Werte.

    **Warum werden fehlerlose Werte aussortiert?**

    1. **Statistische Definition:** Die IQR-Methode identifiziert Werte, die **statistisch ungewöhnlich** sind, d.h. weit vom Median entfernt liegen. Dies bedeutet nicht automatisch, dass diese Werte **falsch** sind.

    2. **Normale Variation:** In realen Daten gibt es oft **legitime extreme Werte**:
       - Sehr schnelle Fahrzeuge (z.B. Rettungsfahrzeuge, Sportwagen)
       - Besondere Verkehrssituationen (z.B. Stau, freie Fahrt)
       - Unterschiedliche Standorte mit unterschiedlichen Geschwindigkeitsprofilen

    **Fazit:** Die IQR-Methode mit Standardparametern ist ein **Screening-Tool**, das ungewöhnliche Werte identifiziert, aber nicht zwischen "fehlerhaften" und "legitimen Extremwerten" unterscheidet.
    """)
    return


@app.cell
def _(df, find_outliers_iqr, pd):
    # Vergleich: Standard k=1.5 vs. strengere Parameter für V85 Richtung 1
    col_to_check = 'V85 Richtung 1'

    # Standard
    outliers_k15 = find_outliers_iqr(df[col_to_check], k=1.5)
    num_k15 = outliers_k15.sum()

    # Strenger
    outliers_k25 = find_outliers_iqr(df[col_to_check], k=2.5)
    num_k25 = outliers_k25.sum()

    # Sehr streng
    outliers_k30 = find_outliers_iqr(df[col_to_check], k=3.0)
    num_k30 = outliers_k30.sum()

    compare = pd.DataFrame({
        'k-Wert': [1.5, 2.5, 3.0],
        'Anzahl Ausreisser': [num_k15, num_k25, num_k30],
    })
    compare
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. Anpassung der IQR-Methode: Wie kann man wirklich problematische Werte aussortieren?

    Um die IQR-Methode so anzupassen, dass sie **wirklich problematische Werte** identifiziert, gibt es mehrere Strategien:

    **1. Anpassung des $k$-Wertes:**
    - **Erhöhen** von $k$ (z.B. $k=2.5$ oder $k=3.0$) macht die Methode **weniger empfindlich**
    - Nur sehr extreme Werte werden als Ausreisser identifiziert
    - Reduziert die Anzahl der "falsch-positiven" Ausreisser

    **2. Alternative Quantile:**
    - Statt $0.25$ und $0.75$ können **andere Quantile** verwendet werden (z.B. $0.1$ und $0.9$)
    - Dies macht die Methode robuster gegen Extremwerte in den Quantilen selbst

    Die beste Anpassung hängt vom **spezifischen Anwendungsfall** und den **verfügbaren Metadaten** ab.
    """)
    return


if __name__ == "__main__":
    app.run()
