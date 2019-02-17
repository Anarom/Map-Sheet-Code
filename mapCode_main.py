import design
import sys
from PyQt5 import QtWidgets

class Connect(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = Connect()
window.show()
app.exec_()
