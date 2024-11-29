from peewee import * # Biblioteca peewee, * tras todas funções 
import os
import datetime

# Criando, dando nome para meu banco de dados 
db_name = 'db/filmes.db'

db = SqliteDatabase(db_name) # gerenciador banco de dados

# Classe Filme criada, definindo suas propriedades
class Notas(Model):
    id_filme = IntegerField()
    nota = DecimalField(2,1)

# Classe banco de dados, metainformação
    class Meta:
        database = db

# Conectar ao banco de dados
db.connect()


if not Notas.table_exists():
    db.create_tables([Notas]) 

def add_notas(id_filme,nota):
    notas = Notas.create(id_filme= id_filme, nota = nota )
    return notas # return não pode ficar vazio 

def nota_to_dict(Notas):
    return {
        "id_filme": Notas.id_filme,
        "nota": Notas.nota
    }

def get_nota_by_id_filme(id_filme):
    notas = Notas.select().where(Notas.id_filme == id_filme)
    notas_lista = [nota_to_dict(nota) for nota in notas] # Para cada filme na lista
    return notas_lista
    
def get_notas():
    notas = Notas.select() # método para selecionar tudo
    notas_lista = [nota_to_dict(nota) for nota in notas] # Para cada filme na lista
    return notas_lista

# Fechar a conexão com o banco de dados
db.close()