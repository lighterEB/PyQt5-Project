#coding:utf-8

"""
Module implementing LayoutDemo
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,  QApplication
from Ui_firstmainWin import Ui_MainWindow

class FirstWin(QMainWindow,  Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self,  parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(FirstWin,  self).__init__(parent)
        self.setupUi(self)
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentationtion goes here
        """
        print('收益_min:', self.doubleSpinBox_returns_min.text())
        print('收益_max:', self.doubleSpinBox_returns_max.text())
        print('最大撤回_min:', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大撤回_max:', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:', self.doubleSpinBox_sharp_min.text())
        print('sharp比_max:', self.doubleSpinBox_sharp_max.text())
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = FirstWin()
    ui.show()
    sys.exit(app.exec_())
