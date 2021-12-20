from app.main_window import MainWindow

import sys

from PyQt5 import QtWidgets


if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: QtWidgets.QMainWindow = MainWindow()
    app.exec_()
