from PyQt6.QtWidgets import QApplication, QTableView
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
import sys

def create_connection():
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('pyqt_users_db')
    db.setUserName('test')
    db.setPassword('test1234')
    if not db.open():
        print(db.lastError().text())
        return False
    return True

def show_table():
    app = QApplication(sys.argv)

    if not create_connection():
        sys.exit(1)

    # Setup the model
    model = QSqlTableModel()
    model.setTable('users')
    # model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)  # Auto-save changes
    model.select()  # Ensure the model fetches data

    # Check if the model retrieved any rows
    if model.rowCount() == 0:
        print("No data retrieved from the table.")

    # Setup the view
    view = QTableView()
    view.setModel(model)

    # Optional: Resize the columns based on content
    view.resizeColumnsToContents()

    view.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    show_table()
