import sys
import PyQt5
import locale
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QValidator, QIntValidator
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QFormLayout, QLineEdit, QMessageBox

class Calculation:
    """Berechnung der Hypothek, Amortisation, Tragbarkeit und Belehnung"""
    
    def __init__(self, kaufpreis, einkommen, eigenmittel):
        """Initialisiert Calculation mit notwendigen Inputparameter"""
        self.kaufpreis = kaufpreis
        self.einkommen = einkommen
        self.eigenmittel = eigenmittel

    def berechne_hypothek(self):
        """Betrag wird als Zahl zurückgegeben"""
        return self.kaufpreis - self.eigenmittel
        
    def berechne_erstehypothek(self):
        return self.kaufpreis * 0.666

    def berechne_amortisation(self):
        hypothek = self.berechne_hypothek()
        hypothek1 = self.berechne_erstehypothek()
        return hypothek - hypothek1

    def berechne_amortisationsbetragprojahr(self):
        return self.berechne_amortisation() / 15

    def berechne_tragbarkeit(self):
        hypothek = self.berechne_hypothek()
        hypothek1 = self.berechne_erstehypothek()
        if hypothek1 >= hypothek:
            return (hypothek * 0.0475 + self.kaufpreis * 0.01) / self.einkommen
        else: 
            amortisationsbetrag = self.berechne_amortisation()
            amortisationsbetragprojahr = self.berechne_amortisationsbetragprojahr()
            return ((hypothek1 * 0.0475 + amortisationsbetrag * 0.0525 + self.kaufpreis *0.01 + amortisationsbetragprojahr) / self.einkommen) * 100

    def berechne_belehnung(self):
        return ((self.kaufpreis - self.eigenmittel) / self.kaufpreis) *100

    
class Formatierung:
    """Formatiert Werte in Währungsdarstellung oder Prozentdarstellung"""

    def __init__(self):
        locale.setlocale(locale.LC_ALL, "de_CH")

    def betrag(self, zahl):
        """Formatiert eine Zahl in Währungstext"""
        return locale.format_string("CHF %d", zahl, grouping = True)

    def prozent(self, zahl):
        """Formatiert eine Zahl in Prozenttext"""
        return f"{zahl:0.2f}%"


class Fehlermeldung:
    """Zeigt verschiedene Fehlermeldungstypen an."""

    def __init__(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Warnung")  
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 

    def fehlermeldung_anzeigen(self, fehlermeldung):
        self.msg.setText(fehlermeldung)
        self.msg.exec_()


class Hyporechner(QWidget):
    """
        Layout minimaler Hypothekarrechner
        Inspiration von: https://pythonspot.com/pyqt5-buttons/
    """

    def __init__(self):
        super().__init__()

        # Eingabefelder
        self.kaufpreis = QLineEdit()
        self.einkommen = QLineEdit()
        self.eigenmittel = QLineEdit()
        # Ausgabefelder
        self.hypothek = QLabel()
        self.tragbarkeit = QLabel()
        self.amortisation = QLabel()
        self.belehnung = QLabel()
        self.button = QPushButton ("Berechnen")

        self.kaufpreis.setValidator (QIntValidator (1, 10000000, self.kaufpreis))
        self.einkommen.setValidator(QIntValidator (1, 20000000, self.einkommen))
        self.eigenmittel.setValidator (QIntValidator (1, 10000000, self.eigenmittel))
        #button.clicked.connect(function) --> Notwendig, um Funktion mit "Push the button" zu verbinden
        self.button.clicked.connect(self.pushaction)
        
        layout = QFormLayout()
        layout.addRow("Kaufpreis:", self.kaufpreis)
        layout.addRow("Jährliches Einkommen:", self.einkommen)
        layout.addRow("Eigenmittel:", self.eigenmittel)
        layout.addWidget(self.button)
        layout.addRow(self.hypothek)
        layout.addRow(self.tragbarkeit)
        layout.addRow(self.amortisation)
        layout.addRow(self.belehnung)

        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.blue)

        self.setWindowTitle("Hypthekenrechner Gruppe Mix")
        self.setGeometry(600, 600, 480, 180)
        self.setLayout(layout)
        self.setPalette(palette)
        self.show()

    def pushaction(self):
        fehlerObj = Fehlermeldung()

        if self.kaufpreis.text() == "" or self.einkommen.text() == "" or self.eigenmittel.text() == "":
            fehlerObj.fehlermeldung_anzeigen("Es sind nicht alle notwendigen Felder ausgefüllt.")
            return

        # Eingabefelder auslesen
        kaufpreis = int(self.kaufpreis.text())
        einkommen = int(self.eigenmittel.text())
        eigenmittel = int(self.eigenmittel.text())

        #Objekte für die Verarbeitung instanzieren
        calculationObj = Calculation(kaufpreis, einkommen, eigenmittel)
        formatierungObj = Formatierung()

        hypobetrag = calculationObj.berechne_hypothek()
        self.hypothek.setText("Hypothek = " + formatierungObj.betrag(hypobetrag))

        #Berechnung Belehnung
        belehnung = calculationObj.berechne_belehnung()
        self.belehnung.setStyleSheet("color : green")
        if belehnung > 80:
            fehlerObj.fehlermeldung_anzeigen("Die Belehnung ist über 80%.")
            self.belehnung.setStyleSheet("color : red")
        self.belehnung.setText("Belehnung = " + formatierungObj.prozent(belehnung))

        #Berechne Trabgarkeit
        tragbarkeit = calculationObj.berechne_tragbarkeit()
        self.tragbarkeit.setStyleSheet("color : green")
        if tragbarkeit > 33:
            fehlerObj.fehlermeldung_anzeigen("Die Tragbarkeit ist nicht gegeben.")
            self.tragbarkeit.setStyleSheet("color : red")
        self.tragbarkeit.setText("Tragbarkeit = " + formatierungObj.prozent(tragbarkeit))
        
        #Berechnung Amortisation
        amortisation_pro_jahr = calculationObj.berechne_amortisationsbetragprojahr()
        self.amortisation.setText("Amortisation pro Jahr = " + formatierungObj.betrag(amortisation_pro_jahr))

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    hypowindow = Hyporechner()
    sys.exit(app.exec())

if __name__ == "__main__":
   main()