import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from buttons import ButtonRole, StyledButton

class MainWindow(qtw.QWidget):

    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('TMP')

        btn1 = StyledButton('Test', ButtonRole.DANGER)
        ml = qtw.QVBoxLayout(self)
        ml.addWidget(btn1)

        self.show()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()

    sys.exit(app.exec())
