# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewMarketim.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenerarMarketim(object):
    def setupUi(self, GenerarMarketim):
        GenerarMarketim.setObjectName("GenerarMarketim")
        GenerarMarketim.resize(761, 358)
        self.centralwidget = QtWidgets.QWidget(GenerarMarketim)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 221, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 130, 221, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 240, 281, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 40, 451, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 130, 461, 21))
        self.label_2.setObjectName("label_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(640, 240, 91, 31))
        self.commandLinkButton.setObjectName("commandLinkButton")
        GenerarMarketim.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GenerarMarketim)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 25))
        self.menubar.setObjectName("menubar")
        GenerarMarketim.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GenerarMarketim)
        self.statusbar.setObjectName("statusbar")
        GenerarMarketim.setStatusBar(self.statusbar)

        self.retranslateUi(GenerarMarketim)
        QtCore.QMetaObject.connectSlotsByName(GenerarMarketim)

    def retranslateUi(self, GenerarMarketim):
        _translate = QtCore.QCoreApplication.translate
        GenerarMarketim.setWindowTitle(_translate("GenerarMarketim", "Generar Marketim"))
        self.pushButton.setText(_translate("GenerarMarketim", "Archivo 1"))
        self.pushButton_2.setText(_translate("GenerarMarketim", "Archivo 2"))
        self.pushButton_3.setText(_translate("GenerarMarketim", "Generar Archivo nuevo"))
        self.label.setText(_translate("GenerarMarketim", "Archivo Base:"))
        self.label_2.setText(_translate("GenerarMarketim", "Archivo Números:"))
        self.commandLinkButton.setText(_translate("GenerarMarketim", "Reiniciar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerarMarketim = QtWidgets.QMainWindow()
    ui = Ui_GenerarMarketim()
    ui.setupUi(GenerarMarketim)
    GenerarMarketim.show()
    sys.exit(app.exec_())

