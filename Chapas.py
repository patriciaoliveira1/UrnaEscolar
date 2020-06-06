from Banco import Banco
 
class Chapas(object):
 
 
    def __init__(self, nome = "", num = ""):
            self.nome = nome
            self.num = num
    
    
    def insertChapa(self):
    
        banco = Banco()
        try:
    
            c = banco.conexao.cursor()
        
            c.execute("insert into chapas (nome, num, votos) values ('" + self.nome + "', '" + self.num + "', 0 )")
        
            banco.conexao.commit()
            c.close()
        
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
    
    
    
    def acrescentarVoto(self):
        
        banco = Banco()
        id1 = 0
        voto1 = 0
        c = banco.conexao.cursor()
        for id in c.execute("select idchapa from chapas where nome = '"+self.nome+"' "):
            id1 = id[0]
            print(id1)
        for voto in c.execute("select votos from chapas where idchapa = '"+ str(id1) + "' "):
            voto1 = voto[0]
            print(voto1)
        
        c.execute("update chapas set votos = '"+str(voto1+1)+"' where idchapa = '"+str(id1)+"' ")
    
        banco.conexao.commit()
        c.close()
        




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
    
    def selectChapa(self):
        banco = Banco()
        chapas = []
        
        c = banco.conexao.cursor()
        
        c.execute("select idchapa, nome, num from chapas")
        
        for linha in c:
            chapas.append(linha)
            
        return chapas
        c.close()


    def countChapas(self):
        banco = Banco()
        chapas = []
        
        c = banco.conexao.cursor()
        
        c.execute("select count(nome) from chapas")
        
        for linha in c:
            chapas.append(linha)
            
        return chapas[0][0]
        c.close()   

    def getVotosChapas(self):
        banco = Banco()
        chapas = []
        
        c = banco.conexao.cursor()
        
        c.execute("select nome,votos from chapas")
        
        for linha in c:
            chapas.append(linha)
            
        return chapas
        c.close()   

