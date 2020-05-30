# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(491, 403)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")

        self.FrameWindow = QtWidgets.QFrame(self.centralwidget)
        self.FrameWindow.setGeometry(QtCore.QRect(70, 60, 351, 251))
        self.FrameWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameWindow.setObjectName("FrameWindow")

        self.LabelUser = QtWidgets.QLabel(self.FrameWindow)
        self.LabelUser.setGeometry(QtCore.QRect(70, 100, 51, 16))
        self.LabelUser.setObjectName("LabelUser")

        self.LabelSenha = QtWidgets.QLabel(self.FrameWindow)
        self.LabelSenha.setGeometry(QtCore.QRect(70, 130, 41, 16))
        self.LabelSenha.setObjectName("LabelSenha")

        self.TextUser = QtWidgets.QLineEdit(self.FrameWindow)
        self.TextUser.setGeometry(QtCore.QRect(120, 100, 111, 21))
        self.TextUser.setObjectName("TextUser")

        self.TextPasswd = QtWidgets.QLineEdit(self.FrameWindow)
        self.TextPasswd.setGeometry(QtCore.QRect(120, 130, 111, 21))
        self.TextPasswd.setObjectName("TextPasswd")
        self.TextPasswd.setEchoMode(QtWidgets.QLineEdit.Password)


        self.BotaoAcessar = QtWidgets.QPushButton(self.FrameWindow)
        self.BotaoAcessar.setGeometry(QtCore.QRect(130, 180, 80, 24))
        self.BotaoAcessar.setObjectName("BotaoAcessar")
        self.BotaoAcessar.clicked.connect(self.check_pass)

        Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")

        Window.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName("menubar")

        self.menuPagina_do_votante = QtWidgets.QMenu(self.menubar)
        self.menuPagina_do_votante.setObjectName("menuPagina_do_votante")
        self.menuPagina_do_Votante = QtWidgets.QMenu(self.menubar)
        self.menuPagina_do_Votante.setObjectName("menuPagina_do_Votante")

        Window.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuPagina_do_votante.menuAction())
        self.menubar.addAction(self.menuPagina_do_Votante.menuAction())

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        #FrameAdmin

        self.FrameAdmin = QtWidgets.QFrame(Window)
        self.FrameAdmin.hide()
        self.FrameAdmin.setGeometry(QtCore.QRect(70, 60, 351, 251))
        self.FrameAdmin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameAdmin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameAdmin.setObjectName("FrameAdmin")
        self.label = QtWidgets.QLabel(self.FrameAdmin)
        self.label.setGeometry(QtCore.QRect(140, 20, 121, 16))
        self.label.setObjectName("label")
        self.BotChapaCadastro = QtWidgets.QPushButton(self.FrameAdmin)
        self.BotChapaCadastro.setGeometry(QtCore.QRect(120, 110, 141, 24))
        self.BotChapaCadastro.setObjectName("BotChapaCadastro")
        self.BotCadCoord = QtWidgets.QPushButton(self.FrameAdmin)
        self.BotCadCoord.setGeometry(QtCore.QRect(120, 170, 141, 24))
        self.BotCadCoord.setObjectName("BotCadCoord")
        self.BotChapaMod = QtWidgets.QPushButton(self.FrameAdmin)
        self.BotChapaMod.setGeometry(QtCore.QRect(120, 140, 141, 24))
        self.BotChapaMod.setObjectName("BotChapaMod")

        self.retranslateUiAcess(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)


        #FrameCadasChapa



        self.FrameCadasChapa = QtWidgets.QFrame(Window)
        self.FrameCadasChapa.hide()
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

        self.retranslateUiCadastro(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)





    def retranslateUiCadastro(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        self.TextCadast.setText(_translate("Window", "Cadastrar nova Chapa"))
        self.LabelSenhaCoord.setText(_translate("Window", "Nome da Chapa"))
        self.LabelNumChapa.setText(_translate("Window", "Numero"))
        self.BotaConfirmCad.setText(_translate("Window", "Confirmar"))


    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.LabelUser.setText(_translate("Window", "Usuario"))
        self.LabelSenha.setText(_translate("Window", "Senha"))
        self.BotaoAcessar.setText(_translate("Window", "Acessar"))
        self.menuPagina_do_votante.setTitle(_translate("Window", "Window"))
        self.menuPagina_do_Votante.setTitle(_translate("Window", "Pagina do Votante"))

    def retranslateUiAcess(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        self.label.setText(_translate("Window", "Bem-vindo(a)!"))
        self.BotChapaCadastro.setText(_translate("Window", "Cadastrar Chapa"))
        self.BotCadCoord.setText(_translate("Window", "Adicionar Coord."))
        self.BotChapaMod.setText(_translate("Window", "Modificar Chapa"))



    def check_pass(self):
        msg = QtWidgets.QMessageBox()
        if(self.TextUser.text() == 'admin' and self.TextPasswd.text() == 'admin'):
            self.FrameWindow.hide()
            self.FrameAdmin.show()
        else:
            msg.setText('Usuario ou Senha Incorreta')
            msg.exec_()





