# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 0, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 0, 1, 1, 1)
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setObjectName("changeButton")
        self.gridLayout.addWidget(self.changeButton, 0, 2, 1, 1)
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setObjectName("findButton")
        self.gridLayout.addWidget(self.findButton, 0, 3, 1, 1)


        self.tableViewStudents = QtWidgets.QTableWidget(self.centralwidget)
        self.tableViewStudents.setObjectName("tableViewStudents")
        self.gridLayout.addWidget(self.tableViewStudents, 1, 3, 2, 3)

        self.tableViewTest = QtWidgets.QTableWidget(self.centralwidget)
        self.tableViewTest.setObjectName("tableViewTest")
        self.gridLayout.addWidget(self.tableViewTest, 1, 0, 1, 3)

        self.tableViewTests = QtWidgets.QTableWidget(self.centralwidget)
        self.tableViewTests.setObjectName("tableViewTests")
        self.gridLayout.addWidget(self.tableViewTests, 2, 0, 1, 3)


        self.undoButton = QtWidgets.QPushButton(self.centralwidget)
        self.undoButton.setObjectName("undoButton")
        self.gridLayout.addWidget(self.undoButton, 3, 4, 1, 1)
        self.reundoButton = QtWidgets.QPushButton(self.centralwidget)
        self.reundoButton.setObjectName("reundoButton")
        self.gridLayout.addWidget(self.reundoButton, 3, 5, 1, 1)
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.gridLayout.addWidget(self.createButton, 3, 0, 1, 1)
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setObjectName("openButton")
        self.gridLayout.addWidget(self.openButton, 3, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataBase"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.removeButton.setText(_translate("MainWindow", "Удалить"))
        self.changeButton.setText(_translate("MainWindow", "Измненить"))
        self.findButton.setText(_translate("MainWindow", "Найти"))
        self.undoButton.setText(_translate("MainWindow", "Undo"))
        self.reundoButton.setText(_translate("MainWindow", "ReUndo"))
        self.createButton.setText(_translate("MainWindow", "Создать"))
        self.openButton.setText(_translate("MainWindow", "Открыть"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
