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

__generated_with = "0.19.1"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    import io
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt
    return io, pd, plt, requests


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
def _(csv_export_url_to_dataframe):
    # URL zum Datensatz (Standort 44, Zyklus 6 - wie in Kontrollaufgabe 3)
    url_smiley = "https://data.bs.ch/api/explore/v2.1/catalog/datasets/100268/exports/csv?lang=de&refine=zyklus%3A%226%22&refine=id_standort%3A%2244%22&facet=facet(name%3D%22id_standort%22%2C%20disjunctive%3Dtrue)&timezone=Europe%2FZurich&use_labels=true&delimiter=%3B"
    df_smiley = csv_export_url_to_dataframe(url_smiley)
    df_smiley
    return (df_smiley,)


@app.cell
def create_boxplot(df_smiley, plt):
    """
    Erstellt Boxplots gruppiert nach Phasen (Vormessung, Betrieb, Nachmessung)
    um zu zeigen, ob das Nudging funktioniert hat.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Gruppiere Daten nach Phasen
    phases = ["Vormessung", "Betrieb", "Nachmessung"]
    data_by_phase = [df_smiley[df_smiley["Phase"] == phase]["Einfahrtstempo"].dropna() for phase in phases]

    # Erstelle Boxplot
    bp = ax.boxplot(data_by_phase, labels=phases, patch_artist=True, showmeans=True)

    # Farben für die Boxen
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel('Einfahrtstempo [km/h]', fontsize=12)
    ax.set_xlabel('Phase', fontsize=12)
    ax.set_title('Geschwindigkeitsverteilung nach Phasen\n(Nudging-Effekt Analyse)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')

    # Berechne und zeige Mittelwerte
    means = [data.mean() for data in data_by_phase]
    for i, (phase, mean) in enumerate(zip(phases, means)):
        ax.text(i+1, mean, f'μ={mean:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
