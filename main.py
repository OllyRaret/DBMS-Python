# coding: utf-8
import dbms
import datetime

# db = DataBase()
#
# db.fill_table(db.students, open("names.txt", encoding='utf-8'))
# db.fill_table(db.tests, ["test1", "test2", "test3", "test4", "test5"])
# db.update_all()
# db.show_all()
#
# db.add(db.students, "Захаров Максим Юрьевич")
# db.add(db.students, "Лакеева Ольга Александровна")
# db.add(db.tests, "hardest_test!!!")
#
# db.delete(db.students, 2)
# db.delete(db.tests, 1)
#
# db.edit(db.students, 7, "Чичиков Павел Иванович")
# db.edit(db.tests, 4, "easiest_test)))")
# db.edit(db.tests, 2, "test5")
#
# db.show_all()
#
# db.show(db.students, 54)
# db.show(db.tests, 3)
#
# db.backup()
# db.show_all()
#
# while db.backup():
#     continue
# db.show_all()
#
# while db.go_next():
#     continue
# db.show_all()
#
#
# hpdb = DataBase()
# hpdb.fill_table(hpdb.students, open("names_more.txt", encoding='utf-8'))
# hpdb.fill_table(hpdb.tests, ["амортенция", "болтливое_зелье", "доксицид", "зелье_от_икоты",
#                              "костерост", "оборотное_зелье", "сыворотка_правды"])
# hpdb.delete(hpdb.students, 6)
# hpdb.edit(hpdb.tests, 2, "зелье_урчания_в_животе")
# hpdb.show_all()
# hpdb.backup()
# hpdb.show_all()

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from add_button_class import AddWidget
from remove_button_class import RemoveWidget
from change_button_class import ChangeWidget
from find_button_class import FindWidget
from gui import *
from dbms import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.addStack = AddWidget()
        self.addStack.signal.connect(self.addData)

        self.removeStack = RemoveWidget()
        self.removeStack.signal.connect(self.removeData)

        self.changeStack = ChangeWidget()
        self.changeStack.signal.connect(self.changeData)

        self.findStack = FindWidget()
        self.findStack.signal.connect(self.findData)

        self.db = None

        self.addButton.clicked.connect(self.addButtonClicked)
        self.removeButton.clicked.connect(self.removeButtonClicked)
        self.changeButton.clicked.connect(self.changeButtonClicked)
        self.findButton.clicked.connect(self.findButtonClicked)
        self.undoButton.clicked.connect(self.undoButtonClicked)
        self.reundoButton.clicked.connect(self.reundoButtonClicked)
        self.createButton.clicked.connect(self.createDB)
        self.openButton.clicked.connect(self.openDB)
        self.saveButton.clicked.connect(self.saveDB)

    def addButtonClicked(self):
        if self.db:
            self.addStack.show()
        else:
            self.error(1)
            return

    def removeButtonClicked(self):
        if self.db:
            self.removeStack.show()
        else:
            self.error(1)
            return

    def changeButtonClicked(self):
        if self.db:
            self.changeStack.show()
        else:
            self.error(1)
            return

    def findButtonClicked(self):
        if self.db:
            self.findStack.show()
        else:
            self.error(1)
            return

    def undoButtonClicked(self):
        if self.db:
            print("UNDO SUCCESS")
            if not (self.db.backup()):
                self.error(2)
                return
            else:
                self.db.show_all()
                self.updateTables()
        else:
            self.error(1)
            return

    def reundoButtonClicked(self):
        if self.db:
            print("REUNDO SUCCESS")
            if not self.db.go_next():
                self.error(3)
                return
            else:
                self.db.show_all()
                self.updateTables()
        else:
            self.error(1)
            return

    def addData(self, data):
        table_choice, string_data = data
        self.printForCheck(table_choice, string_data)
        if table_choice == 1:
            if len(string_data.split()) != 3:
                self.error(6)
                return
            elif not self.db.add(self.db.students, string_data):
                self.error(4)
                return
        else:
            if len(string_data.split()) != 1:
                self.error(6)
                return
            elif not self.db.add(self.db.tests, string_data):
                self.error(4)
                return
        self.db.show_all()
        self.updateTables()

    def removeData(self, data):
        table_choice, id = data
        self.printForCheck(table_choice, id)
        if len(id.split()) != 1 or not id.isdigit():
            self.error(6)
            return
        if table_choice == 1:
            if not self.db.delete(self.db.students, id):
                self.error(5)
                return
        else:
            if not self.db.delete(self.db.tests, id):
                self.error(5)
                return
        self.db.show_all()
        self.updateTables()

    def changeData(self, data):
        table_choice, id, string_data = data
        self.printForCheck(table_choice, id, string_data)
        if len(id.split()) != 1 or not id.isdigit():
            self.error(6)
            return
        if table_choice == 1:
            if len(string_data.split()) != 3:
                self.error(6)
                return
            elif not self.db.edit(self.db.students, id, string_data):
                self.error(5)
                return
        else:
            if len(string_data.split()) != 1:
                self.error(6)
                return
            elif not self.db.edit(self.db.tests, id, string_data):
                self.error(5)
                return
        self.db.show_all()
        self.updateTables()

    def findData(self, data):
        table_choice, id = data
        self.printForCheck(table_choice, id)
        if len(id.split()) != 1 or not id.isdigit():
            self.error(6)
            return
        if table_choice == 1:
            result = self.db.find(self.db.students, id)
        else:
            result = self.db.find(self.db.tests, id)
        if not result:
            self.error(5)
            return
        else:
            QMessageBox.information(self, "Результаты поиска", result, QMessageBox.Ok)
        self.updateTables()

    def createDB(self):
        self.db = DataBase()

    def openDB(self):
        filePath = str(self.getFilePath()[0])
        print(filePath)
        f = open(filePath, encoding='utf-8')
        filename = filePath.split('/')[-1]
        if filename[:2] == "DB":
            students = f.readline()
            tests = f.readline()
            testing_table = f.readline()
            self.db = DataBase(students, tests, testing_table)
        else:
            self.db = DataBase()
            self.db.fill_table(self.db.students, f)
        self.db.show_all()
        self.updateTables()

    def saveDB(self):
        if self.db:
            fileName = "DB_" + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S.txt")
            self.db.save_to_file(fileName)
        else:
            self.error(1)
            return

    def getFilePath(self):
        return QtWidgets.QFileDialog.getOpenFileName(None, "Выбрать файл", ".")

    def updateTables(self):
        if self.db.students:
            self.push_table(self.tableViewStudents, [["STUDENT_ID", "SURNAME", "NAME", "PATRONYMIC"]] + self.db.students)
            for j in range(len(self.db.students[0])):
                self.tableViewStudents.horizontalHeader().setSectionResizeMode(j, QHeaderView.Stretch)
        if self.db.tests:
            self.push_table(self.tableViewTests, [["VARIANT_ID", "PATH_TO_FILE"]] + self.db.tests)
        if self.db.testing_table:
            merged = [["FULL_NAME", "PATH_TO_FILE"]]
            for row in self.db.testing_table:
                merged.append([" ".join(self.db.students[self.db.find_by_id(self.db.students, int(row[0]))][1:]),
                               self.db.tests[self.db.find_by_id(self.db.tests, int(row[1]))][1]])
            self.push_table(self.tableViewTest, merged)
            for j in range(len(self.db.testing_table[0])):
                self.tableViewTest.horizontalHeader().setSectionResizeMode(j, QHeaderView.Stretch)

    def push_table(self, table_screen, table_db):
        table_screen.setRowCount(0)
        table_screen.setColumnCount(len(table_db[0]))
        for i in range(len(table_db)):
            rowPosition = table_screen.rowCount()
            table_screen.insertRow(rowPosition)
            for j in range(len(table_db[0])):
                table_screen.setItem(rowPosition, j, QTableWidgetItem(str(table_db[i][j])))

    def printForCheck(self, *data):
        print(data)

    def error(self, param):
        if param == 1:
            descript = "Необходимо создать или открыть базу данных!"
        elif param == 2:
            descript = "Нет более ранних версий"
        elif param == 3:
            descript = "Нет более новых версий"
        elif param == 4:
            descript = "Такой элемент уже существует"
        elif param == 5:
            descript = "Элемент не был найден в таблице"
        elif param == 6:
            descript = "Неверный формат ввода"
        else:
            descript = "Неизвестная ошибка..."
        QMessageBox.warning(self, "Внимание!", descript, QMessageBox.Ok)



if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec_()
