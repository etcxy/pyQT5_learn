'''
Version 1.2
Encapsulating into class
optimize some sentence
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit,QMessageBox

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('salary statistics')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("please input salary table")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('statistics', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.textEdit.toPlainText()

        salary_above_20k = ''
        salary_below_20k = ''

        for line in info.splitlines():
            line = line.strip()
            parts = [p for p in line.split(' ') if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'
        
        QMessageBox.about(self.window, 'statistics result', 
        f'''salary above 20K: \n{salary_above_20k}
        \nsalary below 20k: \n{salary_below_20k}''')

if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.window.show()
    sys.exit(app.exec_())
