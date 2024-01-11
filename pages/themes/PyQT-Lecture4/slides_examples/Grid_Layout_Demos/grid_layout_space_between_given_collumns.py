import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

class GridDemo(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create buttons grid widget
        buttons_widget = qtw.QWidget(parent=self)
        # buttons_widget.setGeometry(qtc.QRect(0, 0, 200, 100))
        # Set background color using style sheet
        buttons_widget.setStyleSheet("""
            background-color: black;
            color:white;
        """)

        # Create the buttons grid layout
        buttons_layout = qtw.QGridLayout(buttons_widget)
        buttons_layout.setHorizontalSpacing(10)
        buttons_layout.setVerticalSpacing(10)

        # Button positions
        button_positions = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 3)
        ]

        for (text, row, col) in button_positions:
            button = qtw.QPushButton(text)
            buttons_layout.addWidget(button, row, col)


        # Add a spacer item with a width of 100 pixels between the 2nd and 3rd columns
        spacer = qtw.QSpacerItem(100, 0, qtw.QSizePolicy.Policy.Fixed, qtw.QSizePolicy.Policy.Fixed)
        buttons_layout.addItem(spacer, 0, 2, rowSpan=buttons_layout.rowCount(), columnSpan=1)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = GridDemo()
    window.setWindowTitle('Grid Layout Demo')

    # Set window size and center it on the screen
    window_width = 400
    window_height = 400
    available_geometry = qtg.QGuiApplication.primaryScreen().availableGeometry()
    print(f'available_geometry={available_geometry}')

    window.setGeometry(
        (available_geometry.width() - window_width) // 2,
        (available_geometry.height() - window_height) // 2,
        window_width,
        window_height
    )

    window.show()
    sys.exit(app.exec())
