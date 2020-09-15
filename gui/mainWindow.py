# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from aboutWindow import Ui_aboutWidget
import LUFSWidget
import controller
import normalization
import os
import math
import pyqtgraph as qtPlot
from pyqtgraph import PlotWidget

inputAudioFileName = ""
targetLUFS = -23.0


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(795, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.waveFormPlotBefore = QtWidgets.QTabWidget(self.centralwidget)
        self.waveFormPlotBefore.setObjectName("waveFormPlotBefore")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelFileName = QtWidgets.QLabel(self.tab)
        self.labelFileName.setObjectName("labelFileName")
        self.horizontalLayout.addWidget(self.labelFileName)
        self.labelFileNameValue = QtWidgets.QLabel(self.tab)
        self.labelFileNameValue.setObjectName("labelFileNameValue")
        self.horizontalLayout.addWidget(self.labelFileNameValue)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 15)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            1, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.formLayout.setObjectName("formLayout")
        self.label_RMS = QtWidgets.QLabel(self.groupBox)
        self.label_RMS.setObjectName("label_RMS")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_RMS)
        self.label_RMSvalue = QtWidgets.QLabel(self.groupBox)
        self.label_RMSvalue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_RMSvalue.setObjectName("label_RMSvalue")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_RMSvalue)
        self.label_LUFS = QtWidgets.QLabel(self.groupBox)
        self.label_LUFS.setObjectName("label_LUFS")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_LUFS)
        self.label_LUFSvalue = QtWidgets.QLabel(self.groupBox)
        self.label_LUFSvalue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_LUFSvalue.setObjectName("label_LUFSvalue")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_LUFSvalue)
        self.label_LUFS2 = QtWidgets.QLabel(self.groupBox)
        self.label_LUFS2.setObjectName("label_LUFS2")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_LUFS2)
        self.label_LUFS2value = QtWidgets.QLabel(self.groupBox)
        self.label_LUFS2value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_LUFS2value.setObjectName("label_LUFS2value")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_LUFS2value)
        self.label_LU = QtWidgets.QLabel(self.groupBox)
        self.label_LU.setObjectName("label_LU")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_LU)
        self.label_LUvalue = QtWidgets.QLabel(self.groupBox)
        self.label_LUvalue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_LUvalue.setObjectName("label_LUvalue")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.label_LUvalue)

        self.lufsWidget = LUFSWidget.LUFSWidget()
        self.lufsWidget.setMinimumWidth(85)
        self.lufsWidget.setMinimumHeight(320)
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.lufsWidget)
        self.lufsWidget.setPos(0)
        self.verticalLayout_5.addLayout(self.formLayout)

        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(2, 2, 2, 2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_RMSrec = QtWidgets.QLabel(self.groupBox_2)
        self.label_RMSrec.setObjectName("label_RMSrec")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_RMSrec)
        self.label_LUFSrec = QtWidgets.QLabel(self.groupBox_2)
        self.label_LUFSrec.setObjectName("label_LUFSrec")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_LUFSrec)
        self.label_LUFS2rec = QtWidgets.QLabel(self.groupBox_2)
        self.label_LUFS2rec.setObjectName("label_LUFS2rec")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_LUFS2rec)
        self.label_LUrec = QtWidgets.QLabel(self.groupBox_2)
        self.label_LUrec.setObjectName("label_LUrec")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_LUrec)
        self.label_RMSrecValue = QtWidgets.QLabel(self.groupBox_2)
        self.label_RMSrecValue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_RMSrecValue.setObjectName("label_RMSrecValue")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_RMSrecValue)
        self.label_LUFSrecValue = QtWidgets.QLabel(self.groupBox_2)
        self.label_LUFSrecValue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_LUFSrecValue.setObjectName("label_LUFSrecValue")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_LUFSrecValue)
        self.label_LUFS2recValue = QtWidgets.QLabel(self.groupBox_2)
        self.label_LUFS2recValue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_LUFS2recValue.setObjectName("label_LUFS2recValue")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_LUFS2recValue)
        self.label_LUrecValue = QtWidgets.QLabel(self.groupBox_2)
        self.label_LUrecValue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_LUrecValue.setObjectName("label_LUrecValue")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_LUrecValue)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.normalizeLevelValue = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.normalizeLevelValue.setObjectName("normalizeLevelValue")
        self.verticalLayout_4.addWidget(self.normalizeLevelValue)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.waveFormPlotBefore.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.histgrammPlotBefore = PlotWidget(self.tab_2)
        self.histgrammPlotBefore.setObjectName("histgrammPlotBefore")
        self.verticalLayout_7.addWidget(self.histgrammPlotBefore)
        self.histgrammPlotAfter = PlotWidget(self.tab_2)
        self.histgrammPlotAfter.setObjectName("histgrammPlotAfter")
        self.verticalLayout_7.addWidget(self.histgrammPlotAfter)
        self.waveFormPlotBefore.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphicsView_3 = PlotWidget(self.tab_3)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_8.addWidget(self.graphicsView_3)
        self.waveFormPlotAfter = PlotWidget(self.tab_3)
        self.waveFormPlotAfter.setObjectName("waveFormPlotAfter")
        self.verticalLayout_8.addWidget(self.waveFormPlotAfter)
        self.waveFormPlotBefore.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.waveFormPlotBefore)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_openFile = QtWidgets.QAction(mainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/document-open.svg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_openFile.setIcon(icon)
        self.action_openFile.setIconVisibleInMenu(True)
        self.action_openFile.setObjectName("action_openFile")
        self.action_saveAs = QtWidgets.QAction(mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/newPrefix/document-save-as.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_saveAs.setIcon(icon1)
        self.action_saveAs.setObjectName("action_saveAs")
        self.action_normalize = QtWidgets.QAction(mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/player-volume.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_normalize.setIcon(icon2)
        self.action_normalize.setObjectName("action_normalize")
        self.action_about = QtWidgets.QAction(mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/help-about.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon3)
        self.action_about.setObjectName("action_about")
        self.toolBar.addAction(self.action_openFile)
        self.toolBar.addAction(self.action_saveAs)
        self.toolBar.addAction(self.action_normalize)
        self.toolBar.addAction(self.action_about)

        self.normalizeLevelValue.setMaximum(0.0)
        self.normalizeLevelValue.setMinimum(-60.0)
        self.normalizeLevelValue.setValue(-23.0)

        self.retranslateUi(mainWindow)
        self.waveFormPlotBefore.setCurrentIndex(0)
        self.action_about.triggered.connect(self.showAboutWindow)
        self.normalizeLevelValue.valueChanged['double'].connect(
            self.normalizeValueChanged)
        self.action_normalize.triggered.connect(self.startNormalize)
        self.action_saveAs.triggered.connect(self.fileSaveAs)
        self.action_openFile.triggered.connect(self.openFile)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def showAboutWindow(self):
        self.aboutWidget = QtWidgets.QWidget()
        self.ui = Ui_aboutWidget()
        self.ui.setupUi(self.aboutWidget)
        self.aboutWidget.show()

    def openFile(self):
        widgetFO = QtWidgets.QWidget()
        filename = QtWidgets.QFileDialog.getOpenFileName(
            widgetFO, 'Open File', '~', "Audio *.wav files (*.wav)")
        widgetFO.show()
        global inputAudioFileName
        inputAudioFileName = filename[0]
        #check  exist file
        if ((len(filename[0])) > 0):
            try:
                file = open(inputAudioFileName)
            except IOError as e:
                print(u'не удалось открыть файл. Причина: '+str(e))
                widgetMB = QtWidgets.QWidget()
                QtWidgets.QMessageBox.about(widgetMB, "Ошибка", "Не удалось открыть файл!")
            else:
                with file:
                    #dialog
                    self.labelFileNameValue.setText(inputAudioFileName)
                    print(filename[0])
                    self.contr = controller.Controller(filename[0])
                    integratedLoudnessValue, luValue, rmsPeak = self.contr.getAudioInfo()
                    #self.label_LUvalue.setText(luValue)
                    self.lufsWidget.setPos(float(integratedLoudnessValue))
                    self.label_LUFSvalue.setText(integratedLoudnessValue)
                    self.label_RMSvalue.setText(rmsPeak)


    def printChar(self,plot,xArray, yArray):

        #win = qtPlot.GraphicsWindow()
        #win.setWindowTitle('Audio plot')
        xdict = dict(enumerate(yArray))
        #bg1 = qtPlot.BarGraphItem(x=xArray,y1=300, width=0.5, brush='r')
        stringAxis = qtPlot.AxisItem(orientation='bottom')
        xtickts = [list(xdict.items())[::math.ceil(len(xArray)/10)]]
        stringAxis.setTicks(xtickts)
        #plot = win.addPlot(axisItems={'bottom': stringAxis})
        plot.setXRange(0, len(xArray), padding=0)
        #plot.setYRange(min(xArray), max(xArray), padding=0)
        plot.setYRange(-32768, 32768, padding=0)
        curve = plot.plot(list(xdict.keys()),
                          xArray)
        curve.setPen(qtPlot.mkPen(width=1, color=(0, 0, 0)))

    def printBarChar(self,plot,xDict):
        x = list(xDict.keys())
        y1 = list(xDict.values())
        stringAxis = qtPlot.AxisItem(orientation='bottom')
        curve = plot.plot(x,
                          y1)
        curve.setPen(qtPlot.mkPen(width=1, color=(0, 0, 0)))

    def printRealBarChar(self,plot,xDict):
        x1 = list(xDict.keys())
        y1 = list(xDict.values())
        stringAxis = qtPlot.AxisItem(orientation='bottom')
        
        bg1 = qtPlot.BarGraphItem(x=x1,
                          height=y1,width=0.6)
        plot.addItem(bg1)
        #curve.setPen(qtPlot.mkPen(width=1, color=(0, 0, 0)))

    def startNormalize(self):
        try:
            self.normalizer= normalization.Normalization(inputAudioFileName, targetLUFS)
            self.normalizer.normalize(inputAudioFileName, targetLUFS)

            self.printBarChar(self.histgrammPlotBefore,self.normalizer.histogramm)
            self.printBarChar(self.histgrammPlotAfter,self.normalizer.histogramm2)
            self.printChar(self.graphicsView_3,self.normalizer.plotSamplesArray1,self.normalizer.yArray1)
            self.printChar(self.waveFormPlotAfter,self.normalizer.plotSamplesArray2,self.normalizer.yArray2)
        except Exception as e:
            widgetMB = QtWidgets.QWidget()
            QtWidgets.QMessageBox.about(widgetMB, "Ошибка", "Не удалось нормализовать файл! Ошибка: "+str(e))

    def fileSaveAs(self):
        try:
            fullFilePath = os.path.dirname(sys.argv[0])+"/../audio/output.wav"
            file = open(fullFilePath)
        except IOError as e:
            print(u'Не удалось открыть файл. Причина: '+str(e))
            widgetMB = QtWidgets.QWidget()
            QtWidgets.QMessageBox.about(widgetMB, "Ошибка", "Не удалось сохранить файл!")
        else:
            with file:
                #dialog
                widgetFO = QtWidgets.QWidget()
                filename = QtWidgets.QFileDialog.getSaveFileName(
                widgetFO, 'Save File', 'output.wav', "Audio *.wav files (*.wav)")
                widgetFO.show()
                #move file
                os.rename(fullFilePath, filename[0])

    def normalizeValueChanged(self, double):
        global targetLUFS
        targetLUFS = double
        print("value changed {0}".format(double))

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "SoundNormalizer"))
        self.labelFileName.setText(_translate("mainWindow", "Файл: "))
        self.labelFileNameValue.setText(_translate("mainWindow", "не выбран"))
        self.groupBox.setTitle(_translate(
            "mainWindow", "Информация о файле (до нормализации)"))
        self.label_RMS.setText(_translate("mainWindow", "RMS: "))
        self.label_RMSvalue.setText(_translate("mainWindow", "0.0"))
        self.label_LUFS.setText(_translate("mainWindow", "LUFS: "))
        self.label_LUFSvalue.setText(_translate("mainWindow", "0.0"))
        #self.label_LUFS2.setText(_translate("mainWindow", "LUFS2:"))
        #self.label_LUFS2value.setText(_translate("mainWindow", "0.0"))
        #self.label_LU.setText(_translate("mainWindow", "LU:"))
        #self.label_LUvalue.setText(_translate("mainWindow", "0.0"))
        self.groupBox_2.setTitle(_translate(
            "mainWindow", "Рекомендуемые параметры:"))
        self.label_RMSrec.setText(_translate("mainWindow", "RMS:"))
        self.label_LUFSrec.setText(_translate("mainWindow", "LUFS:"))
        #self.label_LUFS2rec.setText(_translate("mainWindow", "LUFS2:"))
        #self.label_LUrec.setText(_translate("mainWindow", "LU:"))
        self.label_RMSrecValue.setText(_translate("mainWindow", "< -1.0"))
        self.label_LUFSrecValue.setText(_translate("mainWindow", "-23.0 ± 1.0"))
        #self.label_LUFS2recValue.setText(_translate("mainWindow", "0.0"))
       #self.label_LUrecValue.setText(_translate("mainWindow", "-1.0"))
        self.groupBox_3.setTitle(_translate(
            "mainWindow", "Настройка нормализации"))
        self.label_2.setText(_translate(
            "mainWindow", "Требуемый уровень громкости:"))
        self.waveFormPlotBefore.setTabText(self.waveFormPlotBefore.indexOf(
            self.tab), _translate("mainWindow", "Главная"))
        self.waveFormPlotBefore.setTabText(self.waveFormPlotBefore.indexOf(
            self.tab_2), _translate("mainWindow", "Гистограммы"))
        self.waveFormPlotBefore.setTabText(self.waveFormPlotBefore.indexOf(
            self.tab_3), _translate("mainWindow", "Звуковая волна"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.action_openFile.setText(_translate("mainWindow", "Открыть"))
        self.action_saveAs.setText(_translate("mainWindow", "Сохранить как"))
        self.action_normalize.setText(
            _translate("mainWindow", "Нормализовать"))
        self.action_about.setText(_translate("mainWindow", "О программе"))



import resources.res

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
