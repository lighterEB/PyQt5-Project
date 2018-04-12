import sys
from PyQt5.QtWidgets import QMainWindow,  QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400,  200)
        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示", 5000)
        self.setWindowTitle("万事开头难")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/conections.ico"))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
