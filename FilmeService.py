# Filme.Service é meu banco de dados, onde  posso fazer varias modificações e adicionar tbm
# Guarda informações muito importantes que faz o app.py funcionar

from peewee import * # Biblioteca peewee, * tras todas funções 
import os
import datetime

# Criando, dando nome para meu banco de dados 
db_name = 'db/filmes.db'

db = SqliteDatabase(db_name) # gerenciador banco de dados

# Classe Filme criada, definindo suas propriedades
class Filme(Model):
    id = AutoField()
    titulo = CharField()
    diretor = CharField()
    ano_lancamento = IntegerField()
    genero = CharField()
    nota = DecimalField(2,1)

# Classe banco de dados, metainformação
    class Meta:
        database = db

# Conectar ao banco de dados
db.connect()

# Validação, se a classe Filme não existe.Caso não, criar uma 
# Classe + método
if not Filme.table_exists():
    db.create_tables([Filme]) 

# Função para adicionar filme
# Classe Fime + método
def add_filme(titulo, diretor, ano_lancamento, genero, nota):
    filme = Filme.create(titulo = titulo , diretor = diretor , ano_lancamento = ano_lancamento , genero = genero , nota = nota )
    return filme # return não pode ficar vazio 

# Função para transformar minha classe filme em formato de dicionario
# Retornando um json
def filme_to_dict(filme):
    return{
        "id": filme.id, # json + classe e suas propriedades 
        "titulo": filme.titulo,
        "diretor":  filme.diretor,
        "ano_lancamento": filme.ano_lancamento,
        "genero": filme.genero,
        "nota": filme.nota
    }

# Pegar 1 filme somente
def get_filme_by_id(id):
    filme = Filme.get(Filme.id==id)
    print (filme.id)
    return filme_to_dict(filme)
    
    

# Função que exibe todos os filmes da lista
# GET seleciona apenas o primeiro que aparece na lista 
def get_filmes():
    filmes = Filme.select() # método para selecionar tudo
    filmes_lista = [filme_to_dict(filme)for filme in filmes] # Para cada filme na lista
    return filmes_lista
# se filme existe em Filmes retornar a lista

#  Atualizar filme
# parametros é igual a nada, se não, não pode ter duas possibilidades
# Duas possibilidades, parametro direto da classe ou o da função de agora
def update_filme(id,titulo=None, diretor=None, ano_lancamento=None, genero=None, nota=None):
    try:
        filme = Filme.get(Filme.id == id)
        filme.titulo = titulo or filme.titulo
        filme.diretor = diretor or filme.diretor
        filme.ano_lacamento = ano_lancamento or filme.ano_lacamento
        filme.genero = genero or filme.genero
        filme.nota = nota or filme.nota
        filme.save() # Salva as mudanças no banco de dados
        return filme
    except Exception as e:
        return None # Retornar nada, se não ter nenhuma modificação

# Deletar filme pelo id
def delete_filme(id):
    Filme.delete_by_id(id) # método

# Fechar a conexão com o banco de dados
db.close()

