# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(493, 396)
        self.MensagemBoasVindas = QtWidgets.QFrame(Form)
        self.MensagemBoasVindas.setGeometry(QtCore.QRect(160, 30, 120, 80))
        self.MensagemBoasVindas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MensagemBoasVindas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MensagemBoasVindas.setObjectName("MensagemBoasVindas")
        self.label = QtWidgets.QLabel(self.MensagemBoasVindas)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label.setObjectName("label")
        self.FrameBotoes = QtWidgets.QFrame(Form)
        self.FrameBotoes.setGeometry(QtCore.QRect(110, 140, 231, 121))
        self.FrameBotoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameBotoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameBotoes.setObjectName("FrameBotoes")
        self.BotChapaCadastro = QtWidgets.QPushButton(self.FrameBotoes)
        self.BotChapaCadastro.setGeometry(QtCore.QRect(40, 10, 141, 24))
        self.BotChapaCadastro.setObjectName("BotChapaCadastro")
        self.BotChapaMod = QtWidgets.QPushButton(self.FrameBotoes)
        self.BotChapaMod.setGeometry(QtCore.QRect(40, 40, 141, 24))
        self.BotChapaMod.setObjectName("BotChapaMod")
        self.BotCadCoord = QtWidgets.QPushButton(self.FrameBotoes)
        self.BotCadCoord.setGeometry(QtCore.QRect(40, 70, 141, 24))
        self.BotCadCoord.setObjectName("BotCadCoord")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Bem-vindo(a)!"))
        self.BotChapaCadastro.setText(_translate("Form", "Cadastrar Chapa"))
        self.BotChapaMod.setText(_translate("Form", "Modificar Chapa"))
        self.BotCadCoord.setText(_translate("Form", "Adicionar Coord."))
