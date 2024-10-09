import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class MainWindow(qtw.QWidget):

    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.conn = self.connectToDB()(user='test', password='test1234', db_name='pyqt_users_db')
        self.data = self.selectAllData()

        lAppTitle = qtw.QLabel('Simplest Table Demo')
        lAppTitle.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.table = self.createTable()

        ml = qtw.QVBoxLayout()
        ml.addWidget(lAppTitle)
        ml.addWidget(self.table)
        self.setLayout(ml)

        self.setWindowTitle('Show MySQL data in QTableWidget')
        self.show()

    def connectToDB(self, user, password, db_name, host="localhost", port=3306):
        # Specify MySQL as the database type
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName(host)
        db.setDatabaseName(db_name)
        db.setUserName(user)
        db.setPassword(password)

        if db.open():
            print("*** Connection Established ***")
        else:
            print(f"Database Error: {db.lastError().text()}")

    def selectAllData(self):
        query = QSqlQuery()


    def createTable(self):
        rows = len(self.data)
        cols = len(self.data[0])

        # init table
        table = qtw.QTableWidget();
        table.setRowCount(rows);
        table.setColumnCount(cols);
        table.setHorizontalHeaderLabels(['id', 'username', 'password']);
        table.setMinimumHeight(cols*100);
        table.setMinimumWidth(rows*100);

        # set table values
        for row in range(rows):
            for col in range(cols):
                item = qtw.QTableWidgetItem(self.data[row][col])
                table.setItem(row, col, item)

        # resize cells to content:
        table.resizeColumnsToContents();
        table.resizeRowsToContents();

        return table


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()

    sys.exit(app.exec())
