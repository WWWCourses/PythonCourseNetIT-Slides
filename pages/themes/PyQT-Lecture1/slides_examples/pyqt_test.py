import sys

from PyQt6.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt6 App Works')
window.setGeometry(100, 100, 500, 500)

window.show()
sys.exit(app.exec())