import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
                             QComboBox, QDateEdit, QCheckBox, QDateTimeEdit,
                             QDial, QDoubleSpinBox, QFontComboBox, QLCDNumber,
                             QLineEdit, QProgressBar, QPushButton, QRadioButton,
                             QSlider, QSpinBox, QTimeEdit, QWidget)
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QPixmap)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()
        widgets = [QCheckBox,
             QComboBox,
             QDateEdit,
             QDateTimeEdit,
             QDial,
             QDoubleSpinBox,
             QFontComboBox,
             QLCDNumber,
             QLabel,
             QLineEdit,
             QProgressBar,
             QPushButton,
             QRadioButton,
             QSlider,
             QSpinBox,
             QTimeEdit]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
