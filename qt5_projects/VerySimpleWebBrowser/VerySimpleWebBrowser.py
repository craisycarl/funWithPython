"""
    ********************* VerySimpleWebBrowser ************************

    This is a Very Simple Web Browser implemented over Qt and QtWebKit.
    More info on: https://codescience.wordpress.com/

    author: Juan Manuel Garcia <jmg.utn@gmail.com>

    Converted to PyQt5

    *******************************************************************
"""

from PyQt5.QtWidgets import (QWidget, QMainWindow, QHBoxLayout, QFrame, QVBoxLayout,
                             QLineEdit, QPushButton, QApplication)
from PyQt5.QtGui import (QIcon)
from PyQt5.QtCore import (QUrl, QSize)

from PyQt5.QtWebKitWidgets import QWebView


class Browser(QMainWindow):

    def __init__(self):
        """
            Initialize the browser GUI and connect the events
        """

        super(Browser, self).__init__()
        self.resize(800, 600)
        self.centralwidget = QWidget(self)

        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(1, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)

        self.gridLayout = QVBoxLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QHBoxLayout()
        self.tb_url = QLineEdit()
        self.bt_back = QPushButton()
        self.bt_ahead = QPushButton()

        self.bt_back.setIcon(QIcon("./icons/previous.png"))
        self.bt_back.setMinimumSize(40, 40)
        self.bt_back.setIconSize(QSize(32, 32))
        self.bt_ahead.setIcon(QIcon('./icons/next.png'))
        self.bt_ahead.setMinimumSize(40, 40)
        self.bt_ahead.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.bt_back)
        self.horizontalLayout.addWidget(self.bt_ahead)
        self.horizontalLayout.addWidget(self.tb_url)
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        # self.connect(self.tb_url, self.SIGNAL("returnPressed()"), self.browse)
        self.tb_url.returnPressed.connect(self.browse)

        # self.connect(self.bt_back, self.SIGNAL("clicked()"), self.html.back)
        self.bt_back.clicked.connect(self.html.back)

        # self.connect(self.bt_ahead, self.SIGNAL("clicked()"), self.html.forward)
        self.bt_ahead.clicked.connect(self.html.forward)

        # self.connect(self.html, self.SIGNAL("urlChanged(const QUrl)"), self.url_changed)
        self.html.urlChanged.connect(self.url_changed)

        self.default_url = "http://codescience.wordpress.com/"
        self.tb_url.setText(self.default_url)
        self.browse()

    def browse(self):
        """
            Make a web browse on a specific url and show the page on the
            Webview widget.
        """

        url = self.tb_url.text() if self.tb_url.text() else self.default_url
        self.html.load(QUrl(url))
        self.html.show()
        
    def url_changed(self, url):
        """
            Triggered when the url is changed
        """
        self.tb_url.setText(url.toString())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = Browser()
    main.show()
app.exec_()
