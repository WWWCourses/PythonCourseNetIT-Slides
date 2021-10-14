from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication([])

main_window = QWidget()
main_window.show()

# start the event loop
app.exec_()

print('App END')