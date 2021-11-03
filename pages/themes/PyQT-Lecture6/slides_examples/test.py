import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):
	sig_submit = qtc.pyqtSignal(str)

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUI()

		# self.btn_ok.clicked.connect(self.on_ok)
		self.le_user_name.textChanged.connect(self.on_ok)

	@qtc.pyqtSlot(bool)
	def onSubmit(self):
		self.sig_submit.emit(self.le_user_name.text())
		self.close()

	# @qtc.pyqtSlot(str)
	def on_ok(self,*args):
		print(args)

	def setupUI(self):
		self.setWindowTitle('Main')

		self.le_user_name = qtw.QLineEdit()
		self.btn_ok = qtw.QPushButton('OK')

		main_layout = qtw.QVBoxLayout(self)
		main_layout.addWidget(self.le_user_name)
		main_layout.addWidget(self.btn_ok)

		self.show();





if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
