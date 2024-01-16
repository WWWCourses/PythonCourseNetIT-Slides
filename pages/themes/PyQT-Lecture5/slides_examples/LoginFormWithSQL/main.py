import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from loginForm import LoginForm




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    w = qtw.QWidget()

    qr = w.frameGeometry()
    cp = qtw.QApplication.primaryScreen().geometry().center()
    print(cp)
    qr.moveCenter(cp)
    w.move(qr.topLeft())

    w.show()


    sys.exit(app.exec())
