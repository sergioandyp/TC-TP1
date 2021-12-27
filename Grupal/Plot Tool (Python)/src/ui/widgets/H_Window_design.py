# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\ui\designer\HWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class H_Window_design(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(402, 312)
        Dialog.setMinimumSize(QtCore.QSize(0, 312))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 350))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(-1, 11, -1, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nombreL = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombreL.sizePolicy().hasHeightForWidth())
        self.nombreL.setSizePolicy(sizePolicy)
        self.nombreL.setObjectName("nombreL")
        self.horizontalLayout_3.addWidget(self.nombreL)
        self.nombreT = QtWidgets.QLineEdit(Dialog)
        self.nombreT.setInputMask("")
        self.nombreT.setObjectName("nombreT")
        self.horizontalLayout_3.addWidget(self.nombreT)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.numeradorL = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numeradorL.sizePolicy().hasHeightForWidth())
        self.numeradorL.setSizePolicy(sizePolicy)
        self.numeradorL.setObjectName("numeradorL")
        self.horizontalLayout_2.addWidget(self.numeradorL)
        self.numeradorT = QtWidgets.QLineEdit(Dialog)
        self.numeradorT.setInputMask("")
        self.numeradorT.setObjectName("numeradorT")
        self.horizontalLayout_2.addWidget(self.numeradorT)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.denominadorL = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.denominadorL.sizePolicy().hasHeightForWidth())
        self.denominadorL.setSizePolicy(sizePolicy)
        self.denominadorL.setObjectName("denominadorL")
        self.horizontalLayout.addWidget(self.denominadorL)
        self.denominadorT = QtWidgets.QLineEdit(Dialog)
        self.denominadorT.setInputMask("")
        self.denominadorT.setObjectName("denominadorT")
        self.horizontalLayout.addWidget(self.denominadorT)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widgetTransferencia = TeXLabel(Dialog)
        self.widgetTransferencia.setObjectName("widgetTransferencia")
        self.verticalLayout.addWidget(self.widgetTransferencia)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.freqLinRbtn = QtWidgets.QRadioButton(Dialog)
        self.freqLinRbtn.setObjectName("freqLinRbtn")
        self.freqTypeGroup = QtWidgets.QButtonGroup(Dialog)
        self.freqTypeGroup.setObjectName("freqTypeGroup")
        self.freqTypeGroup.addButton(self.freqLinRbtn)
        self.horizontalLayout_4.addWidget(self.freqLinRbtn)
        self.freqLogRbtn = QtWidgets.QRadioButton(Dialog)
        self.freqLogRbtn.setChecked(True)
        self.freqLogRbtn.setObjectName("freqLogRbtn")
        self.freqTypeGroup.addButton(self.freqLogRbtn)
        self.horizontalLayout_4.addWidget(self.freqLogRbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.okBtn = QtWidgets.QPushButton(Dialog)
        self.okBtn.setMinimumSize(QtCore.QSize(60, 30))
        self.okBtn.setMaximumSize(QtCore.QSize(60, 30))
        self.okBtn.setStyleSheet("background-color: rgb(14, 51, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"")
        self.okBtn.setObjectName("okBtn")
        self.verticalLayout.addWidget(self.okBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Función Transferencia"))
        self.nombreL.setText(_translate("Dialog", "Nombre:        "))
        self.nombreT.setPlaceholderText(_translate("Dialog", "Ingrese el nombre de la curva"))
        self.numeradorL.setText(_translate("Dialog", "Numerador:   "))
        self.numeradorT.setPlaceholderText(_translate("Dialog", "Ingrese los coeficientes separados por comas"))
        self.denominadorL.setText(_translate("Dialog", "Denominador:"))
        self.denominadorT.setPlaceholderText(_translate("Dialog", "Ingrese los coeficientes separados por comas"))
        self.freqLinRbtn.setText(_translate("Dialog", "Lineal"))
        self.freqLogRbtn.setText(_translate("Dialog", "Logarítmica"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "1"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "1e7"))
        self.okBtn.setText(_translate("Dialog", "OK"))
from src.ui.widgets.TeXLabel import TeXLabel


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = H_Window_design()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
