## Projeto Lista de Filmes Favoritos

### Descrição
Um aplicativo web para gerenciar e avaliar seus filmes favoritos. Utilize nossa API REST para criar, ler, atualizar e deletar filmes, além de calcular a avaliação média de cada um.

### Tecnologias
* **Python:** Linguagem de programação principal.
* **Flask:** Framework web para construção da API.
* **SQLite:** Banco de dados leve para armazenar as informações dos filmes.
* **Postman:** Ferramenta para testar a API.

### Funcionalidades
* **Adicionar um filme:** Inclui título, ano, gênero, sinopse e uma avaliação inicial.
* **Avaliar um filme:** Permite atualizar a avaliação de um filme existente.
* **Modificar um filme:** Edita as informações de um filme, exceto o ID.
* **Deletar um filme:** Remove um filme da lista.
* **Listar um filme:** Retorna as informações detalhadas de um filme específico.
* **Listar todos os filmes:** Retorna uma lista com todos os filmes e suas avaliações.
* **Calcular avaliação final:** Calcula a média das avaliações de um filme, considerando o peso de cada avaliação.

### Exemplos de Requisições
**Adicionar um filme:**
POST /filmes
{
"titulo": "O Poderoso Chefão",
"ano": 1972,
"genero": "Drama",
"sinopse": "A história de uma poderosa família mafiosa italiana...",
"avaliacao": 5
}

**Obter todos os filmes:**
GET /filmes

### Como Usar
1. **Clonar o repositório:** `git clone https://github.com/seu_usuario/seu_repositorio.git`
2. **Criar um ambiente virtual:** `python -m venv venv`
3. **Ativar o ambiente virtual:** `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/macOS)
4. **Instalar as dependências:** `pip install -r requirements.txt`
5. **Rodar o servidor:** `flask run`
6. **Acessar a API:** Utilize o Postman ou qualquer outro cliente HTTP para fazer as requisições.

### Contribuições
Contribuições são bem-vindas! Abra um issue ou um pull request.
