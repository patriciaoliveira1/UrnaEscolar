from Banco import Banco
 
class Chapas(object):
 
 
    def __init__(self, idchapa = 0, nome = "", num = ""):
            self.idchapa = idchapa
            self.nome = nome
            self.num = num
    
    
    def insertChapa(self):
    
        banco = Banco()
        try:
    
            c = banco.conexao.cursor()
        
            c.execute("insert into chapas (nome, num) values ('" + self.nome + "', '" + self.num + "' )")
        
            banco.conexao.commit()
            c.close()
        
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
    
    
    
    def acrescentarVoto(self,nome,num):
        
        banco = Banco()
        try:
    
            c = banco.conexao.cursor()
    
            for linha in c.execute("select nome, num, votos from chapas where nome = '" + nome + "' and num = '" + num + "' "):
                print(linha)
        
            banco.conexao.commit()
            c.close()
        
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"



    def updateChapa(self):
    
        banco = Banco()
        try:
    
            c = banco.conexao.cursor()
    
            c.execute("update chapas set nome = '" + self.nome + "', num = '" + self.num + "' where idchapa = " + self.idchapa + " ")
        
            banco.conexao.commit()
            c.close()
        
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
    
    def deleteChapa(self):
    
        banco = Banco()
        try:
        
            c = banco.conexao.cursor()
        
            c.execute("delete from chapas where idchapa = " + self.idchapa + " ")
        
            banco.conexao.commit()
            c.close()
        
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"
    
    def selectChapa(self, nome, num):
        banco = Banco()
        try:
        
            c = banco.conexao.cursor()
        
            c.execute("select nome, num from chapas where nome = " + nome + " and num = " + num + " ")
        
            for linha in c:
                self.nome = linha[0]
                self.num = linha[1]
        
            c.close()
        
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"