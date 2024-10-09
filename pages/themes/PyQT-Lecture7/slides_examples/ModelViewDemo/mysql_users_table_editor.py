# mysql_users_table_editor.py
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Setup database connection
        self.conn = self.connectToDB(user='test', password='test1234', db_name='pyqt_users_db')

        # Create the model
        self.model = self.createModel()

        # Setup UI elements
        self.table = self.createTable()
        self.save_button = qtw.QPushButton("Save Changes")
        self.save_button.clicked.connect(self.saveChanges)

        layout = qtw.QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

        self.setWindowTitle('Edit Users Table')
        self.resize(600, 400)
        self.show()

    def connectToDB(self, user, password, db_name, host="localhost", port=3306):
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName(host)
        db.setDatabaseName(db_name)
        db.setUserName(user)
        db.setPassword(password)

        if db.open():
            print("*** Connection Established ***")
        else:
            print(f"Database Error: {db.lastError().text()}")
        return db

    def createModel(self):
        model = QSqlTableModel(self)
        model.setTable("users")
        model.select()  # Load data from the 'users' table
        return model

    def createTable(self):
        table = qtw.QTableView()
        table.setModel(self.model)
        table.setEditTriggers(qtw.QAbstractItemView.EditTrigger.DoubleClicked)  # Enable editing on double-click
        table.resizeColumnsToContents()  # Adjust column widths to contents
        return table

    def saveChanges(self):
        if self.model.submitAll():  # Save changes to the database
            print("Changes saved successfully.")
        else:
            print(f"Error saving changes: {self.model.lastError().text()}")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
