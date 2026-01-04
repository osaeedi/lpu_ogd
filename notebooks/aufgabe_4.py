# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
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
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Programmierschnittstellen (APIs)

    Eine **API** (Application Programming Interface) ist eine klar definierte Schnittstelle, über die Programme oder Dienste automatisiert Daten oder Funktionen austauschen können.

    APIs ermöglichen den standardisierten Zugriff auf Daten, ohne dass deren interne Struktur oder Speicherung bekannt sein muss.

    Man kann sich APIs wie Steckverbindungen oder Bausteine vorstellen:
    Ein Dienst stellt Daten oder Funktionen bereit, ein anderes Programm greift gezielt darauf zu.
    Entscheidend ist dabei nicht, wie der Dienst intern implementiert ist, sondern **wie** man ihn ansprechen darf und **was** man zurückbekommt.

    APIs sind zentral für datengetriebene Anwendungen: Sie machen Daten maschinenlesbar, aktuell und skalierbar zugänglich.

    Eine besonders verbreitete Form von APIs sind sogenannte **REST-APIs** (Representational State Transfer).

    REST-APIs basieren auf dem HTTP-Protokoll, das auch beim Aufrufen von Webseiten verwendet wird.

    Typische HTTP-Anfragen sind:
    * `GET` – Daten abrufen,
    * `POST` – neue Daten senden,
    * `PUT` – bestehende Daten ändern,
    * `DELETE` – Daten löschen.

    Für den reinen Datenabruf ist insbesondere `GET` relevant.

    In **Python** wird für den Zugriff auf REST-APIs typischerweise die Bibliothek `requests` verwendet.
    Sie erlaubt es, HTTP-Anfragen zu senden und die Antwort weiterzuverarbeiten – oft in nur wenigen Zeilen Code.
    """)
    return


@app.cell
def _():
    import io
    import requests
    import pandas as pd
    return io, pd, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## requests.get()

    Die Funktion [`requests.get`](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request) stammt aus dem Python-Modul `requests` und dient dazu **HTTP-GET-Anfragen** zu senden – also Daten von einem Webserver abzurufen.

    **Grundprinzip:**
    ```python
    import requests

    response = requests.get("https://example.com/data.csv")
    ```

    * `requests.get(url)` schickt eine GET-Anfrage an die angegebene URL.
    * Die Rückgabe (`response`) ist ein **Response-Objekt**, das viele nützliche Attribute enthält:

    | Attribut             | Beschreibung                              | Beispiel                           |
    | -------------------- | ----------------------------------------- | ---------------------------------- |
    | `status_code`        | HTTP-Statuscode (z. B. `200`, `404`)      | `response.status_code == 200`      |
    | `text`               | Antwortinhalt als String (z. B. CSV-Text) | `response.text[:200]`              |
    | `content`            | Antwortinhalt als Bytes                   | `response.content`                 |
    | `headers`            | HTTP-Header der Antwort                   | `response.headers["Content-Type"]` |
    | `raise_for_status()` | Löst Fehler aus, falls kein 2xx-Status    | `response.raise_for_status()`      |

    **Beispiel mit Fehlerprüfung:**

    ```python
    resp = requests.get(url)
    resp.raise_for_status()  # wirft bei HTTP-Fehlern eine Exception
    csv_text = resp.text
    ```

    **Hinweis:**
    Bei öffentlichen REST-APIs wie auf *opendata.swiss* genügt meist ein einfacher GET-Request ohne Authentifizierung.
    Manche APIs erfordern jedoch Parameter (`params={...}`), Header oder Tokens – das Prinzip bleibt dasselbe.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Daten per REST-API (Heizgradtage und akkumulierte Temperaturdifferenzen)

    1. Öffnen Sie [opendata.swiss](https://opendata.swiss) und suchen Sie den Datensatz
       **„Heizgradtage und akkumulierte Temperaturdifferenzen für verschiedene Standorte in der Stadt Zürich“**.
       Öffnen Sie die **Preview** des Datensatzes.

    2. Kopieren Sie die **Download-URL** der CSV-Datei `UMW103OD1031.csv`.

    3. Fügen Sie diese URL in der Zelle `get_heizgradtage` in die Variable `url` ein.

    4. Implementieren Sie die Funktion
       `csv_export_url_to_dataframe(url: str)`, die:
       - eine beliebige CSV-Datei über die angegebene URL lädt (sofern die REST-API dies zulässt),
       - und die Daten als DataFrame zurückgibt.

    5. Überprüfen Sie das Ergebnis, indem Sie sich die ersten Zeilen des DataFrames anzeigen lassen.
    """)
    return


@app.cell
def get_heizgradtage(io, pd, requests):
    # TODO: Hier die direkte Download-URL zu `UMW103OD1031.csv` einfügen:
    url = ""

    df = None
    if url:
        resp = requests.get(url)
        resp.raise_for_status()
        df = pd.read_csv(io.BytesIO(resp.content), sep=None, engine="python", encoding="utf-8")

    df
    return (url,)


@app.cell
def csv_export_url_to_dataframe(pd):
    def csv_export_url_to_dataframe(url: str) -> pd.DataFrame:
        """
        Lädt eine CSV von einer direkten HTTP(s)-URL und gibt ein DataFrame zurück.

        Args:
            url: Direkte Download-URL zur CSV.

        Returns:
            pd.DataFrame
        """
        # TODO: Implementieren Sie die Funktion hier
        print(f"Getting data from {url}")
        # Hier können wir df nochmals zuweisen, da die Variable nur innerhalb der Funktion existiert
        df = None
        return df
    return (csv_export_url_to_dataframe,)


@app.cell
def use_function(csv_export_url_to_dataframe, url):
    csv_export_url_to_dataframe(url)
    return


if __name__ == "__main__":
    app.run()
