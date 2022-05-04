import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Image test')

		# create label
		self.label = qtw.QLabel(self)

		# load image
		pixmap = qtg.QPixmap('../images/MainWindowComponents.png')

		# add image to label
		self.label.setPixmap(pixmap)

		# Optional, resize label to image size
		self.label.resize(pixmap.width(),
						  pixmap.height())


		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
