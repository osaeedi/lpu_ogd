# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.7",
#     "pandas==2.3.3",
#     "requests==2.32.5",
#     "openpyxl==3.1.5",
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
    return io, mo, pd, requests


@app.cell
def xlsx_export_url_to_dataframe(io, pd, requests):
    def xlsx_export_url_to_dataframe(url: str) -> pd.DataFrame:
        """
        Lädt eine Excel-Datei von einer direkten HTTP(s)-URL und gibt ein DataFrame zurück.

        Args:
            url: Direkte Download-URL zur Excel-Datei (.xlsx).

        Returns:
            pd.DataFrame
        """
        pass
    return (xlsx_export_url_to_dataframe,)


if __name__ == "__main__":
    app.run()
