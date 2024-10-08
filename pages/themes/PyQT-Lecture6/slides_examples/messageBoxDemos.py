import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        # create widgets:
        btnShowCommonMessageBox = qtw.QPushButton('ShowCommonMessageBox')
        btnShowQuestionMessageBox = qtw.QPushButton('ShowQuestionMessageBox')
        btnShowInformationMessageBox = qtw.QPushButton('ShowInformationMessageBox')
        btnShowWarningMessageBox = qtw.QPushButton('ShowWarningMessageBox')
        btnShowCriticalMessageBox = qtw.QPushButton('ShowCriticalMessageBox')

        # main layout
        main_layout = qtw.QGridLayout(self)
        main_layout.addWidget(btnShowCommonMessageBox, 0, 0, 1, 2)
        main_layout.addWidget(btnShowQuestionMessageBox, 1, 0)
        main_layout.addWidget(btnShowInformationMessageBox, 1, 1)
        main_layout.addWidget(btnShowWarningMessageBox, 2, 0)
        main_layout.addWidget(btnShowCriticalMessageBox, 2, 1)

        btnShowCommonMessageBox.clicked.connect(self.showCommonMessageBox)
        btnShowQuestionMessageBox.clicked.connect(self.showQuestionMessageBox)
        btnShowInformationMessageBox.clicked.connect(self.showInformationMessageBox)
        btnShowWarningMessageBox.clicked.connect(self.showWarningMessageBox)
        btnShowCriticalMessageBox.clicked.connect(self.showCriticalMessageBox)

        self.setWindowTitle('Message Box Demos')
        self.show()

    # Create a QMessageBox instance
    def showCommonMessageBox(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Common")
        msg_box.setIcon(qtw.QMessageBox.Icon.Warning)  # Set the icon to Warning
        msg_box.setText("Are you sure you want to continue?")
        msg_box.setStandardButtons(qtw.QMessageBox.StandardButton.Ok | qtw.QMessageBox.StandardButton.No)

        msg_box.show()

    def showQuestionMessageBox(self):
        reply = qtw.QMessageBox.question(
            self,
            "Question",  # Title
            "Do you want to continue?",  # Message text
            qtw.QMessageBox.StandardButton.Yes | qtw.QMessageBox.StandardButton.No,  # Buttons
            defaultButton=qtw.QMessageBox.StandardButton.No  # Optional default button
        )

        if reply == qtw.QMessageBox.StandardButton.Yes:
            print("User chose to continue.")
        else:
            print("User chose not to continue.")

    def showInformationMessageBox(self):
        qtw.QMessageBox.information(
            self,
            "Information",
            "This is an info message.",
            qtw.QMessageBox.StandardButton.Ok
        )

    def showWarningMessageBox(self):
        qtw.QMessageBox.warning(
            self,
            "Warning",
            "This is a warning message.",
            qtw.QMessageBox.StandardButton.Ok
        )

    def showCriticalMessageBox(self):
        qtw.QMessageBox.critical(
            self,
            "Critical",
            "This is a critical message.",
            qtw.QMessageBox.StandardButton.Ok
        )


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()

    sys.exit(app.exec())
