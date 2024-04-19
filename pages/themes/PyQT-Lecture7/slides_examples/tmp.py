import sys

from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
from lib.db import DB

class Radiotheaters(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(450, 250)

        self.view = QTableWidget()
        self.view.setColumnCount(4)
        self.view.setHorizontalHeaderLabels(["ID", "Title", "Content", "Date"])

        query = QSqlQuery("SELECT id, title, content, date FROM radiotheaters")

        while query.next():
            rows = self.view.rowCount()

            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))

        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DB()

    win = Radiotheaters()
    win.show()
    sys.exit(app.exec())