import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class LoginForm(qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create child widgets:
		leUserName = qtw.QLineEdit(self)
		lePassword = qtw.QLineEdit(self)
		lePassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

		btnLogin = qtw.QPushButton('Login')
		btnCancel = qtw.QPushButton('Cancel')

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

		# attach mainLayout to our LoginForm widget (self)
		self.setLayout(mainLayout)

		# set some properties of LoginForm widget(self)
		self.setWindowTitle('Login Form')
		# self.setGeometry(0, 0, 1024, 680)
		self.show();

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = LoginForm()

	sys.exit(app.exec())
