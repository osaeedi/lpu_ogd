# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
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
    # Was ist marimo?

    **marimo** ist ein reaktives Python-Notebook: Wenn Sie eine Zelle ausführen, werden abhängige Zellen automatisch neu ausgeführt (oder als veraltet markiert). So bleiben Code und Ausgaben konsistent und viele Fehler werden verhindert, bevor sie entstehen.
    Abhängigkeiten zwischen Zellen müssen zwei wichtige Regeln einhalten:
      1. **Eine Variable (und somit auch imports) darf nur in genau *einer* Zelle zugewiesen werden.**
      2. **Zirkuläre Abhängigkeiten sind nicht möglich.**
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Reaktivität in 3 Zellen

    1. Führen Sie das ganze Skript aus, indem Sie unten rechts auf die **Play-Taste** klicken. Ändern Sie nun `x` in der ersten Zelle. Was beobachten Sie?

    2. Ändern Sie eine der drei Zellen (`declare_x`, `declare_y` oder `declare_z`), so dass die **erste** Bedingung nicht mehr erfüllt ist. Lesen Sie die Fehlermeldung. Warum gilt die **erste** Bedingung? Begründen Sie in Ihren eigenen Worten.

    3. Ändern Sie eine der drei Zellen, so dass die **zweite** Bedingung nicht mehr erfüllt ist. Lesen Sie die Fehlermeldung. Warum gilt die **zweite** Bedingung? Begründen Sie in Ihren eigenen Worten.
    """
    )
    return


@app.cell
def declare_x():
    x = 10
    x
    return (x,)


@app.cell
def declare_y(x):
    y = 2 * x
    print(f"y = 2 * x = {y}")
    return (y,)


@app.cell
def declare_z(y):
    z = y + 1
    print(f"z = y + 1 = {z}")
    return


if __name__ == "__main__":
    app.run()
