import PyQt5
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
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