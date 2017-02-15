from PyQt5.QtGui import (QStandardItemModel, QStandardItem)
from PyQt5.QtWidgets import (QWidget, QMessageBox, QMainWindow, QApplication)
from PyQt5.QtCore import (Qt)
from PyQt5.uic import loadUi


class MyPopup(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyPopup, self).__init__(*args, **kwargs)

    def onShowInformation(self):
        QMessageBox.information(self, "Information", "Python rocks!")

    def onShowCriticalMessage(self):
        """
        Show the critical message
        """
        flags = QMessageBox.Abort
        flags |= QMessageBox.Retry
        flags |= QMessageBox.Ignore

        result = QMessageBox.critical(self, "CRITICAL ERROR",
                                            "You're trying Perl aren't you?",
                                            flags)
        if result == QMessageBox.Abort:
            print "Aborted!"
        elif result == QMessageBox.Retry:
            print "Retrying!"
        elif result == QMessageBox.Ignore:
            print "Ignoring!"


class ConfigGUITop(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ConfigGUITop, self).__init__(*args, **kwargs)

        self.ui = loadUi('mainwindow.ui', self)
        self.setWindowTitle("My Awesome App")
        self.ui.show()

        self.model, self.model_unit, self.model_group, self.model_sep = None, None, None, None
        self.model_2, self.model_unit_2 = None, None

        self.sliderBar1, self.sliderBarUnit, self.sliderBarGroup, self.sliderBarSep = None, None, None, None
        self.sliderBar2, self.sliderBarUnit2 = None, None

        self.init_ui()

    def init_ui(self):
        self.ui.statusBar.showMessage('Ready!')
        self.ui.actionExit.setShortcut('Ctrl+Q')
        self.ui.actionExit.setStatusTip('Exit application')
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Qt.triggered.connect(self.about_qt)
        self.ui.actionMessage_Box_Test.triggered.connect(self.about_test_box)

        # ************************** listView stuff ************************** #
        self.model = QStandardItemModel(self.ui.listView)
        self.model_unit = QStandardItemModel(self.ui.listView_unit)
        self.model_group = QStandardItemModel(self.ui.listView_group)
        self.model_sep = QStandardItemModel(self.ui.listView_sep)
        self.model_2 = QStandardItemModel(self.ui.listView_2)
        self.model_unit_2 = QStandardItemModel(self.ui.listView_unit_2)
        foods = [
            'Pie',  # Must be store-bought
            'Cookie dough',  # Must be store-bought
            'Cookie dough',  # Must be store-bought
            'Cookie dough',  # Must be store-bought
            'Cookie dough',  # Must be store-bought
            'Cookie dough',  # Must be store-bought
            'Cookie dough',  # Must be store-bought
            'Chocolate whipped cream',  # Must be plentiful
            'Hummus',  # Must be homemade
            'Hummus',  # Must be homemade
            'Hummus',  # Must be homemade
            'Hummus',  # Must be homemade
            'Hummus',  # Must be homemade
            'Spaghetti',  # Must be saucy
            'Spaghetti',  # Must be saucy
            'Spaghetti',  # Must be saucy
            'Spaghetti',  # Must be saucy
            'Dal makhani',  # Must be spicy
            'Dal makhani',  # Must be spicy
            'Dal makhani',  # Must be spicy
            'Dal makhani',  # Must be spicy
            'Dal makhani',  # Must be spicy
            'Chocolate whipped cream'  # Must be plentiful
        ]
        measurements = ['ICCI1', 'ICCI2', 'ICCI3', 'ICCI4']
        units = ['mA', 'mA', 'mA', 'mA', 'mA', 'mA', 'mA', 'mA', 'mA', 'mA', 'mV', 'mA', 'mA', 'mA', 'mA', 'V', 'mA',
                 'mA', 'mA', 'mA', 'mA', 'mA', 'Ohm']
        units_2 = ['mA', 'mA', 'A', 'A']
        empty = [' ']*len(foods)

        for food in foods:
            # Create an item with a caption
            item = QStandardItem(food)

            # Add a checkbox to it
            item.setCheckable(True)

            # Add the item to the model
            self.model.appendRow(item)

        for unit in units:
            item = QStandardItem(unit)
            self.model_unit.appendRow(item)

        for emptyItem in empty:
            item = QStandardItem(emptyItem)
            item.setCheckable(True)
            self.model_group.appendRow(item)

        for emptyItem in empty:
            item = QStandardItem(emptyItem)
            item.setCheckable(True)
            self.model_sep.appendRow(item)

        for meas in measurements:
            # Create an item with a caption
            item = QStandardItem(meas)

            # Add a checkbox to it
            item.setCheckable(True)

            # Add the item to the model
            self.model_2.appendRow(item)

        for unit in units_2:
            item = QStandardItem(unit)
            self.model_unit_2.appendRow(item)

        # Apply the model to the list view
        self.ui.listView.setModel(self.model)
        self.ui.listView_unit.setModel(self.model_unit)
        self.ui.listView_group.setModel(self.model_group)
        self.ui.listView_sep.setModel(self.model_sep)
        self.ui.listView_2.setModel(self.model_2)
        self.ui.listView_unit_2.setModel(self.model_unit_2)

        self.sliderBar1 = self.ui.listView.verticalScrollBar()
        self.sliderBarUnit = self.ui.listView_unit.verticalScrollBar()
        self.sliderBarGroup = self.ui.listView_group.verticalScrollBar()
        self.sliderBarSep = self.ui.listView_sep.verticalScrollBar()
        self.sliderBar2 = self.ui.listView_2.verticalScrollBar()
        self.sliderBarUnit2 = self.ui.listView_unit_2.verticalScrollBar()
        self.sliderBar1.valueChanged.connect(self.sync_scroll)
        self.sliderBar2.valueChanged.connect(self.sync_scroll_2)
        
        self.sliderBarUnit.setStyleSheet("QScrollBar {width:0px;}")
        self.sliderBarGroup.setStyleSheet("QScrollBar {width:0px;}")
        self.sliderBarSep.setStyleSheet("QScrollBar {width:0px;}")
        self.sliderBarUnit2.setStyleSheet("QScrollBar {width:0px;}")
        # ************************** listView stuff ************************** #
        
        # ************************** select all     ************************** #
        self.ui.SelectAllStim.stateChanged.connect(self.select_all)
        self.ui.SelectAllGroup.stateChanged.connect(self.select_all)
        self.ui.SelectAllSep.stateChanged.connect(self.select_all)
        # ************************** select all     ************************** #
        
        self.ui.pushButton_PlotIt.clicked.connect(self.plot_it)

    def plot_it(self):
        check_item_names, check_item_index = [], []
        check_items_group_list, check_item_state_list = [], []
        
        i = 0
        while self.model.item(i):
            if self.model.item(i).checkState():
                check_item_names.append(self.model.item(i).text())
                check_item_index.append(self.model.item(i).row())
            i += 1
        
        for index in check_item_index:
            if self.model_group.item(index).checkState():
                check_items_group_list.append(True)
            else:
                check_items_group_list.append(False)
            
            if self.model_sep.item(index).checkState():
                check_item_state_list.append(True)
            else:
                check_item_state_list.append(False)

        # Print what you found
        for i, plotString in enumerate(check_item_names):
            print 'checked item index found at %s, %s, %s' % (plotString, check_items_group_list[i],
                                                              check_item_state_list[i])

        sender = self.sender()
        self.ui.statusBar.showMessage(sender.text() + ' was pressed')
        modifiers = QApplication.keyboardModifiers()
        msg = self.ui.statusBar.currentMessage()
        if modifiers == Qt.ShiftModifier:
            self.ui.statusBar.showMessage(msg + ' Shift+Click')
        if modifiers == Qt.ControlModifier:
            self.ui.statusBar.showMessage(msg + ' Control+Click')
        elif modifiers == (Qt.ControlModifier | Qt.ShiftModifier):
            self.ui.statusBar.showMessage(msg + ' Control+Shift+Click')
        
    def sync_scroll(self):
        slider_value = self.sliderBar1.value()
        self.sliderBarUnit.setValue(slider_value)
        self.sliderBarGroup.setValue(slider_value)
        self.sliderBarSep.setValue(slider_value)
        
    def sync_scroll_2(self):
        slider_value = self.sliderBar2.value()
        self.sliderBarUnit2.setValue(slider_value)
    
    def close(self):
        sys.exit()

    def about(self):
        QMessageBox.about(self, "About Dock Widgets",
                          "The <b>Dock Widgets</b> example demonstrates how to use "
                          "Qt's dock widgets. You can enter your own text, click a "
                          "customer to add a customer name and address, and click "
                          "standard paragraphs to add them.")

    @staticmethod
    def about_qt():
        QApplication.instance().aboutQt()

    @staticmethod
    def about_test_box():
        print "Opening a new popup window..."
        w = MyPopup()
        w.onShowInformation()
        w.onShowCriticalMessage()
        
    def select_all(self):
        o = self.sender()
        check_all_boxes = False
        if o.objectName() == 'SelectAllStim':
            m = self.model
            check_all_boxes = self.ui.SelectAllStim.isChecked()
        elif o.objectName() == 'SelectAllGroup':
            m = self.model_group
            check_all_boxes = self.ui.SelectAllGroup.isChecked()
        elif o.objectName() == 'SelectAllSep':
            m = self.model_sep
            check_all_boxes = self.ui.SelectAllSep.isChecked()
        
        item_list = []
        i = 0
        while m.item(i):
            item_list.append(m.item(i))
            i += 1

        if check_all_boxes:
            for it in item_list:
                it.setCheckState(Qt.Checked)
        else:
            for it in item_list:
                it. setCheckState(Qt.Unchecked)
                # if it.checkState():
                #     print 'checked item index found at %s' % it.row()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_win = ConfigGUITop()

    sys.exit(app.exec_())
