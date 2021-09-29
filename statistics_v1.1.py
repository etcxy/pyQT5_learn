'''
Version 1.1
add response and handel function
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit, QMessageBox

# slot: handle function for signal
def handleCalc():
    # get salary table
    info = textEdit.toPlainText()

    # list for salary>20000 or salary<20000
    salary_above_20k = ''
    salary_below_20k = ''

    # split table and get content
    for line in info.splitlines():
        # remove ' ' and '\n'
        if not line.strip():
            continue
        # type parts: list ==> [name, salary, age]
        parts = line.split(' ')
        # remove null str in list
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'
    
    QMessageBox.about(window, 'statistics result', 
    f'''salary above 20K: \n{salary_above_20k}
    \nsalary below 20k: \n{salary_below_20k}''')


app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 300)
window.setWindowTitle('Wage statistics')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("please input salary table")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('Statistics', window)
button.move(380, 80)
# NOTE singnal: button click event
button.clicked.connect(handleCalc)

window.show()

sys.exit(app.exec_())

