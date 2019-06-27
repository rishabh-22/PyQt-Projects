import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem
import psutil_test


class MyTable(QTableWidget):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.init_ui()

    def init_ui(self):
        self.show()


class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        process_list = psutil_test.get_list_of_processes()
        if process_list:

            rows = len(process_list)
            self.create_widget(rows)

            # assigning values to the respective columns from respective lists, row by row
            for i, process in enumerate(process_list):

                self.form_widget.setItem(i, 0, QTableWidgetItem(str(process['pid'])))
                self.form_widget.setItem(i, 1, QTableWidgetItem(str(process['name'])))
                self.form_widget.setItem(i, 2, QTableWidgetItem(str(process['username'])))
                self.form_widget.setItem(i, 3, QTableWidgetItem(str(process['vms'])))
                self.form_widget.setItem(i, 4, QTableWidgetItem(str(process['cpu'])))
                self.form_widget.setItem(i, 5, QTableWidgetItem(str(process['path'])))
        else:
            self.create_widget(0)
        self.show()

    def create_widget(self, rows):
        self.form_widget = MyTable(rows, 6)
        self.setCentralWidget(self.form_widget)
        col_headers = ['Process ID', 'Process Name', 'User', 'Memory', 'CPU Usage', 'Path']
        self.form_widget.setHorizontalHeaderLabels(col_headers)


app = QApplication(sys.argv)
task_mgr = TaskManager()
sys.exit(app.exec_())
