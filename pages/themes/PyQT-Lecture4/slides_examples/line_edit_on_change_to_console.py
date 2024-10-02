import sys
from PyQt6 import QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set up the main layout
        main_layout = qtw.QVBoxLayout(self)

        # Create and add the QLineEdit to the layout
        self.leTest = qtw.QLineEdit()
        main_layout.addWidget(self.leTest)

        # Connect the textChanged signal to the custom slot
        self.leTest.textChanged.connect(self.print_content)

        self.setWindowTitle('Demo')
        self.show()

    def print_content(self, text):
        print(f'Content: {text}')

# Run the application
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
