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
        self.styleTable()


    def createTable(self):
        rows = 4
        cols = 3

        # init table
        self.table = qtw.QTableWidget(self)
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        self.table.setHorizontalHeaderLabels(['Heading1', 'Heading2', 'Heading3'])

        # set table values
        for row in range(rows):
            for col in range(cols):
                self.table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

        # resize cells to content:
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        self.table.show()

    def styleTable(self):
        self.table.setAlternatingRowColors(True)

        self.table.setAlternatingRowColors(True)
        with open('./main.css',"r") as f:
            style_sheet = f.read()

        self.table.setStyleSheet(style_sheet)

        self.table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)






if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())