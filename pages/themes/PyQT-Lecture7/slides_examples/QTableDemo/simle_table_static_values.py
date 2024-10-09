# simle_table_static_values.py
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('')
        self.show()

        self.createTable()


    def createTable(self):
        rows = 4
        cols = 3

        # init table
        table = qtw.QTableWidget(self)
        table.setRowCount(rows)
        table.setColumnCount(cols)
        table.setHorizontalHeaderLabels(['Heading1', 'Heading2', 'Heading3'])

        # set table values
        for row in range(rows):
            for col in range(cols):
                table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

        # resize cells to content:
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        table.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())