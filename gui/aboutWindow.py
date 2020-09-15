# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutWidget(object):
    def setupUi(self, aboutWidget):
        aboutWidget.setObjectName("aboutWidget")
        aboutWidget.resize(338, 142)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutWidget.sizePolicy().hasHeightForWidth())
        aboutWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(aboutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(aboutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(aboutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(aboutWidget)
        self.pushButton.clicked.connect(aboutWidget.close)
        QtCore.QMetaObject.connectSlotsByName(aboutWidget)

    def retranslateUi(self, aboutWidget):
        _translate = QtCore.QCoreApplication.translate
        aboutWidget.setWindowTitle(_translate("aboutWidget", "Form"))
        self.label.setText(_translate("aboutWidget", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Sound Normalizer</span></p><p align=\"center\">Программа для нормализации аудио файлов.</p><p align=\"center\">Автор: Устин Антон Михайлович<br/>2018 год</p></body></html>"))
        self.pushButton.setText(_translate("aboutWidget", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutWidget = QtWidgets.QWidget()
    ui = Ui_aboutWidget()
    ui.setupUi(aboutWidget)
    aboutWidget.show()
    sys.exit(app.exec_())

