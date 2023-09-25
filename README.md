
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

#### Cria um aluno

```http
  POST /students
```

##### no corpo da requisição:

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name`        | `string`   | **Obrigatório**. O nome do aluno que você quer criar|
| `email`        | `string`   | **Obrigatório**. O email do aluno que você quer criar|

#### Retorna todos alunos

```http
  GET /students
```

#### Retorna um aluno

```http
  GET /students/{id}
```

##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do aluno que você quer |

#### Deleta um aluno

```http
  DELETE /students/{id}
```

##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do aluno que você quer |

#### Atualiza parcialmente um aluno

```http
  PATCH /students/{id}
```
##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do aluno que você quer |

##### no corpo da requisição:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name`      | `string` | O nome do aluno que você quer definir|
| `email`      | `string` | O email do aluno que você quer definir|

#### Atualiza completamente um aluno

```http
  PUT /students/{id}
```
##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do aluno que você quer |

##### no corpo da requisição:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name`      | `string` | **Obrigatório**. O nome do aluno que você quer definir|
| `email`      | `string` | **Obrigatório**. O email do aluno que você quer definir|

#### Retorna as tarefas de um aluno

```http
  GET /students/{id}/tasks
```

##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do aluno que você quer |






#### Cria uma disciplina

```http
  POST /subjects
```

##### no corpo da requisição:

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name`        | `string`   | **Obrigatório**. O nome da disciplina que você quer criar|
| `description`        | `string`   | **Obrigatório**. A descrição da disciplina que você quer criar|

#### Retorna todas as disciplinas

```http
  GET /subjects
```

#### Retorna uma disciplina

```http
  GET /subjects/{id}
```

##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da disciplina que você quer |

#### Deleta uma disciplina

```http
  DELETE /subjects/{id}
```

##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da disciplina que você quer |

#### Atualiza parcialmente uma disciplina

```http
  PATCH /students/{id}
```
##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da disciplina que você quer |

##### no corpo da requisição:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name`      | `string` | O nome da disciplina que você quer definir|
| `description`      | `string` | A descrição da disciplina que você quer definir|

#### Atualiza completamente um aluno

```http
  PUT /students/{id}
```
##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da disciplina que você quer |

##### no corpo da requisição:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name`      | `string` | **Obrigatório**. O nome da disciplina que você quer definir|
| `description`      | `string` | **Obrigatório**. A descrição da disciplina que você quer definir|





















#### Cria uma tarefa

```http
  POST /tasks
```

##### no corpo da requisição:

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `title`        | `string`   | **Obrigatório**. O titulo da tarefa que você quer criar|
| `description`        | `string`   | **Obrigatório**. A descrição da tarefa que você quer criar|
| `due_date`        | `string`   | **Obrigatório**. A data de entrega máxima de entrega da tarefa|
| `completed`        | `string`   | **Obrigatório**. True ou false para definir o status da atividade|
| `student`        | `string`   | **Obrigatório**. O id do aluno que aquela tarefa pertence|
| `subjects`        | `string`   | **Obrigatório**. A lista contendo o id das disciplinas que a tareda faz parte|


#### Retorna todas as disciplinas

```http
  GET /tasks
```

#### Retorna uma disciplina

```http
  GET /tasks/{id}
```

##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da tarefa que você quer |

#### Deleta uma disciplina

```http
  DELETE /tasks/{id}
```

##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da tarefa que você quer |

#### Atualiza parcialmente uma tarefa

```http
  PATCH /students/{id}
```
##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da disciplina que você quer |


##### no corpo da requisição:

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `title`        | `string`   | O titulo da tarefa que você quer criar|
| `description`        | `string`   | A descrição da tarefa que você quer criar|
| `due_date`        | `string`   | A data de entrega máxima de entrega da tarefa|
| `completed`        | `string`   | True ou false para definir o status da atividade|
| `student`        | `string`   | O id do aluno que aquela tarefa pertence|
| `subjects`        | `string`   | A lista contendo o id das disciplinas que a tareda faz parte|

#### Atualiza completamente um aluno

```http
  PUT /students/{id}
```
##### na url:
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID da disciplina que você quer |


##### no corpo da requisição:

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `title`        | `string`   | **Obrigatório**. O titulo da tarefa que você quer criar|
| `description`        | `string`   | **Obrigatório**. A descrição da tarefa que você quer criar|
| `due_date`        | `string`   | **Obrigatório**. A data de entrega máxima de entrega da tarefa|
| `completed`        | `string`   | **Obrigatório**. True ou false para definir o status da atividade|
| `student`        | `string`   | **Obrigatório**. O id do aluno que aquela tarefa pertence|
| `subjects`        | `string`   | **Obrigatório**. A lista contendo o id das disciplinas que a tareda faz parte|


