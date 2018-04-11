import sys
from PyQt5.QtWidgets import QPushButton, QApplication,  QWidget

class WinForm( QWidget):
    def __init__(self,  parent = None):
        super(WinForm, self).__init__()
        self.setGeometry(300,  300,  300,  350)
        self.setWindowTitle('点击按钮关闭窗口')
        quit = QPushButton('点了就是我儿子', self)
        quit.setGeometry(10, 10, 100, 100)
        quit.setStyleSheet("background-color: red")
        quit.clicked.connect(self.close)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
        
    
