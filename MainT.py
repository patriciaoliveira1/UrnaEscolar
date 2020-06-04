# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Usuarios import Usuarios
from Chapas import Chapas

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(510, 460)

        #Login

        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")

        self.FrameWindow = QtWidgets.QFrame(self.centralwidget)
        self.FrameWindow.setGeometry(QtCore.QRect(70, 10, 361, 421))
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

        self.BotaoVoto = QtWidgets.QPushButton(self.FrameWindow)
        self.BotaoVoto.setGeometry(QtCore.QRect(120, 360, 111, 24))
        self.BotaoVoto.setObjectName("BotaoVoto")
        self.BotaoVoto.clicked.connect(self.mudar_Voto)

        Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")

        Window.setStatusBar(self.statusbar)

        self.retranslateUiLogin(Window)
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
        self.BotChapaCadastro.clicked.connect(self.mudar_cadChapa)

        self.BotCadCoord = QtWidgets.QPushButton(self.FrameAdmin)
        self.BotCadCoord.setGeometry(QtCore.QRect(120, 140, 141, 24))
        self.BotCadCoord.setObjectName("BotCadCoord")
        self.BotCadCoord.clicked.connect(self.mudar_cadCoord)

        self.retranslateUiAdmin(Window)
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
        self.BotaConfirmCad.clicked.connect(self.confirm_cad_chapa)

        self.retranslateUiCadastro(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        #FrameCadCoord

        self.FrameCadCoord = QtWidgets.QFrame(Window)
        self.FrameCadCoord.hide()
        self.FrameCadCoord.setGeometry(QtCore.QRect(30, 60, 371, 251))
        self.FrameCadCoord.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCadCoord.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCadCoord.setObjectName("FrameCadCoord")
        self.LabelNomeCoord = QtWidgets.QLabel(self.FrameCadCoord)
        self.LabelNomeCoord.setGeometry(QtCore.QRect(160, 70, 41, 16))
        self.LabelNomeCoord.setObjectName("LabelNomeCoord")
        self.TextUserCoord = QtWidgets.QLineEdit(self.FrameCadCoord)
        self.TextUserCoord.setGeometry(QtCore.QRect(120, 90, 113, 24))
        self.TextUserCoord.setObjectName("TextUserCoord")
        self.label_3 = QtWidgets.QLabel(self.FrameCadCoord)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 41, 16))
        self.label_3.setObjectName("label_3")
        self.TextPasswdCoord = QtWidgets.QLineEdit(self.FrameCadCoord)
        self.TextPasswdCoord.setGeometry(QtCore.QRect(120, 160, 113, 24))
        self.TextPasswdCoord.setObjectName("TextPasswdCoord")
        self.pushButton = QtWidgets.QPushButton(self.FrameCadCoord)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.confirm_cad_coord)
    
    
        self.label = QtWidgets.QLabel(self.FrameCadCoord)
        self.label.setGeometry(QtCore.QRect(110, 10, 141, 16))
        self.label.setObjectName("label")

        self.retranslateUiCadCoord(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)


        #PagVoto

        self.FrameVoto = QtWidgets.QFrame(Window)
        self.FrameVoto.hide()
        self.FrameVoto.setGeometry(QtCore.QRect(70, 60, 351, 251))
        self.FrameVoto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameVoto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameVoto.setObjectName("FrameVoto")
        self.BtConfirm = QtWidgets.QDialogButtonBox(self.FrameVoto)
        self.BtConfirm.setGeometry(QtCore.QRect(90, 210, 166, 24))
        self.BtConfirm.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.BtConfirm.setObjectName("BtConfirm")
        self.BtConfirm.accepted.connect(self.confirm_voto)
        self.BtConfirm.rejected.connect(self.voltar_voto)

        self.LabelEscolha = QtWidgets.QLabel(self.FrameVoto)
        self.LabelEscolha.setGeometry(QtCore.QRect(120, 40, 111, 31))
        self.LabelEscolha.setObjectName("LabelEscolha")
        self.labelBV = QtWidgets.QLabel(self.FrameVoto)
        self.labelBV.setGeometry(QtCore.QRect(130, 0, 91, 16))
        self.labelBV.setObjectName("labelBV")
        self.BoxEscolhaCh = QtWidgets.QComboBox(self.FrameVoto)
        self.BoxEscolhaCh.setGeometry(QtCore.QRect(98, 80, 131, 24))
        self.BoxEscolhaCh.setObjectName("BoxEscolhaCh")
        self.CampoSenhaVoto = QtWidgets.QLineEdit(self.FrameVoto)
        self.CampoSenhaVoto.setGeometry(QtCore.QRect(100, 140, 131, 31))
        self.CampoSenhaVoto.setObjectName("CampoSenhaVoto")
        self.CampoSenhaVoto.setEchoMode(QtWidgets.QLineEdit.Password)

        self.labelVoto = QtWidgets.QLabel(self.FrameVoto)
        self.labelVoto.setGeometry(QtCore.QRect(70, 110, 211, 16))
        self.labelVoto.setObjectName("labelVoto")


        chapa = Chapas()
        chapas = chapa.selectChapa()
        if(chapas != None):
            for c in chapas:
                self.BoxEscolhaCh.addItem(c[1])
        else:
            self.BoxEscolhaCh.addItem("Sem Chapas")



        self.retranslateUiVoto(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        #PagCoord

        self.frameCoord = QtWidgets.QFrame(Window)
        self.frameCoord.hide()
        self.frameCoord.setGeometry(QtCore.QRect(20, 10, 451, 401))
        self.frameCoord.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCoord.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCoord.setObjectName("frameCoord")
        self.TableVotos = QtWidgets.QTableWidget(self.frameCoord)
        self.TableVotos.setGeometry(QtCore.QRect(110, 90, 211, 281))
       
        qtchapas = Chapas().countChapas()
        self.TableVotos.setRowCount(qtchapas)
        self.TableVotos.setColumnCount(2)
        self.TableVotos.setObjectName("TableVotos")
        linha = 0
        coluna = 0
        self.atualizarTabela(linha,coluna)
        item = QtWidgets.QTableWidgetItem()
        self.TableVotos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableVotos.setHorizontalHeaderItem(1, item)
        self.labelMsgCoord = QtWidgets.QLabel(self.frameCoord)
        self.labelMsgCoord.setGeometry(QtCore.QRect(150, 30, 121, 20))
        self.labelMsgCoord.setObjectName("labelMsgCoord")

        self.retranslateCoord(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)


    #retranslates
        
    def retranslateCoord(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Form", "Form"))
        item = self.TableVotos.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Chapa"))
        item = self.TableVotos.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Votos"))
        self.labelMsgCoord.setText(_translate("Form", "Resultado dos Votos"))

    def retranslateUiVoto(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LabelEscolha.setText(_translate("Dialog", "Escolha a chapa:"))
        self.labelBV.setText(_translate("Dialog", "Bem-Vindo(a)!"))
        self.labelVoto.setText(_translate("Dialog", "Por favor, Insira a senha para acesso"))

    def retranslateUiModChapa(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        self.TextMod.setText(_translate("Window", "Altere a chapa desejada:"))
        self.BotaoConfirmMod.setText(_translate("Window", "Confirmar"))

    def retranslateUiCadCoord(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        self.LabelNomeCoord.setText(_translate("Window", "Nome"))
        self.label_3.setText(_translate("Window", "Senha"))
        self.pushButton.setText(_translate("Window", "Confirmar"))
        self.label.setText(_translate("Window", "Cadastrar Coordenador"))

    def retranslateUiCadastro(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        self.TextCadast.setText(_translate("Window", "Cadastrar nova Chapa"))
        self.LabelSenhaCoord.setText(_translate("Window", "Nome da Chapa"))
        self.LabelNumChapa.setText(_translate("Window", "Numero"))
        self.BotaConfirmCad.setText(_translate("Window", "Confirmar"))

    def retranslateUiLogin(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.LabelUser.setText(_translate("Window", "Usuario"))
        self.LabelSenha.setText(_translate("Window", "Senha"))
        self.BotaoAcessar.setText(_translate("Window", "Acessar"))
        self.BotaoVoto.setText(_translate("Window", "Pagina de Voto"))

    def retranslateUiAdmin(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        self.label.setText(_translate("Window", "Bem-vindo(a)!"))
        self.BotChapaCadastro.setText(_translate("Window", "Cadastrar Chapa"))
        self.BotCadCoord.setText(_translate("Window", "Adicionar Coord."))


    #Botoes

    def confirm_cad_chapa(self):
        chapa = Chapas()
        chapa.nome = self.TextNameChap.text()
        chapa.num = self.TextNumChap.text()

        chapa.insertChapa()

    def confirm_cad_coord(self):
        coord = Usuarios()
        coord.usuario = self.TextUserCoord.text()
        coord.senha = self.TextPasswdCoord.text()

        coord.insertUser()

    def confirm_voto(self):
        msg = QtWidgets.QMessageBox()
        if(self.CampoSenhaVoto.text() == 'q1w2e3r4'):
            c = self.BoxEscolhaCh.currentText()
            chapa = Chapas(c)
            chapa.acrescentarVoto()
            self.CampoSenhaVoto.setText('')
            self.atualizarTabela(0,0)
        else:
            msg.setText('Senha Incorreta')
            msg.exec_()

    def mudar_cadChapa(self):
        self.FrameAdmin.hide()
        self.FrameCadasChapa.show()

    def mudar_cadCoord(self):
        self.FrameAdmin.hide()
        self.FrameCadCoord.show()

    def mudar_Voto(self):
        self.FrameWindow.hide()
        self.FrameVoto.show()

    def voltar_voto(self):
        self.FrameWindow.show()
        self.FrameVoto.hide()        

    def check_pass(self):
        msg = QtWidgets.QMessageBox()
        user = Usuarios()
        linha = user.selectUser(self.TextUser.text(),self.TextPasswd.text())
        if(self.TextUser.text() == 'admin' and self.TextPasswd.text() == 'admin'):
            self.FrameWindow.hide()
            self.FrameAdmin.show()
        elif(linha != None):
            self.FrameWindow.hide()
            self.frameCoord.show()
        else:
            msg.setText('Usuario ou Senha Incorreta')
            msg.exec_()


    def atualizarTabela(self,linha,coluna):
        for i in Chapas().getVotosChapas():
            coluna = 0
            self.TableVotos.setItem(linha,coluna, QtWidgets.QTableWidgetItem(i[0]))
            coluna = coluna+1
            self.TableVotos.setItem(linha,coluna, QtWidgets.QTableWidgetItem(str(i[1])))
            linha = linha+1