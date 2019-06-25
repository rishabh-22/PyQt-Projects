import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getcwd())
        print(os.getcwd())
        print('filename', filename)
        print('filename[0]', filename[0])
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getcwd())
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()


class Writer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        find_action = QAction('Find...', self)

        replace_action = QAction('Replace...', self)

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)
        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)

        self.setWindowTitle('Text Editor')
        self.show()

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == 'New':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()


app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())
