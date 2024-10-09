# custom_context_menu_actions.py
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Custom context menu actions demo')
        self.setGeometry(500, 200, 400, 300)  # Set the window size

        self.createTable()  # Initialize the table UI

    def createTable(self):
        rows = 4
        cols = 3

        # Initialize the table
        self.table = qtw.QTableWidget(self)
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        self.table.setHorizontalHeaderLabels(['Heading1', 'Heading2', 'Heading3'])

        # Set table values
        for row in range(rows):
            for col in range(cols):
                self.table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row + 1},{col + 1}'))

        # Resize cells to fit content
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        # Set the context menu policy to allow for custom context menus in this widget
        self.table.setContextMenuPolicy(qtc.Qt.ContextMenuPolicy.CustomContextMenu)

        # Connect the custom context menu requested signal to the context_actions method
        self.table.customContextMenuRequested.connect(self.context_actions)

    def context_actions(self, pos):
        menu = qtw.QMenu()

        # Get the index of the currently selected row
        current_row = self.table.currentRow()

        # Add action to insert a new row
        menu.addAction("Add Row", lambda: self.table.insertRow(current_row if current_row >= 0 else self.table.rowCount()))

        # Add action to remove the currently selected row
        menu.addAction("Remove Row", lambda: self.table.removeRow(current_row) if current_row >= 0 else None)

        # Execute the menu at the cursor position
        menu.exec(self.table.viewport().mapToGlobal(pos))


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()  # Show the main window

    sys.exit(app.exec())
