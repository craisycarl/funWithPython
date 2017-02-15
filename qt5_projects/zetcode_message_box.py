# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This program shows a confirmation
message box when we click on the close
button of the application window.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)


class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')

    def closeEvent(self, event):
        
        reply = QMessageBox.question(QMessageBox(), 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No
                                     )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            print 'cancel was clicked'
            event.ignore()        

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
