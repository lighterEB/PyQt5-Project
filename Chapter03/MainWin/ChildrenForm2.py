# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5Project\Chapter03\MainWin\ChildrenForm2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildrenForm2(object):
    def setupUi(self, ChildrenForm2):
        ChildrenForm2.setObjectName("ChildrenForm2")
        ChildrenForm2.resize(359, 276)
        self.textEdit = QtWidgets.QTextEdit(ChildrenForm2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 341, 261))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ChildrenForm2)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm2)

    def retranslateUi(self, ChildrenForm2):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm2.setWindowTitle(_translate("ChildrenForm2", "Form"))
        self.textEdit.setHtml(_translate("ChildrenForm2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">我是子窗口的内容</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChildrenForm2 = QtWidgets.QWidget()
    ui = Ui_ChildrenForm2()
    ui.setupUi(ChildrenForm2)
    ChildrenForm2.show()
    sys.exit(app.exec_())

