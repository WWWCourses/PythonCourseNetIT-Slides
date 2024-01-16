import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):
	sig_submit = qtc.pyqtSignal(int,int)

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.btnSubmit = qtw.QPushButton('Submit')
		self.lOutput = qtw.QLabel('Output')
		self.ml = qtw.QVBoxLayout(self)
		self.ml.addWidget(self.btnSubmit)
		self.ml.addWidget(self.lOutput)


		self.btnSubmit.clicked.connect(self.btnSubmitClicked)
		self.sig_submit.connect(self.customSignalSlot)
		self.show();

	def btnSubmitClicked(self):
		x = 2
		self.sig_submit.emit(x,4)

	def customSignalSlot(self, *args):
		print('customSignalSlot')
		print(args)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
