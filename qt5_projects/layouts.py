import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
                             QHBoxLayout, QPushButton)
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QPalette, QColor, QPixmap)

print("This "
      "is a test "
      "to show how text can wrap.")


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class Pic(QLabel):

    def __init__(self):
        super(Pic, self).__init__()
        self.setAutoFillBackground(True)
        pixmapTarget = QPixmap('./images/hrh.jpg')
        print pixmapTarget.height()
        pixmapTarget.scaled(15, 55, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(pixmapTarget)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        self.standard()

    def standard(self):
        layout = QHBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('orange'))
        layout.addWidget(Color('blue'))

        # layout.addWidget(Pic())
        pb = QPushButton('switch layout')
        pb.setCheckable(True)
        pb.toggled.connect(self.change_layout)
        layout.addWidget(pb)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mess(self):
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)

        pb = QPushButton('switch layout')
        pb.setCheckable(True)
        pb.setChecked(True)
        pb.toggled.connect(self.change_layout)
        layout1.addWidget(pb)

        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def change_layout(self, s):
        if s:
            self.mess()
        else:
            self.standard()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
