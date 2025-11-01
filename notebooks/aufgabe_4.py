# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas==2.3.3",
#     "requests==2.32.5",
# ]
# ///

import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Programmierschnittstellen (APIs)

    Eine **API** (Application Programming Interface) ist eine definierte Schnittstelle zwischen zwei Programmen oder Diensten, über die strukturierte Daten oder Funktionen automatisiert ausgetauscht werden können.

    Man kann sich APIs wie *Lego-Bausteine* vorstellen: Jeder Dienst oder jede Anwendung ist ein Baustein mit bestimmten Fähigkeiten.  
    Durch klar definierte Verbindungsstellen – die API – können diese Bausteine miteinander kombiniert werden.  
    So entstehen neue, komplexe Anwendungen, ohne dass jedes Teil von Grund auf neu entwickelt werden muss.

    APIs sind zentral für viele datengetriebene Prozesse: Sie machen Daten maschinenlesbar zugänglich und ermöglichen skalierbare Analysen in Echtzeit.

    Eine besonders verbreitete Form offener Datenschnittstellen ist die **REST-API** (Representational State Transfer).  
    Sie basiert auf einfachen HTTP-Anfragen – wie `GET`, `POST`, `PUT` oder `DELETE` – und liefert meist Daten im `JSON`- oder `XML`-Format zurück.  
    So kann z. B. eine `GET`-Anfrage an eine bestimmte URL einen aktuellen Datensatz abrufen, etwa zu Wetter, Verkehr oder Finanzen.

    In **Python** wird für den Zugriff auf REST-APIs typischerweise die Bibliothek `requests` verwendet.  
    Sie erlaubt das einfache Senden von HTTP-Anfragen und das Weiterverarbeiten der erhaltenen Daten – oft in wenigen Zeilen Code.
    """
    )
    return


@app.cell
def _():
    import io
    import requests
    import pandas as pd
    return pd, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Daten per REST-API (Heizgradtage und akkumulierte Temperaturdifferenzen)

    1. Suchen Sie auf [opendata.swiss](https://opendata.swiss) den Datensatz **„Heizgradtage und akkumulierte Temperaturdifferenzen für verschiedene Standorte in der Stadt Zürich“**. Öffnen Sie **Preview** → kopieren Sie die **Download-URL** von `UMW103OD1031.csv`.

    2. Fügen Sie diese URL in der Zelle `get_heizgradtage` bei `url` ein.

    3. Implementieren Sie `csv_export_url_to_dataframe(url: str) → pd.DataFrame`, die eine CSV-Datei über eine URL lädt und als DataFrame zurückgibt.
    """
    )
    return


@app.cell
def get_heizgradtage(pd, requests):
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
