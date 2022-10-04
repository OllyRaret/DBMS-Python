from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from change import *


class ChangeWidget(QWidget, Change_Form):
    signal = pyqtSignal(tuple)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.changeData)
        self.cancelButton.clicked.connect(self.close)

    def changeData(self):
        table = 1 if self.radioButton1.isChecked() else 2
        id = self.idlineEdit.text()
        data = self.datalineEdit.text()
        self.signal.emit((table, id, data))
        self.close()
        self.idlineEdit.clear()
        self.datalineEdit.clear()
