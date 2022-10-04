from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from remove import *


class RemoveWidget(QWidget, Remove_Form):
    signal = pyqtSignal(tuple)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.removeData)
        self.cancelButton.clicked.connect(self.close)

    def removeData(self):
        table = 1 if self.radioButton1.isChecked() else 2
        data = self.lineEdit.text()
        self.signal.emit((table, data))
        self.lineEdit.clear()
        self.close()
