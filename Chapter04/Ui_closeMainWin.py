# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5Project\Chapter04\closeMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_closeMainWin(object):
    def setupUi(self, closeMainWin):
        closeMainWin.setObjectName("closeMainWin")
        closeMainWin.resize(348, 101)
        self.pushButton = QtWidgets.QPushButton(closeMainWin)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 301, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(closeMainWin)
        QtCore.QMetaObject.connectSlotsByName(closeMainWin)

    def retranslateUi(self, closeMainWin):
        _translate = QtCore.QCoreApplication.translate
        closeMainWin.setWindowTitle(_translate("closeMainWin", "Form"))
        self.pushButton.setText(_translate("closeMainWin", "关闭主窗口"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    closeMainWin = QtWidgets.QWidget()
    ui = Ui_closeMainWin()
    ui.setupUi(closeMainWin)
    closeMainWin.show()
    sys.exit(app.exec_())

