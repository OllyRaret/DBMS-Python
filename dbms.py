from random import randint


class DataBase:
    def __init__(self, students=None, tests=None, testing_table=None):
        self.students = []
        if students is not None:
            students = students.split()
            for i in range(len(students)//3):
                self.students.append((f"{i + 1} " + ' '.join(students[3*i:(3*i+3)])).split())
        self.tests = []
        if tests is not None:
            tests = tests.split()
            for i in range(len(tests)):
                self.tests.append([str(i+1), tests[i]])
        self.testing_table = []
        if testing_table is not None:
            testing_table = testing_table.split()
            for i in range(len(testing_table)):
                self.testing_table.append([str(i+1), testing_table[i]])
        self.bckup = DoubleLink()

    def fill_table(self, table, source):
        i = 1
        for str in source:
            table.append((f"{i} " + str).split())
            i += 1

    def relate_tables(self):
        self.testing_table.clear()
        for el_1 in self.students:
            j = randint(0, len(self.tests) - 1)
            self.testing_table.append([el_1[0], self.tests[j][0]])

    def export_testing_table(self, filename):
        f = open(filename, "w")
        for row in self.testing_table:
            f.write(" ".join(row) + "\n")

    def print_table(self, data, cell_sep=' | ', header_separator=True):
        rows = len(data)
        cols = len(data[0])

        col_width = []
        for col in range(cols):
            columns = [data[row][col] for row in range(rows)]
            col_width.append(len(max(columns, key=len)))

        separator = "-+-".join('-' * n for n in col_width)

        for i, row in enumerate(range(rows)):
            if i == 1 and header_separator:
                print(separator)

            result = []
            for col in range(cols):
                item = data[row][col].center(col_width[col])
                result.append(item)

            print(cell_sep.join(result))
        print()

    def print_testing_table_by_id(self):
        merged = [["FULL_NAME", "PATH_TO_FILE"]]
        for row in self.testing_table:
            merged.append([" ".join(self.students[self.find_by_id(self.students, int(row[0]))][1:]),
                           self.tests[self.find_by_id(self.tests, int(row[1]))][1]])
        self.print_table(merged)

    def update_all(self):
        if len(self.students) > 0 and len(self.tests) > 0:
            self.relate_tables()
            self.export_testing_table("testing_table.txt")

    def show_all(self):
        self.print_table([["STUDENT_ID", "SURNAME", "NAME", "PATRONYMIC"], *self.students])
        self.print_table([["VARIANT_ID", "PATH_TO_FILE"], *self.tests])
        self.print_testing_table_by_id()

    def add(self, table, data):
        if not self.unique(table, data):
            print(f"Строка {data} уже существует!\n")
            return False
        if len(table) == 0:
            table.append(("1 " + data).split())
        else:
            self.bckup.insert_at_start(self.students, self.tests, self.testing_table)
            table.append((f"{int(table[-1][0]) + 1} " + data).split())
        self.update_all()
        return True

    def delete(self, table, key):
        if len(table) == 0:
            print("Таблица уже пуста!\n")
            return False
        self.bckup.insert_at_start(self.students, self.tests, self.testing_table)
        ind = self.find_by_id(table, int(key))
        if ind != -1:
            table.pop(ind)
            if len(table) == 0:
                self.testing_table = []
                return True
            self.update_all()
            return True
        else:
            return False

    def find_by_id(self, table, key):
        for ind in range(len(table)):
            if int(table[ind][0]) == int(key):
                return ind
            if int(table[ind][0]) > int(key):
                print("Попытка найти несуществующий элемент")
                return -1

    def find(self, table, key):
        for ind in range(len(table)):
            if int(table[ind][0]) == int(key):
                return ' '.join(table[ind])
            if int(table[ind][0]) > int(key):
                print("Попытка найти несуществующий элемент")
                return None

    def edit(self, table, id, new_data):
        if not self.unique(table, new_data):
            print(f"Строка {new_data} уже существует!\n")
            return False
        row = self.find_by_id(table, int(id))
        if row == -1:
            return False
        self.bckup.insert_at_start(self.students, self.tests, self.testing_table)
        table[row] = (table[row][0] + " " + new_data).split()
        self.update_all()
        return True

    # def show(self, table, id):
    #     row = self.find_by_id(table, id)
    #     for i in range(1, len(table[0]) - 1):
    #         print(f"{table[row][i]} | ", end="")
    #     print(table[row][-1], "\n")
    #     return ' '.join(table[row][1:])

    def unique(self, table, data):
        if len(table) == 0:
            return True
        for elem in table:
            if " ".join(elem[1:]) == data:
                return False
        return True

    def backup(self):
        if not self.bckup.start_node:
            print("Нет более ранних версий\n")
            return False
        if self.bckup.start_node.prev is None:
            self.bckup.insert_at_start(self.students, self.tests, self.testing_table)
        if self.bckup.start_node.next is not None:
            self.students, self.tests, self.testing_table = self.bckup.backup()
            self.export_testing_table("testing_table.txt")
            return True
        else:
            print("Нет более ранних версий\n")
            return False

    def go_next(self):
        if not self.bckup.start_node:
            print("Нет более новых версий\n")
            return False
        if self.bckup.start_node.prev is not None:
            self.students, self.tests, self.testing_table = self.bckup.go_next()
            self.export_testing_table("testing_table.txt")
            return True
        else:
            print("Нет более новых версий\n")
            return False

    def save_to_file(self, filename):
        f = open(filename, 'w', encoding='utf-8')
        for i in range(len(self.students)):
            f.write(' '.join(self.students[i][1:]) + ' ')
        f.write('\n')
        for i in range(len(self.tests)):
            f.write(self.tests[i][1] + ' ')
        f.write('\n')
        for i in range(len(self.testing_table)):
            f.write(self.testing_table[i][1] + ' ')


class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLink(object):
    def __init__(self):
        self.start_node = None

    def insert_at_start(self, students, tests, testing_table):
        if self.start_node is not None:
            self.delete_prev()
        if self.start_node is None:
            new_node = Node([students.copy(), tests.copy(), testing_table.copy()])
            self.start_node = new_node
            return
        new_node = Node([students.copy(), tests.copy(), testing_table.copy()])
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def delete_prev(self):
        self.start_node.prev = None

    def backup(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return self.start_node
        if self.start_node.next is None:
            # self.start_node = None
            return self.start_node.data
        self.start_node = self.start_node.next
        # self.start_node.prev = None
        return self.start_node.data

    def go_next(self):
        self.start_node = self.start_node.prev
        return self.start_node.data
