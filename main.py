import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator

import design
from calculate import get_name, get_corner


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        for widget in self.findChildren(QtWidgets.QLineEdit):
            if not widget.isReadOnly():
                val = QIntValidator(0, int(widget.whatsThis()))
                widget.setValidator(val)
                
        self.pushButton.clicked.connect(self.callback)

    def callback(self):
        values = (self.get_coord(0), self.get_coord(1),
                  self.get_scale(), self.get_hemisphere())
        self.lineEdit_7.setText(get_name(*values))
        
        lst = (self.lineEdit_8, self.lineEdit_11, self.lineEdit_9, self.lineEdit_10)
        for index in range(0,4):
            coord =  get_corner(*values, index)
            deg = coord // 60
            min = coord - deg * 60
            sec = (min - int(min)) * 60
            lst[index].setText(f'{int(deg)}° {int(min)}′ {round(sec)}′′')

    def get_coord(self, param):
        if param:
            lst = [self.lineEdit_4.text(),
                   self.lineEdit_5.text(),
                   self.lineEdit_6.text()]
        else:
            lst = [self.lineEdit.text(),
                   self.lineEdit_2.text(),
                   self.lineEdit_3.text()]
        for x in range(len(lst)):
            if lst[x] == '':
                lst[x] = 0
        return int(lst[0]) * 60 + int(lst[1]) + float(lst[2]) / 60

    def get_scale(self):
        scale = self.comboBox_2.currentText()[3:]
        for index in range(0, len(scale) - 3):
            if scale[index] == ' ':
               scale = scale[:index] + scale[index + 1:]
        return int(scale)

    def get_hemisphere(self):
        return {'NE': 0, 'NW': 1, 'SE': 2, 'SW': 3}[self.comboBox.currentText()]
    
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
