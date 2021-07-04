import sys

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication

from OCR_main1 import Ui_OCR_Main
from darktheme.widget_template import DarkPalette
from qdarkstyle.light.palette import LightPalette


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_OCR_Main()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    '''file = QFile("D:\\Final-Year-Project\\BreezeStyleSheets-master\\light.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())'''
    # app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightPalette))
    window.show()

    sys.exit(app.exec())
