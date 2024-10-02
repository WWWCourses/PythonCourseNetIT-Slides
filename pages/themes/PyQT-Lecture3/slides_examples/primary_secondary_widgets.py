"""primary_secondary_widgets.py"""
import sys
import PyQt6.QtWidgets as qtw

class SecondaryWidget(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(300, 200)

        layout = qtw.QVBoxLayout()
        label = qtw.QLabel("This is a secondary widget!")
        layout.addWidget(label)

        self.setLayout(layout)

# Primary Widget (Main Window)
class PrimaryWidget(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primary Widget")
        self.setGeometry(50, 50, 400, 300)

        # Button for opening modal dialog
        modal_button = qtw.QPushButton("Open Modal Dialog", self)
        modal_button.setGeometry(100, 100, 200, 40)
        modal_button.clicked.connect(self.open_modal_dialog)

        # Button for opening modeless dialog
        modeless_button = qtw.QPushButton("Open Modeless Dialog", self)
        modeless_button.setGeometry(100, 150, 200, 40)
        modeless_button.clicked.connect(self.open_modeless_dialog)

    def open_modal_dialog(self):
        # Create and open a new secondary widget in modal mode
        modal_dialog = SecondaryWidget(self)
        modal_dialog.setWindowTitle('Secondary Widget in Modal Mode')
        modal_dialog.exec()  # Blocks interaction with main window until closed

    def open_modeless_dialog(self):
        # Create and open a new secondary widget in modeless mode
        modeless_dialog = SecondaryWidget(self)
        modeless_dialog.setWindowTitle('Secondary Widget in Modeless Mode')
        modeless_dialog.show()  # Allows interaction with both windows

if __name__=="__main__":

    app = qtw.QApplication(sys.argv)
    # app.setStyle("Windows")
    main_window = PrimaryWidget()
    main_window.show()
    sys.exit(app.exec())
