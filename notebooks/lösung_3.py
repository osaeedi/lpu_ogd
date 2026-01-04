# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
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
    # Was ist marimo?

    **marimo** ist ein reaktives Python-Notebook:
    Änderungen in einer Zelle lösen automatisch die Neuausführung aller von ihr abhängigen Zellen aus.

    **Abhängigkeitsstruktur:** Die Abhängigkeiten zwischen Zellen werden durch einen gerichteten Graphen modelliert:

    - Jede Zelle entspricht einem **Knoten** des Graphen.
    - Eine gerichtete **Kante** von Zelle *A* nach Zelle *B* bedeutet, dass *B* eine in *A* definierte Variable verwendet.

    **Regeln für gültige Abhängigkeiten:** Damit diese Struktur eine eindeutige und wohldefinierte automatische Ausführung erlaubt, erzwingt marimo die folgenden Regeln:

    1. **Single Assignment:**
       Jede Variable (einschliesslich `import`-Variablen) darf nur in genau einer Zelle definiert werden.
    2. **Azyklizität:**
       Der Abhängigkeitsgraph darf keine Zyklen enthalten; zirkuläre Abhängigkeiten zwischen Zellen sind nicht erlaubt.

    Unter diesen Regeln ist der Abhängigkeitsgraph ein **gerichteter azyklischer Graph (DAG)** und besitzt damit eine eindeutige topologische Ausführungsreihenfolge.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Die beiden Regeln für gültige Abhängigkeiten untersuchen wir in der folgenden Aufgabe praktisch.

    Wir beobachten zuerst das reaktive Verhalten und provozieren danach gezielt die beiden Regelverletzungen.

    Klicken Sie oben rechts **Fork and run**.
    Erstellen Sie ein Account, falls Sie noch keines haben.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Beobachten: reaktive Neuausführung

       Führen Sie das ganze Skript aus (Play-Taste unten rechts).
       Ändern Sie danach den Wert von `x` in der Zelle `declare_x`.

       1. Welche Zellen werden danach automatisch erneut ausgeführt?
       2. Welche Ausgaben ändern sich, und warum?
    """)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Lösung: Reaktive Neuausführung

    **Antworten:**

    1. **Welche Zellen werden automatisch erneut ausgeführt?**
       - Wenn `x` in der Zelle `declare_x` geändert wird, werden automatisch alle Zellen erneut ausgeführt, die von `x` abhängen. Das sind:
         - `declare_y` (verwendet `x`)
         - `declare_z` (verwendet `y`, welches von `x` abhängt)
       - Die Zelle `declare_x` selbst wird natürlich auch ausgeführt.

    2. **Welche Ausgaben ändern sich, und warum?**
       - Die Ausgabe von `declare_y` ändert sich, weil `y = 2 * x` direkt von `x` abhängt.
       - Die Ausgabe von `declare_z` ändert sich, weil `z = y + 1` indirekt von `x` abhängt (über `y`).
       - Dies geschieht automatisch durch die reaktive Ausführung: marimo erkennt die Abhängigkeiten im DAG und führt alle betroffenen Zellen in der richtigen Reihenfolge neu aus.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Regel 1 brechen: Single Assignment

       Ändern Sie das Notebook so, dass die Variable `x` in zwei verschiedenen Zellen zugewiesen wird
       (z. B. einmal in `declare_x` und zusätzlich in `declare_y`).

       1. Lesen Sie die Fehlermeldung: Was sagt sie aus?
       2. Begründen Sie in eigenen Worten, warum marimo diese Regel erzwingt.
          Beziehen Sie sich dabei auf den Abhängigkeitsgraphen der Zellen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Lösung: Regel 1 brechen - Single Assignment

    **Beispiel für Regelverletzung:**

    Wenn man versucht, `x` in zwei Zellen zu definieren (z.B. in `declare_x` und zusätzlich in `declare_y`), würde marimo einen Fehler melden.

    **Antworten:**

    1. **Was sagt die Fehlermeldung aus?**
       - marimo meldet einen Fehler, dass die Variable `x` mehrfach definiert wurde (multiple definitions).
       - Die Fehlermeldung zeigt an, in welchen Zellen die Variable definiert wurde.

    2. **Warum erzwingt marimo diese Regel?**
       - **Eindeutigkeit im Abhängigkeitsgraphen:** Wenn eine Variable in mehreren Zellen definiert werden könnte, wäre unklar, welche Definition verwendet werden soll. Der Abhängigkeitsgraph würde mehrdeutig werden.
       - **Deterministische Ausführung:** Um eine eindeutige Reihenfolge der Auführbarkeit zu ermöglichen, muss jede Variable genau eine Quelle haben. Andernfalls wäre nicht klar, welche Zelle zuerst ausgeführt werden muss.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Regel 2 brechen: Zirkuläre Abhängigkeit

       Ändern Sie das Notebook so, dass ein Kreisbezug entsteht:
       Zelle A hängt von Zelle B ab und Zelle B hängt von Zelle A ab (direkt oder indirekt).

       1. Lesen Sie die Fehlermeldung: Was sagt sie aus?
       2. Begründen Sie in eigenen Worten, warum zirkuläre Abhängigkeiten in einem reaktiven Notebook nicht funktionieren.
          Argumentieren Sie mithilfe des gerichteten Abhängigkeitsgraphen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Lösung: Regel 2 brechen - Zirkuläre Abhängigkeit

    **Beispiel für Regelverletzung:**

    Wenn man versucht, eine zirkuläre Abhängigkeit zu erstellen (z.B. Zelle A hängt von B ab und B hängt von A ab), würde marimo einen Fehler melden.

    **Antworten:**

    1. **Was sagt die Fehlermeldung aus?**
       - marimo meldet einen Fehler, dass ein Zyklus im Abhängigkeitsgraphen erkannt wurde.
       - Die Fehlermeldung zeigt den Pfad des Zyklus an (z.B. A → B → A).

    2. **Warum funktionieren zirkuläre Abhängigkeiten nicht?**
       - **Keine Reihenfolge möglich:** Ein gerichteter Graph mit Zyklen kann nicht sortiert werden. Es gibt keine eindeutige Ausführungsreihenfolge.
       - **Unendliche Rekursion:** Wenn Zelle A von B abhängt und B von A, dann würde eine Änderung in A B aktualisieren, was wiederum A aktualisieren würde, was B aktualisieren würde, usw. - eine Endlosschleife.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Reihenfolge der Zellen

       Verändern Sie die Reihenfolge der Zellen, ohne die Logik zu ändern.

       1. Ändert sich das Ergebnis?
       2. Was sagt das über den Unterschied zwischen *Reihenfolge* und *Abhängigkeit* aus?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Lösung: Reihenfolge der Zellen

    **Antworten:**

    1. **Ändert sich das Ergebnis?**
       - **Nein**, das Ergebnis ändert sich nicht, unabhängig von der Reihenfolge der Zellen im Editor.
       - marimo bestimmt die Ausführungsreihenfolge automatisch basierend auf dem Abhängigkeitsgraphen (topologische Sortierung).

    2. **Unterschied zwischen Reihenfolge und Abhängigkeit:**
       - **Reihenfolge (im Editor):** Die visuelle Anordnung der Zellen im Notebook-Editor ist beliebig und hat keinen Einfluss auf die Ausführung.
       - **Abhängigkeit (im Graphen):** Die logische Abhängigkeit zwischen Zellen (wer verwendet welche Variable) bestimmt die tatsächliche Ausführungsreihenfolge.
       - **Beispiel:** Auch wenn `declare_z` im Editor vor `declare_x` steht, wird `declare_x` zuerst ausgeführt, weil `declare_z` von `y` abhängt, welches wiederum von `x` abhängt.
       - Dies ist ein wichtiger Unterschied zu traditionellen Notebooks (wie Jupyter), wo die Reihenfolge der Zellen im Editor die Ausführungsreihenfolge bestimmt.
    """)
    return


if __name__ == "__main__":
    app.run()
