# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(491, 403)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")

        self.Framelogin = QtWidgets.QFrame(self.centralwidget)
        self.Framelogin.setGeometry(QtCore.QRect(70, 60, 351, 251))
        self.Framelogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Framelogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Framelogin.setObjectName("Framelogin")

        self.LabelUser = QtWidgets.QLabel(self.Framelogin)
        self.LabelUser.setGeometry(QtCore.QRect(70, 100, 51, 16))
        self.LabelUser.setObjectName("LabelUser")

        self.LabelSenha = QtWidgets.QLabel(self.Framelogin)
        self.LabelSenha.setGeometry(QtCore.QRect(70, 130, 41, 16))
        self.LabelSenha.setObjectName("LabelSenha")

        self.TextUser = QtWidgets.QLineEdit(self.Framelogin)
        self.TextUser.setGeometry(QtCore.QRect(120, 100, 111, 21))
        self.TextUser.setObjectName("TextUser")

        self.TextPasswd = QtWidgets.QLineEdit(self.Framelogin)
        self.TextPasswd.setGeometry(QtCore.QRect(120, 130, 111, 21))
        self.TextPasswd.setObjectName("TextPasswd")

        self.BotaoAcessar = QtWidgets.QPushButton(self.Framelogin)
        self.BotaoAcessar.setGeometry(QtCore.QRect(130, 180, 80, 24))
        self.BotaoAcessar.setObjectName("BotaoAcessar")
        self.BotaoAcessar.clicked.connect(self.check_pass)

        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")

        Login.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName("menubar")

        self.menuPagina_do_votante = QtWidgets.QMenu(self.menubar)
        self.menuPagina_do_votante.setObjectName("menuPagina_do_votante")
        self.menuPagina_do_Votante = QtWidgets.QMenu(self.menubar)
        self.menuPagina_do_Votante.setObjectName("menuPagina_do_Votante")

        Login.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuPagina_do_votante.menuAction())
        self.menubar.addAction(self.menuPagina_do_Votante.menuAction())

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.LabelUser.setText(_translate("Login", "Usuario"))
        self.LabelSenha.setText(_translate("Login", "Senha"))
        self.BotaoAcessar.setText(_translate("Login", "Acessar"))
        self.menuPagina_do_votante.setTitle(_translate("Login", "Login"))
        self.menuPagina_do_Votante.setTitle(
            _translate("Login", "Pagina do Votante"))

    def check_pass(self):
        msg = QtWidgets.QMessageBox()
        if(self.TextUser.text() == 'admin' and self.TextPasswd.text() == 'admin'):
            msg.setText('Successo')
            msg.exec_()
        else:
            msg.setText('Senha Incorreta')
            msg.exec_()
