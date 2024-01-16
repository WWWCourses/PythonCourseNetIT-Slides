import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from buttons import ButtonRole, StyledButton


class LoginForm(qtw.QWidget):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set some properties of LoginForm widget(self)
        self.setWindowTitle('Login Form')
        # center on screen
        window_width = 300
        window_height = 250
        screen = qtg.QGuiApplication.primaryScreen()
        if screen:
            available_geometry = screen.availableGeometry()

            self.setGeometry(
                (available_geometry.width() - window_width) // 2,
                (available_geometry.height() - window_height) // 2,
                window_width,
                window_height
            )

        # create child widgets:
        leUserName = qtw.QLineEdit(self)
        lePassword = qtw.QLineEdit(self)
        lePassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        btnLogin = StyledButton('Login', ButtonRole.PRIMARY)
        btnCancel = StyledButton('Cancel', role=ButtonRole.DEFAULT)

        # create buttons layout:
        btnLayout = qtw.QHBoxLayout()
        btnLayout.addWidget(btnLogin,1)
        btnLayout.insertStretch(1,1)
        btnLayout.addWidget(btnCancel, 1)

        # create main Form layout
        mainLayout = qtw.QFormLayout()
        mainLayout.addRow('User Name', leUserName)
        mainLayout.addRow('Password', lePassword)
        mainLayout.addRow('', btnLayout)
        mainLayout.setVerticalSpacing(18)

        # attach mainLayout to our LoginForm widget (self)
        self.setLayout(mainLayout)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    loginForm = LoginForm()

    sys.exit(app.exec())
