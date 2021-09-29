'''
Version 1.1
Realize window, text edit, button 

QApplication：
提供整个UI程序的底层管理功能，比如初始化、程序入口参数、用户事件（点击、输入、拖拽）等

后面三个控件分别对应界面的主窗口、文本框、按钮
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

if __name__ == '__main__':

    app = QApplication([])      # 初始化QApplication

    window = QMainWindow()
    # 主界面的长宽
    window.resize(500, 400)
    # move决定位置：此时主窗口在 相对屏幕左上角x=300 y=310的位置
    window.move(300, 310)
    window.setWindowTitle('薪资统计')

    # QT系统中，控件(widget)是层层嵌套的
    # 这里的window表明TextEdit的父控件对象是window
    textEdit = QPlainTextEdit(window)
    textEdit.setPlaceholderText("请输入薪资表")
    textEdit.move(10,25)
    textEdit.resize(300,350)

    button = QPushButton('统计', window)
    button.move(380,80)

    window.show()

    app.exec_()