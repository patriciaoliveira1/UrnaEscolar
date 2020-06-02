from Banco import Banco


class Usuarios(object):

    def __init__(self, idusuario=0, usuario="", senha=""):
        self.idusuario = idusuario
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (usuario, senha) values ('" +
                      self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set usuario = '" + self.usuario + "', senha = '" +
                      self.senha + "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " +
                      self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, usuario, senha):
        banco = Banco()

        c = banco.conexao.cursor()

        c.execute("select usuario, senha from usuarios where usuario = '" +
                     usuario + "' and senha = '" + senha + "' ")

        for linha in c:
            self.usuario = linha[0]
            self.senha = linha[1]
            return linha

        c.close()
