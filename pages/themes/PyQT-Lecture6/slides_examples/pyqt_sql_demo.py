from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6.QtWidgets import QTableView, QApplication
import sys


class DB:
    def __init__(self) -> None:
        self.conn()

    def conn(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bnr.db')

        if not db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"),
                QtGui.QMessageBox.Cancel)

            return False

        self.query = QSqlQuery()
        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DB()