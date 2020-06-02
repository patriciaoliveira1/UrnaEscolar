import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()
    
    def createTable(self):
        c = self.conexao.cursor()
    
        c.execute("""CREATE TABLE if not exists usuarios (
                    idusuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                    usuario TEXT,
                    senha TEXT)""")
        
        c.execute("""CREATE TABLE if not exists chapas (
                    idchapa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                    nome TEXT,
                    num INTEGER,
                    votos INTEGER)""")
        self.conexao.commit()
        c.close()