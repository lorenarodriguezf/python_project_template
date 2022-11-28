import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
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
layout.addRow("Kaufpreis:", QLineEdit())
layout.addRow("Jährliches Einkommen:", QLineEdit())
layout.addRow("Eigenmittel:", QLineEdit())
#Signals & Slots -> Pushbutton (In der Funktion definieren - Berechnung und Validierung)
layout.addWidget(QPushButton('Berechnung'))
window.setLayout(layout)
window.setLayout(layout)
window.show()
app.exec()