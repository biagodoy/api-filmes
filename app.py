from flask import Flask, request,make_response,jsonify
import FilmeService
import notasService as Notas
import numpy
from decimal import *
# Funções importadas e arquivo
# Sem importar o arquivo em que guarda o banco de dados, não funcionara bem

# Criando instancia de classe Flask
# app primeiro, depois service
app= Flask(__name__)

def valida_header(autenticacao):

    if not autenticacao:
        resposta = {
            "mensagem": "Erro de autenticação",
            "detalhe" : "Não foi encontrada informações de autenticação"
        }
        return {'validado': False,'resposta': make_response(resposta, 401)}
    
    if not autenticacao == ("4b9f2a87-704e-4685-b0bf-668b1c5eb8b1"):
        resposta = {
            "mensagem": "Erro de autenticação",
            "detalhe": "Erro ao validar o token"
        }
        return {'validado': False,'resposta': make_response(resposta, 401)}
    
    return {'validado': True}
    
# Request para adicionar filme
@app.post("/filme")
def Add_filme():
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']
    
    filme_enviado = request.get_json()
    id_do_filme = FilmeService.add_filme(filme_enviado['titulo'],filme_enviado['diretor'],filme_enviado['ano_lancamento'],filme_enviado['genero'],filme_enviado['nota'])

    resposta = {
        "mensagem": "O Filme foi criado!",
        "detalhe": id_do_filme.id
    }
    return make_response(resposta,200)


# Pegar somente um filme
@app.get("/filmes/<int:id>")
def get_filme_by_id(id):
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']

    try:
        filme = FilmeService.get_filme_by_id(id)
        return make_response(jsonify(filme), 200)
    except FilmeService.DoesNotExist:
        return make_response(jsonify({"Error": "Filme não encontrado"}), 404)
    except Exception as e:
        return make_response(jsonify({"Error": "Informações inválidas"}), 400) #??

# Criando endpoint para selecionar todos os filmes salvos
@app.get("/filmes")
def get_all_films():
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']

    dados_filmes = FilmeService.get_filmes()
    return make_response(jsonify(dados_filmes),200)

# Modificar as informações pegando o id
@app.put("/filmes/<id>")
def atualizar_filme(id):
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']

    try:
        data = request.get_json()
        filme_atualizado = FilmeService.update_filme(
            id,
            data.get("titulo"),
            data.get("diretor"),
            data.get("ano_lancamento"),
            data.get("genero"),
            data.get("nota")
        )
        if filme_atualizado: # Se o filme for atualizado
            return make_response(jsonify({"message": "Filme atualizado com sucesso"}), 200)
        else:
            return make_response(jsonify({"Error": "Filme não encontrado"}), 404)
    except Exception as e:
        return make_response(jsonify({"Error": "Informações inválidas"}), 400) #??

# Deletar filme
@app.delete("/filmes/<int:id>")
def deletar_filme(id):
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']

    FilmeService.delete_filme(id)
    return ("Filme deletado com sucesso")

@app.post("/nota")
def Add_nota():
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']


    nota_enviada= request.get_json()
    id_do_filme = Notas.add_notas(nota_enviada['id_filme'],nota_enviada['nota'])
   
    resposta = {
        "mensagem": "A nota foi criada!",
    }
    return make_response(resposta,200)

@app.get("/notas/<int:idFilme>") #retornar
def get_filmes(idFilme):
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']

    notas = Notas.get_nota_by_id_filme(idFilme)
    return make_response(notas,200)

@app.get("/filme/nota/<int:idFilme>")
def get_avaliacao_filme_by_id(idFilme):
    
    validacao = valida_header(request.headers.get('Authorization'))
    if not (validacao['validado']):
        return validacao['resposta']

    # pegar todas as notas do filme
    notas = Notas.get_nota_by_id_filme(idFilme)
    info_filme =  FilmeService.get_filme_by_id(idFilme)
    titulo =  info_filme['titulo']
    diretor =  info_filme['diretor']
    lista_notas = []
    # somar a avaliacao do final
    for nota in notas:
        lista_notas.append((nota['nota'])) 

    avaliacao = numpy.sum(lista_notas) / len(lista_notas)
    
    resposta = {
        'Filme': titulo,
        'Diretor': diretor,
        'Nota': round(avaliacao,2)
    }
    # retornar a avaliacao para o usuario
    return make_response(jsonify(resposta),200)



