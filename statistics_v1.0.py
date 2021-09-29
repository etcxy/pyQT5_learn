'''
Version 1.0
Realize window, text edit, button 

QApplication：
提供整个UI程序的底层管理功能，比如初始化、程序入口参数、用户事件（点击、输入、拖拽）等

后面三个控件分别对应界面的主窗口、文本框、按钮
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit

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

    # 放在主窗口的控件，要能全部显示在界面上，必须show一下
    window.show()

    # app.exec_()是QApplication类的方法
    # 它的作用是 进入程序的主循环知道exit()被调用
    # app.exec_()
    # 建议使用下面这种方式
    sys.exit(app.exec_())