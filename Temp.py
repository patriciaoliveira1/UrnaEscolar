from tkinter import *
import Admin
  
class Login:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.Titulo = Frame(master)
        self.Titulo["pady"] = 20
        self.Titulo.pack()
  
        self.CampoUsuario = Frame(master)
        self.CampoUsuario["padx"] = 20
        self.CampoUsuario.pack()
  
        self.CampoSenha = Frame(master)
        self.CampoSenha["padx"] = 20
        self.CampoSenha.pack()
  
        self.BotaoLog = Frame(master)
        self.BotaoLog["pady"] = 20
        self.BotaoLog.pack()


        self.titulo = Label(self.Titulo, text="Login")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.CampoUsuario,text="Usuario", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.CampoUsuario)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.CampoSenha, text=" Senha ", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.CampoSenha)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.BotaoLog)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  

        self.mensagem = Label(self.BotaoLog, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "admin" and senha == "!@4dm1n#":
            
        else:
            self.mensagem["text"] = "Usuário/senha inválidos"
 
janela = Tk()
Login(janela)
janela.title("Urna Escolar 2020")
janela.mainloop()