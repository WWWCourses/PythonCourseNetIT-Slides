import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)

		self.create_actions()
		self.create_menu_bar()
		self.create_toolbar()

		self.show();

	def create_menu_bar(self):
		# add menu items
		menubar = self.menuBar()
		file_menu = menubar.addMenu('&File')
		edit_menu = menubar.addMenu('&Edit')
		help_menu = menubar.addMenu('&Help')

		file_menu.addAction(self.openAction)

	def create_toolbar(self):
		toolbar = self.addToolBar('File')
		toolbar.addAction(self.openAction)

		toolbar.setMovable(True)
		toolbar.setFloatable(False)
		toolbar.setAllowedAreas(
			qtc.Qt.TopToolBarArea |
			qtc.Qt.BottomToolBarArea
		)

	def create_actions(self):
		self.openAction = qtw.QAction("&Open...", self)
		self.saveAction = qtw.QAction("&Save", self)
		self.exitAction = qtw.QAction("&Exit", self)


	def open_new_file(self):
		self.file_path, filter_type = qtw.QFileDialog.getOpenFileName(self, "Open new file","", "All files (*)")
		if self.file_path:
			with open(self.file_path, "r") as f:
				file_contents = f.read()
				self.title.setText(self.file_path)
				self.scrollable_text_area.setText(file_contents)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
