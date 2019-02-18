import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
import design


class Connect(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        lst = []
        int_val = QIntValidator()
        for widget in self.findChildren(QtWidgets.QLineEdit):
            if not widget.isReadOnly():
                widget.setValidator(int_val)
                widget.textChanged.connect(self.debug_output)
                lst.append(widget)
            
    def debug_output(self):
        sender = self.sender()
        print('debug output ',sender.text())


app = QtWidgets.QApplication(sys.argv)
window = Connect()
window.show()
app.exec_()
