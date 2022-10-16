import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)

		self.create_actions()
		self.create_menu_bar()
		self.create_toolbar()
		self.create_doc_widget()
		self.create_status_bar()

		self.set_style()
		self.show()


	def create_menu_bar(self):
		# add menu items
		menubar = self.menuBar()
		file_menu = menubar.addMenu('&File')
		edit_menu = menubar.addMenu('&Edit')
		help_menu = menubar.addMenu('&Help')
		help_menu.addAction(self.help_action)

		file_menu.addAction(self.openAction)

	def create_toolbar(self):
		toolbar = self.addToolBar('File')
		toolbar.addAction(self.openAction)

		toolbar.setMovable(True)
		toolbar.setFloatable(False)
		toolbar.setAllowedAreas(
			qtc.Qt.ToolBarArea.TopToolBarArea |
			qtc.Qt.ToolBarArea.BottomToolBarArea
		)

		toolbar.addAction(self.help_action)

	def create_doc_widget(self):
		dock = qtw.QDockWidget("Replace")
		self.addDockWidget(qtc.Qt.DockWidgetArea.LeftDockWidgetArea, dock)

		# set dock widget to move and float (but not closeable)
		dock.setFeatures(
			qtw.QDockWidget.DockWidgetFeature.DockWidgetMovable |
			qtw.QDockWidget.DockWidgetFeature.DockWidgetFloatable
		)

		replace_widget = qtw.QWidget()
		replace_widget.setLayout(qtw.QVBoxLayout())

		self.search_text_input = qtw.QLineEdit()
		self.search_text_input.setPlaceholderText('search')
		self.replace_text_input = qtw.QLineEdit()
		self.replace_text_input.setPlaceholderText('replace')

		search_and_replace_btn = qtw.QPushButton(
			"Search and Replace",
			)
		search_and_replace_btn.clicked.connect(self.search_and_replace)

		replace_widget.layout().addWidget(self.search_text_input)
		replace_widget.layout().addWidget(self.replace_text_input)
		replace_widget.layout().addWidget(search_and_replace_btn)
		replace_widget.layout().addStretch()

		dock.setWidget(replace_widget)

	def create_status_bar(self):
		# create status bar widget and atach it to main window:
		self.status_bar = qtw.QStatusBar()
		self.setStatusBar(self.status_bar)

		# show temporary message for 3 second:
		self.status_bar.showMessage('Welcome to My Text Editor',3000)

		charcount_label = qtw.QLabel("chars: 0")
		self.textedit.textChanged.connect(
			lambda: charcount_label.setText( "chars: " + str(len(self.textedit.toPlainText())) )
		)
		self.status_bar.addPermanentWidget(charcount_label)

	def create_actions(self):
		self.openAction = qtg.QAction("&Open...", self)
		self.openAction.triggered.connect(self.open_new_file)
		self.saveAction = qtg.QAction("&Save", self)
		self.exitAction = qtg.QAction("&Exit", self)

		self.help_action = qtg.QAction(
			self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogHelpButton),
			'Help',
			self  # important to pass the parent!
		)
		# add signal
		self.help_action.triggered.connect(lambda : qtw.QMessageBox.information(self,'Not Implemented','Sorry, no help yet!'))

	def open_new_file(self):
		self.file_path, filter_type = qtw.QFileDialog.getOpenFileName(self, "Open new file","", "All files (*)")
		if self.file_path:
			with open(self.file_path, "r") as f:
				file_contents = f.read()
				self.setWindowTitle(self.file_path)
				self.textedit.setText(file_contents)

	def search_and_replace(self):
		print('search_and_replace')

	def set_style(self):
		with open("./main.css") as f:
			mainStyle = f.read()

		self.setStyleSheet(mainStyle)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
