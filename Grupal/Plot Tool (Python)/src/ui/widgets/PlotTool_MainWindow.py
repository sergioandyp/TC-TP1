# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from src.ui.widgets.PlotWidget import PlotWidget
from PlotWidget import PlotWidget


class PlotTool_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(913, 801)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 750))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(-1, 2, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tituloT = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tituloT.sizePolicy().hasHeightForWidth())
        self.tituloT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.tituloT.setFont(font)
        self.tituloT.setScaledContents(False)
        self.tituloT.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloT.setWordWrap(False)
        self.tituloT.setObjectName("tituloT")
        self.verticalLayout_7.addWidget(self.tituloT)
        self.horizontalWidget_10 = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_10.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_10.setSizePolicy(sizePolicy)
        self.horizontalWidget_10.setObjectName("horizontalWidget_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalWidget_10)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.checkFase = QtWidgets.QCheckBox(self.horizontalWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkFase.sizePolicy().hasHeightForWidth())
        self.checkFase.setSizePolicy(sizePolicy)
        self.checkFase.setChecked(True)
        self.checkFase.setObjectName("checkFase")
        self.horizontalLayout_13.addWidget(self.checkFase)
        self.checkAmplitud = QtWidgets.QCheckBox(self.horizontalWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkAmplitud.sizePolicy().hasHeightForWidth())
        self.checkAmplitud.setSizePolicy(sizePolicy)
        self.checkAmplitud.setChecked(True)
        self.checkAmplitud.setObjectName("checkAmplitud")
        self.horizontalLayout_13.addWidget(self.checkAmplitud)
        self.checkRespuesta = QtWidgets.QCheckBox(self.horizontalWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkRespuesta.sizePolicy().hasHeightForWidth())
        self.checkRespuesta.setSizePolicy(sizePolicy)
        self.checkRespuesta.setChecked(True)
        self.checkRespuesta.setObjectName("checkRespuesta")
        self.horizontalLayout_13.addWidget(self.checkRespuesta)
        self.verticalLayout_7.addWidget(self.horizontalWidget_10)
        self.horizontalWidget_9 = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_9.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_9.setSizePolicy(sizePolicy)
        self.horizontalWidget_9.setObjectName("horizontalWidget_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalWidget_9)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.radioButtonF = QtWidgets.QRadioButton(self.horizontalWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonF.sizePolicy().hasHeightForWidth())
        self.radioButtonF.setSizePolicy(sizePolicy)
        self.radioButtonF.setChecked(True)
        self.radioButtonF.setObjectName("radioButtonF")
        self.horizontalLayout_12.addWidget(self.radioButtonF)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_12.addWidget(self.radioButton)
        self.verticalLayout_7.addWidget(self.horizontalWidget_9)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalWidget_4 = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_4.sizePolicy().hasHeightForWidth())
        self.verticalWidget_4.setSizePolicy(sizePolicy)
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.listWidget = QtWidgets.QListWidget(self.verticalWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.listWidget.setMouseTracking(False)
        self.listWidget.setAcceptDrops(False)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        self.verticalLayout_8.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.verticalWidget_4)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalWidget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_3.sizePolicy().hasHeightForWidth())
        self.verticalWidget_3.setSizePolicy(sizePolicy)
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnH = QtWidgets.QPushButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnH.sizePolicy().hasHeightForWidth())
        self.btnH.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnH.setFont(font)
        self.btnH.setStyleSheet("background-color: rgb(14, 51, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: 30px;\n"
"min-height: 100px;\n"
"min-width:160px;\n"
"max-width:160px;")
        self.btnH.setObjectName("btnH")
        self.horizontalLayout_2.addWidget(self.btnH)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnSpice = QtWidgets.QPushButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSpice.sizePolicy().hasHeightForWidth())
        self.btnSpice.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnSpice.setFont(font)
        self.btnSpice.setStyleSheet("background-color: rgb(14, 51, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: 30px;\n"
"min-height: 100px;\n"
"min-width:160px;\n"
"max-width:160px;")
        self.btnSpice.setObjectName("btnSpice")
        self.horizontalLayout_8.addWidget(self.btnSpice)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnMedicion = QtWidgets.QPushButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMedicion.sizePolicy().hasHeightForWidth())
        self.btnMedicion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnMedicion.setFont(font)
        self.btnMedicion.setStyleSheet("background-color: rgb(14, 51, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: 20px;\n"
"min-height: 100px;\n"
"min-width:160px;\n"
"max-width:160px;")
        self.btnMedicion.setObjectName("btnMedicion")
        self.horizontalLayout_7.addWidget(self.btnMedicion)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnRespuesta = QtWidgets.QPushButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRespuesta.sizePolicy().hasHeightForWidth())
        self.btnRespuesta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnRespuesta.setFont(font)
        self.btnRespuesta.setStyleSheet("background-color: rgb(14, 51, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: 20px;\n"
"min-height: 100px;\n"
"min-width:160px;\n"
"max-width:160px;")
        self.btnRespuesta.setObjectName("btnRespuesta")
        self.horizontalLayout_10.addWidget(self.btnRespuesta)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnBorrar = QtWidgets.QPushButton(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBorrar.sizePolicy().hasHeightForWidth())
        self.btnBorrar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnBorrar.setFont(font)
        self.btnBorrar.setStyleSheet("background-color: rgb(14, 51, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: 17px;\n"
"min-height: 100px;\n"
"min-width:160px;\n"
"max-width:160px;")
        self.btnBorrar.setAutoRepeatInterval(0)
        self.btnBorrar.setObjectName("btnBorrar")
        self.horizontalLayout_6.addWidget(self.btnBorrar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addWidget(self.verticalWidget_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalWidget_7 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_7.sizePolicy().hasHeightForWidth())
        self.verticalWidget_7.setSizePolicy(sizePolicy)
        self.verticalWidget_7.setObjectName("verticalWidget_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widgetModulo = PlotWidget(self.verticalWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetModulo.sizePolicy().hasHeightForWidth())
        self.widgetModulo.setSizePolicy(sizePolicy)
        self.widgetModulo.setObjectName("widgetModulo")
        self.verticalLayout_10.addWidget(self.widgetModulo)
        self.verticalLayout_4.addWidget(self.verticalWidget_7)
        self.horizontalWidget_6 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_6.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_6.setSizePolicy(sizePolicy)
        self.horizontalWidget_6.setObjectName("horizontalWidget_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widgetFase = PlotWidget(self.horizontalWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFase.sizePolicy().hasHeightForWidth())
        self.widgetFase.setSizePolicy(sizePolicy)
        self.widgetFase.setObjectName("widgetFase")
        self.horizontalLayout_9.addWidget(self.widgetFase)
        self.verticalLayout_4.addWidget(self.horizontalWidget_6)
        self.verticalWidget_6 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_6.sizePolicy().hasHeightForWidth())
        self.verticalWidget_6.setSizePolicy(sizePolicy)
        self.verticalWidget_6.setObjectName("verticalWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_9.setContentsMargins(-1, 0, 1, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widgetRespuesta = PlotWidget(self.verticalWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetRespuesta.sizePolicy().hasHeightForWidth())
        self.widgetRespuesta.setSizePolicy(sizePolicy)
        self.widgetRespuesta.setObjectName("widgetRespuesta")
        self.verticalLayout_9.addWidget(self.widgetRespuesta)
        self.verticalLayout_4.addWidget(self.verticalWidget_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.widgetRespuesta.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plot Tool"))
        self.tituloT.setText(_translate("MainWindow", "PLOT TOOL - GRUPO 2 - 2021"))
        self.checkFase.setText(_translate("MainWindow", "Fase"))
        self.checkAmplitud.setText(_translate("MainWindow", "Amplitud"))
        self.checkRespuesta.setText(_translate("MainWindow", "Respuesta"))
        self.radioButtonF.setText(_translate("MainWindow", "Frecuencia [Hz]"))
        self.radioButton.setText(_translate("MainWindow", "Frecuencia angular [rad/s]"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Elemento 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Elemento 2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.btnH.setText(_translate("MainWindow", "H ($)"))
        self.btnSpice.setText(_translate("MainWindow", "SPICE"))
        self.btnMedicion.setText(_translate("MainWindow", "MEDICIÓN"))
        self.btnRespuesta.setText(_translate("MainWindow", "RESPUESTA"))
        self.btnBorrar.setText(_translate("MainWindow", "BORRAR GRÁFICOS"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PlotTool_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
