from PyQt5.QtWidgets import (QApplication, QDialog, QListWidget)
from PyQt5.uic import loadUi


class Win(QDialog):
    def __init__(self, *args, **kwargs):
        super(Win, self).__init__(*args, **kwargs)

        self.ui = loadUi('basic_layout.ui', self)
        self.setWindowTitle("My Awesome Dialog Box")
        self.fill_in_gui()
        self.ui.show()

    def fill_in_gui(self):
        for i in range(10):
            self.ui.comboBox_1.addItem('Item %s' %(i + 1))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_win = Win()

    sys.exit(app.exec_())
