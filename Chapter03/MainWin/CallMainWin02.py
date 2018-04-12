# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication,  QMainWindow,  QFileDialog
from MainForm2 import Ui_MainWindow
from ChildrenForm2 import Ui_ChildrenForm2

class MainForm(QMainWindow,  Ui_MainWindow):
    def __init__(self):
        super(MainForm,  self).__init__()
        self.setupUi(self)
        
        # self.child = children()生成子窗口实例 self.child
        self.child = ChildrenForm()
         
        # 菜单的单击事件，当单击关闭菜单时连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 菜单的单击事件，当单击关闭菜单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)
        
        # 单击actionTst，子窗口就会显示在主窗口的MaingridLayout中
        self.addWinAction.triggered.connect(self.childShow)
        
    def childShow(self):
        # 添加子窗口
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
    
    def openMsg(self):
        file,  ok = QFileDialog.getOpenFileName(self,  "打开",  "C:/",  "ALLFiles (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)
        
class ChildrenForm(QWidget,  Ui_ChildrenForm2):
    def __init__(self):
        super(ChildrenForm,  self).__init__()
        self.setupUi(self)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
