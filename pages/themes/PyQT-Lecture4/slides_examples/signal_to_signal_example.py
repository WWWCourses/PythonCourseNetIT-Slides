# Filename: signal_to_signal_example.py

import sys
from PyQt6.QtWidgets import QApplication, QSpinBox, QSlider, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QSpinBox and a QSlider
        self.spin_box = QSpinBox()
        self.slider = QSlider()

        # Set range for both to make their values match
        self.spin_box.setRange(0, 100)
        self.slider.setRange(0, 100)

        # Connect the valueChanged signal of QSpinBox to the valueChanged signal of QSlider
        self.spin_box.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spin_box.setValue)

        # Layout to organize widgets
        layout = QVBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.slider)

        self.setLayout(layout)

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
