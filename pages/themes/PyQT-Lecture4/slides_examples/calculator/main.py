import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class Calculator(qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setupUI()

		self.setWindowTitle('Calculator')

	def setupUI(self):
		# create child widgets
		self.output = qtw.QLabel('Output')

		btnBackspace = qtw.QPushButton('Backspace')
		btnClear = qtw.QPushButton('Clear')
		btnClearAll = qtw.QPushButton('ClearAll')

		# create Main Layout
		self.mainLayout = qtw.QVBoxLayout(self)
		self.mainLayout.addWidget(self.output)

		# create Buttons Layout
		buttonsLayout=qtw.QGridLayout()

		# create 1st row
		buttonsLayout.addWidget(btnBackspace,0,0,1,2)
		buttonsLayout.addWidget(btnClear,0,2,1,2)
		buttonsLayout.addWidget(btnClearAll,0,4,1,2)

		# create 2nd row
		rowBtnNames = ['MC', '7', '8', '9', '%', 'Sqrt']
		for i,name in enumerate(rowBtnNames):
			btn = qtw.QPushButton(name)
			buttonsLayout.addWidget(btn,1,i)

		self.mainLayout.addLayout(buttonsLayout)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	calc = Calculator()
	calc.show()

	sys.exit(app.exec())
