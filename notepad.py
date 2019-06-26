import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QHBoxLayout, QAction, qApp


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)

        self.show()

    def save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            with open(fileName, 'w') as f:
                my_text = self.text.toPlainText()
                f.write(my_text)

    def open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            with open(fileName, 'r') as f:
                file_text = f.read()
                self.text.setText(file_text)

    def clear(self):
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

        find_action = QAction('Find', self)

        replace_action = QAction('Replace', self)

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
            self.form_widget.clear()
        elif signal == '&Open':
            self.form_widget.open()
        elif signal == '&Save':
            self.form_widget.save()


app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())
