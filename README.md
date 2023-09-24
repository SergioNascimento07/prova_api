
# API de CRUD para alunos, tarefas e disciplinas

Este projeto é uma api, onde é possível realizar criação, deleção, atualização e busca de alunos, tarefas e disciplinas, para controle de atividades.




## Tabela de conteúdos
   * [Funcionalidades](#funcionalidades)
   * [Tecnologias utilizadas](#tecnologias-utilizadas)
   * [Instalação](#instalacao)
   * [Como usar](#como-usar)
   * [Documentação da API](#documentacao-da-api)
   
## Funcionalidades

- [x]  Cadastro de aluno
- [x]  Listagem de aluno
- [x]  Atualização de aluno
- [x]  Deletação de aluno
- [x]  Listagem de tarefas de um aluno
- [x]  Cadastro de disciplina
- [x]  Listagem de disciplina
- [x]  Atualização de disciplina
- [x]  Deletação de disciplina
- [x]  Cadastro de tarefa
- [x]  Listagem de tarefa
- [x]  Atualização de tarefa
- [x]  Deletação de tarefa


## tecnologias utilizadas

- Python 3.11.0
- Postman 10.18.5

## Instalação

- baixar  projeto na máquina:
```
  git clone https://github.com/SergioNascimento07/prova_api
``` 

- Abrir o terminal de comando na pasta raiz do projeto

- Criar ambiente virtual:
```
    python -m venv ./venv 
```

- Ativar ambiente virtual:
```
    ./venv/Scripts/activate
```

- Instalar dependências:
```
    pip install -r requirements.txt
```

- Rodar projeto:
```
    python manage.py runserver
```

## Como usar

Para testar o projeto pode ser utilizado o postman, importando o ```prova_andre_api.postman_collection.json``` que carregará os endpoints e mostrará como colocar os dados corretos. Se tiver dificuldades em importar a collection, pode seguir este tutorial https://www.youtube.com/watch?v=M-qHvBhULes

- obs: Na collection do postman há também exemplo de dados e respostas passadas em cada requisição.
## Documentação da API

#### Retorna todos alunos

```http
  GET /students
```

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.

