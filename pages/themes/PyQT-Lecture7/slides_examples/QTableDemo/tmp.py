from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMenu, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QPoint
import sys

class TableWidgetWithContextMenu(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)  # 0 rows, 3 columns for example
        self.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

        # Enable custom context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_context_menu)

    def open_context_menu(self, position: QPoint):
        # Create the context menu
        menu = QMenu()

        # Add the "Insert Row" option
        insert_row_action = menu.addAction("Insert Row")

        # Connect the action to a function
        insert_row_action.triggered.connect(self.add_new_row)

        # Display the context menu at the cursor position
        menu.exec(self.mapToGlobal(position))

    def add_new_row(self):
        # Get current row count
        row_count = self.rowCount()

        # Insert a new row at the end
        self.insertRow(row_count)

        # Optionally set default data for the new row
        self.setItem(row_count, 0, QTableWidgetItem("New Item 1"))
        self.setItem(row_count, 1, QTableWidgetItem("New Item 2"))
        self.setItem(row_count, 2, QTableWidgetItem("New Item 3"))

def show_table():
    app = QApplication(sys.argv)

    # Setup the main window and layout
    window = QWidget()
    layout = QVBoxLayout()

    # Create the custom table widget with context menu
    table_widget = TableWidgetWithContextMenu()

    # Add the table widget to the layout
    layout.addWidget(table_widget)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    show_table()
