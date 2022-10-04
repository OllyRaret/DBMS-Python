from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from find import *


class FindWidget(QWidget, Find_Form):
    signal = pyqtSignal(tuple)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.addData)
        self.closeButton.clicked.connect(self.close)

    def addData(self):
        table = 1 if self.radioButton1.isChecked() else 2
        data = self.idlineEdit.text()
        self.signal.emit((table, data))
        self.idlineEdit.clear()
        self.close()
