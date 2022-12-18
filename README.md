# <GUI_Projekt>

- Einfacher Hypothekarrechner, der berechnet, ob eine Hypothek bei gegebenem Kaufpreis, Einkommen und Eigenmittel möglich ist
- Rückmeldung an User, ob Hypothek tragbar ist oder nicht und ob Belehnung i.O. ist
- Anzeige von Hypothek, Tragbarkeit, Belehnung und Amortisation
- Bewusste Einschränkung der Funktionalitäten: Keine Berücksichtigung des Alters (Auswirkungen auf Amortisation), Art der Eigenmittel und keine Abdeckung für Ablösung von Hypotheken

## Start aus der Konsole
python GUI_Projekt.py

## Test von Calculationobjekt auf pythoninteraktiven Konsole
1. Schritt: 
python -i GUI_Projekt.py

2. Schritt
calc = Calculation(1000000, 250000, 120000)
calc.berechne_hypothek()

3. Schritt
exit()

## Um mit dem Projekt zu starten, muss das Haupt Python File geöffnet werden:
``
    GUI_Projekt.py
``
## Damit die notwendigen Packages vorhanden sind, muss der folgende Befehl ausgeführt werden:
``
    pip install -r requirements.txt
``
## Um berechnen zu können, ob eine Hypothek für den Kreditnehmer tragbar ist, müssen Kaufpreis, Eigenmittel und Einkommen abgefüllt werden. Mittels Pushbutton werden die notwendigen Berechnungen aufgeführt und falls notwendig Fehlermeldungen an den User zurück gemeldet.

![Draft für GUI](https://github.com/lorenarodriguezf/python_project_template/blob/183cf270881d0856eb039c3af4f7efba93423db3/WhatsApp%20Image%202022-11-25%20at%2016.07.16.jpeg)
![Draft für Berechnungen](https://github.com/lorenarodriguezf/python_project_template/blob/183cf270881d0856eb039c3af4f7efba93423db3/WhatsApp%20Image%202022-11-25%20at%2016.07.17.jpeg)

