# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5Project\Chapter03\MainWindowSignalSlog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.closeWinBth = QtWidgets.QPushButton(Form)
        self.closeWinBth.setGeometry(QtCore.QRect(150, 110, 81, 31))
        self.closeWinBth.setObjectName("closeWinBth")

        self.retranslateUi(Form)
        self.closeWinBth.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.closeWinBth.setText(_translate("Form", "关闭窗口"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

