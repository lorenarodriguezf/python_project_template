import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
app.setStyle('Windows')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
window = QWidget()
window.setWindowTitle("Hypthekenrechner Gruppe Mix")
window.setGeometry(400, 400, 280, 80)
layout = QVBoxLayout()
layout.addWidget(QPushButton('Kaufpreis'))
layout.addWidget(QPushButton('Jährliches Bruttoeinkommen'))
layout.addWidget(QPushButton('Eigenmittel'))
window.setLayout(layout)
window.show()
app.exec()