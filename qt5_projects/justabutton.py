from PyQt5.QtWidgets import (QWidget, QMainWindow, QHBoxLayout, QFrame, QVBoxLayout,
                             QLineEdit, QPushButton, QApplication, QLabel)
from PyQt5.QtGui import (QIcon)
from PyQt5.QtCore import (QUrl, QSize, Qt)

from PyQt5.QtWebKitWidgets import QWebView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        self.label = QLabel("THIS IS AWESOME!!!")
        self.bt_back = QPushButton()
        self.tb_url = QLineEdit()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.bt_back)
        self.layout.addWidget(self.tb_url)


        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

        self.tb_url.returnPressed.connect(self.browse)

        self.default_url = "http://codescience.wordpress.com/"
        self.tb_url.setText(self.default_url)

    def browse(self):
        print "this is a test!!!!"

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
app.exec_()
