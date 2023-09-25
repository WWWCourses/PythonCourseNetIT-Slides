import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")

		button = qtw.QPushButton("Press Me!")
		button.setCheckable(True)
		button.clicked.connect(self.the_button_was_clicked)
		button.clicked.connect(self.the_button_was_toggled)

		mainLayout = qtw.QVBoxLayout(self)
		mainLayout.addWidget(button)
		self.setLayout(mainLayout)



	def the_button_was_clicked(self,*args):
		print("Clicked!")
		print(f'args: {args}')

	def the_button_was_toggled(self, checked):
		print("Checked?", checked)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
