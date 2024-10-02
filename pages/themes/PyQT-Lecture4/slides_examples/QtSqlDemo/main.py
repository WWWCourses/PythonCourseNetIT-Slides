# Filename: main.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableView
from PyQt6.QtSql import QSqlTableModel
import db

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Books Database')
        self.setGeometry(100, 100, 600, 400)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create the "Show Authors" button
        show_authors_btn = QPushButton('Show Authors')
        show_authors_btn.clicked.connect(self.show_authors)

        # Create a table view for displaying data
        self.table_view = QTableView()

        # Add widgets to the main layout
        main_layout.addWidget(show_authors_btn)
        main_layout.addWidget(self.table_view)

        self.setLayout(main_layout)

        # Establish database connection
        if not db.create_connection():
            show_authors_btn.setEnabled(False)

    def show_authors(self):
        # Create and configure the model for the "author" table
        model = QSqlTableModel()
        model.setTable('author')
        model.select()

        # Set the model to the table view
        self.table_view.setModel(model)

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
