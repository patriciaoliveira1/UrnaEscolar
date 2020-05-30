# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 402)
        self.FrameCadasChapa = QtWidgets.QFrame(Form)
        self.FrameCadasChapa.setGeometry(QtCore.QRect(50, 30, 321, 311))
        self.FrameCadasChapa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCadasChapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCadasChapa.setObjectName("FrameCadasChapa")
        self.TextCadast = QtWidgets.QLabel(self.FrameCadasChapa)
        self.TextCadast.setGeometry(QtCore.QRect(100, 0, 131, 16))
        self.TextCadast.setObjectName("TextCadast")
        self.LabelSenhaCoord = QtWidgets.QLabel(self.FrameCadasChapa)
        self.LabelSenhaCoord.setGeometry(QtCore.QRect(120, 70, 101, 20))
        self.LabelSenhaCoord.setObjectName("LabelSenhaCoord")
        self.TextNameChap = QtWidgets.QLineEdit(self.FrameCadasChapa)
        self.TextNameChap.setGeometry(QtCore.QRect(110, 90, 113, 24))
        self.TextNameChap.setObjectName("TextNameChap")
        self.LabelNumChapa = QtWidgets.QLabel(self.FrameCadasChapa)
        self.LabelNumChapa.setGeometry(QtCore.QRect(140, 130, 51, 16))
        self.LabelNumChapa.setObjectName("LabelNumChapa")
        self.TextNumChap = QtWidgets.QLineEdit(self.FrameCadasChapa)
        self.TextNumChap.setGeometry(QtCore.QRect(150, 150, 31, 21))
        self.TextNumChap.setObjectName("TextNumChap")
        self.BotaConfirmCad = QtWidgets.QPushButton(self.FrameCadasChapa)
        self.BotaConfirmCad.setGeometry(QtCore.QRect(130, 200, 81, 21))
        self.BotaConfirmCad.setObjectName("BotaConfirmCad")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TextCadast.setText(_translate("Form", "Cadastrar nova Chapa"))
        self.LabelSenhaCoord.setText(_translate("Form", "Nome da Chapa"))
        self.LabelNumChapa.setText(_translate("Form", "Numero"))
        self.BotaConfirmCad.setText(_translate("Form", "Confirmar"))
