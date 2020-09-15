from PyQt5 import QtCore, QtGui, QtWidgets
from mainWindow import Ui_mainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_mainWindow()
    ui.show()
    sys.exit(app.exec_())
