import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create user input widgets:
		user_name_input = qtw.QLineEdit(self)
		password_input = qtw.QLineEdit(self)
		password_input.setEchoMode(qtw.QLineEdit.EchoMode.Password)

		user_name_input.move(20, 10)
		password_input.move(20,50)

		self.setWindowTitle('Login Form')
		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
