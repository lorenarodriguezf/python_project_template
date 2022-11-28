import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QValidator, QIntValidator
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QFormLayout, QLineEdit
app = QApplication([])
app.setStyle('Windows')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
window = QWidget()
window.setWindowTitle("Hypthekenrechner Gruppe Mix")
window.setGeometry(600, 600, 480, 180)
layout = QFormLayout()
kaufpreis = QLineEdit()
#on changed oder ähnliches für QlineEdit checken
kaufpreis.setValidator (QIntValidator (1, 10000000, kaufpreis))
einkommen = QLineEdit()
einkommen.setValidator(QIntValidator (1, 20000000, einkommen))
eigenmittel = QLineEdit()
eigenmittel.setValidator (QIntValidator (1, 10000000, eigenmittel))
layout.addRow("Kaufpreis:", kaufpreis)
layout.addRow("Jährliches Einkommen:", einkommen)
layout.addRow("Eigenmittel:", eigenmittel)
#Signals & Slots -> Pushbutton (In der Funktion definieren - Berechnung und Validierung / on button click verbinden mit Funktion)
button = QPushButton ("Berechnen")
#button.clicked.connect(function) --> Notwendig, um Funktion mit "Push the button" zu verbinden

#def pushbutton ():
    #if kaufpreis.text() == "" or einkommen.text() == "" or eigenmittel.text() == "":
       # print ("Es sind nicht alle notwendigen Felder ausgefüllt")

def pushbutton ():
    zkaufpreis = kaufpreis.text()
    zeinkommen = einkommen.text()
    zeigenmittel = eigenmittel.text()
    # neue Variable "z" definieren, da ansonsten ein Wert definiert wird, der noch nicht vorhanden ist --> kaufpreis.text greift den definierten Wert von oben auf, der neu in eine Zahl umgewandelt werden soll.
    zkaufpreis = int(zkaufpreis)
    zeinkommen = int(zeinkommen)
    zeigenmittel = int(zeigenmittel)
    #Berechnungen 
    Hypothek = zkaufpreis - zeigenmittel
    Belehnung = ((zkaufpreis-zeigenmittel) / zkaufpreis) *100
    Hypothek1 = zkaufpreis * 0.666
    #Tragbarkeitsberechnung
    Tragbarkeit = 0
    Amortisationsbetragprojahr = 0
    if Hypothek1 >= Hypothek:
        Tragbarkeit = (Hypothek * 0.0475 + zkaufpreis * 0.01)/zeinkommen 
        print ("Es ist keine Amortisation notwendig")
    else: 
        Amortisationsbetrag = Hypothek - Hypothek1
        Amortisationsbetragprojahr = Amortisationsbetrag / 15
        Tragbarkeit = (Hypothek1 * 0.0475 + Amortisationsbetrag * 0.0525 + zkaufpreis *0.01 + Amortisationsbetragprojahr) /zeinkommen 
    Tragbarkeit = Tragbarkeit*100
        #belehnungs_wert = ......
 

    # Resultate in UI einfügen
    #belehnung.setText(.....)
    

#def amortisation (betragprojahr):
    #if Amortisationsbetrag > 0:
       # return (Amortisationsbetrag / 15)
    #else:
        #return ("Es ist keine Amortisation notwendig")
    print(Hypothek)
    print(Belehnung, "%")
    print(Amortisationsbetragprojahr)
    print(Tragbarkeit, "%")

#wenn man Zeichenkette mit% möchte dann f string

button.clicked.connect (pushbutton)
Hypothek = QLabel("Hypothek")
layout.addWidget(button)
window.setLayout(layout)
window.setLayout(layout)
window.show()
app.exec()