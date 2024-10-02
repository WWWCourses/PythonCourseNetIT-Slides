import sys
import PyQt6.QtWidgets as qtw

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    # Create the primary window
    main_window = qtw.QMainWindow()
    main_window.setWindowTitle('Primary')
    main_window.setGeometry(100, 100, 600, 400)  # Set position and size

    # Create the secondary window using QDialog
    child_window = qtw.QDialog(parent=main_window)
    child_window.setWindowTitle('Secondary')
    child_window.setGeometry(150, 150, 300, 200)  # Set position and size for the child dialog

    # Show both windows
    main_window.show()
    child_window.show()

    sys.exit(app.exec())
