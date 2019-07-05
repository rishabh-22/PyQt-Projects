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

    @QtCore.pyqtSlot()
    def change_values(self):

        new_list = psutil_test.getListOfProcesses()
        self.form_widget.setRowCount(len(new_list))
        print(new_list)

        for i, process in enumerate(new_list):
            self.form_widget.setItem(i, 0, QTableWidgetItem(str(process['pid'])))
            self.form_widget.setItem(i, 1, QTableWidgetItem(str(process['name'])))
            self.form_widget.setItem(i, 2, QTableWidgetItem(str(process['username'])))
            self.form_widget.setItem(i, 3, QTableWidgetItem(str(process['vms'])))
            self.form_widget.setItem(i, 4, QTableWidgetItem(str(process['cpu'])))
            self.form_widget.setItem(i, 5, QTableWidgetItem(str(process['path'])))


app = QApplication(sys.argv)

task_mgr = TaskManager()

task_mgr.show()
task_mgr.timer.start(1000)

sys.exit(app.exec_())
