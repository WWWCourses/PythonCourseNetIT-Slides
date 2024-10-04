import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class DataEntryDialog(qtw.QDialog):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My Form')
		self.setGeometry(500,400,200,100)

		# ------------------------- create and atach widgets ------------------------- #
		self.edit = qtw.QLineEdit()
		self.btn_submit = qtw.QPushButton('Submit')

		self.setLayout(qtw.QVBoxLayout())
		self.layout().addWidget(self.edit)
		self.layout().addWidget(self.btn_submit)

class MainWindow(qtw.QWidget):
	signal1 = qtc.pyqtSignal(str)

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My App')
		self.setGeometry(400,300,300,200)

		# ------------------------- create and atach widgets ------------------------- #
		self.label = qtw.QLabel('Initial Text')
		self.btn_change = qtw.QPushButton('change text')

		self.main_layout = qtw.QVBoxLayout()
		self.main_layout.addWidget(self.label)
		self.main_layout.addWidget(self.btn_change)
		self.setLayout(self.main_layout)

		# ---------------------------------- signals --------------------------------- #
		self.btn_change.clicked.connect(self.onChangeClicked)

		self.show()

	def onChangeClicked(self):
		self.dialog = DataEntryDialog(self)
		# tightly-coupled approach: we must know dialog's implementation
		self.dialog.edit.setText(self.label.text())
		self.dialog.btn_submit.clicked.connect(self.on_dialog_text_changed)

		self.dialog.show()


	def on_dialog_text_changed(self):
		self.label.setText(self.dialog.edit.text())
		self.dialog.close()


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())