import sys
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Login Form')

        # Create user input widgets
        self.user_name_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        # Create the buttons
        btn_login = qtw.QPushButton('Login')
        btn_cancel = qtw.QPushButton('Cancel')

        # Create buttons layout
        buttons_layout = qtw.QHBoxLayout()
        buttons_layout.addWidget(btn_login)
        buttons_layout.addWidget(btn_cancel)

        # Create form layout and add widgets
        form_layout = qtw.QFormLayout()
        form_layout.addRow('User name: ', self.user_name_input)
        form_layout.addRow('Password: ', self.password_input)
        form_layout.addRow('', buttons_layout)
        # Adjust margins and spacing to control position
        form_layout.setContentsMargins(50, 50, 50, 50)  # (left, top, right, bottom)
        form_layout.setSpacing(20)  # Spacing between rows

        # Apply the form layout
        self.setLayout(form_layout)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
