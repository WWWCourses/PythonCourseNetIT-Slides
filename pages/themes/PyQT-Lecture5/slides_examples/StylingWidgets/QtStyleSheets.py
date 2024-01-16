import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.userNameInput = qtw.QLineEdit()
		self.btnSubmit = qtw.QPushButton('Submit')
		self.btnSubmit.setObjectName('btnSubmit')
		self.btnCancel = qtw.QPushButton('Cancel')
		self.btnCancel.setStyleSheet("""
			background-color:gray;
			padding:10px;
		""")

		self.mainLayout = qtw.QFormLayout(self)
		self.mainLayout.addRow('user name: ', self.userNameInput)
		self.btnLayout = qtw.QHBoxLayout()
		self.btnLayout.addWidget(self.btnSubmit)
		self.btnLayout.addWidget(self.btnCancel)
		self.mainLayout.addRow(self.btnLayout)

		self.setupStyleSheet()

		self.setWindowTitle('Qt Style Sheets Demo')
		self.show()

	def setupStyleSheet(self):
		with open('./main.css','r') as f:
			mainStyle = f.read()

		self.setStyleSheet(mainStyle)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
