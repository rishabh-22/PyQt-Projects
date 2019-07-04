import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore
import psutil_test


class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.init_ui()

    def init_ui(self):
        self.show()


pids = [li['pid'] for li in psutil_test.listOfProcObjects]
names = [li['name'] for li in psutil_test.listOfProcObjects]
users = [li['username'] for li in psutil_test.listOfProcObjects]
mems = [li['vms'] for li in psutil_test.listOfProcObjects]
cpus = [li['cpu'] for li in psutil_test.listOfProcObjects]
paths = [li['path'] for li in psutil_test.listOfProcObjects]


class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        rows = psutil_test.rows
        self.form_widget = MyTable(rows, 6)
        self.setCentralWidget(self.form_widget)
        col_headers = ['Process ID', 'Process Name', 'User', 'Memory', 'CPU Usage', 'Path']
        self.form_widget.setHorizontalHeaderLabels(col_headers)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.change_values)

<<<<<<< HEAD
    def show_task(self):
        # assigning values to the respective columns from respective lists, row by row
        # i = 0
        # for (id, name, user, mem, cpu, path) in zip(pids, names, users, mems, cpus, paths):
        #     col1 = QTableWidgetItem(str(id))
        #     col2 = QTableWidgetItem(str(name))
        #     col3 = QTableWidgetItem(str(user))
        #     col4 = QTableWidgetItem(str(mem))
        #     col5 = QTableWidgetItem(str(cpu))
        #     col6 = QTableWidgetItem(str(path))
        #
        #     self.form_widget.setItem(i, 0, col1)
        #     self.form_widget.setItem(i, 1, col2)
        #     self.form_widget.setItem(i, 2, col3)
        #     self.form_widget.setItem(i, 3, col4)
        #     self.form_widget.setItem(i, 4, col5)
        #     self.form_widget.setItem(i, 5, col6)
        #
        #     i += 1
=======
        i = 0
        for (id, name, user, mem, cpu, path) in zip(pids, names, users, mems, cpus, paths):
            col1 = QTableWidgetItem(str(id))
            col2 = QTableWidgetItem(str(name))
            col3 = QTableWidgetItem(str(user))
            col4 = QTableWidgetItem(str(mem))
            col5 = QTableWidgetItem(str(cpu))
            col6 = QTableWidgetItem(str(path))

            self.form_widget.setItem(i, 0, col1)
            self.form_widget.setItem(i, 1, col2)
            self.form_widget.setItem(i, 2, col3)
            self.form_widget.setItem(i, 3, col4)
            self.form_widget.setItem(i, 4, col5)
            self.form_widget.setItem(i, 5, col6)

            i += 1
>>>>>>> 58dba02b921e1a128b72e9db56c33d8e4cd02e64

        self.show()

    @QtCore.pyqtSlot()
    def change_values(self):

        new_list = psutil_test.getListOfProcesses()
        print(new_list)
        for i, process in enumerate(new_list):
            self.form_widget.setItem(i, 0, QTableWidgetItem(str(process['pid'])))
            self.form_widget.setItem(i, 1, QTableWidgetItem(str(process['name'])))
            self.form_widget.setItem(i, 2, QTableWidgetItem(str(process['username'])))
            self.form_widget.setItem(i, 3, QTableWidgetItem(str(process['vms'])))
            self.form_widget.setItem(i, 4, QTableWidgetItem(str(process['cpu'])))
            self.form_widget.setItem(i, 5, QTableWidgetItem(str(process['path'])))

        # self.form_widget.setItem(0, 0,  QTableWidgetItem('xxxxxxxxxxxxxxxxxxx'))
        # self.form_widget.setItem(0, 1, QTableWidgetItem('xxxxxxxxxxxxxxxxxxx'))
        # self.form_widget.setItem(0, 2, QTableWidgetItem('xxxxxxxxxxxxxxxxxxx'))
        # self.form_widget.setItem(0, 3, QTableWidgetItem('xxxxxxxxxxxxxxxxxxx'))
        # self.form_widget.setItem(0, 4, QTableWidgetItem('xxxxxxxxxxxxxxxxxxx'))
        # self.form_widget.setItem(0, 5, QTableWidgetItem('xxxxxxxxxxxxxxxxxxx'))


app = QApplication(sys.argv)

task_mgr = TaskManager()

task_mgr.show_task()
task_mgr.timer.start(1000)

sys.exit(app.exec_())