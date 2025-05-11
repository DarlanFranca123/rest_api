# API de Candidatos 

Uma API REST para gerenciar os dados (nome,semestre, ira e e-mail), dos integrantes do processo seletivo, construída utilizando Flask e SQLAlchemy.

 [Demo / Status](#-demo--status)  
- [Funcionalidades](#-funcionalidades)  
- [Tecnologias](#-tecnologias)  
- [Pré-requisitos](#-pré-requisitos)    
- [Como usar](#-como-usar)  
  - [Rodando o servidor](#rodando-o-servidor)  
  - [Endpoints](#endpoints)  
    - `GET /`  
    - `GET /candidatos`  
    - `GET /candidatos/<id>`  
    - `POST /candidatos`  
    - `PUT /candidatos/<id>`  
    - `DELETE /candidatos/<id>`  
- [Estrutura do Banco de Dados](#-estrutura-do-banco-de-dados)  
- [Logs](#-logs)  


## Funcionalidades

- Listar todos os candidatos  
- Buscar candidato por ID  
- Inserir novo candidato  
- Atualizar dados de um candidato  
- Deletar candidato  

---

## Tecnologias

- [Python 3.x](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)   

---

## Pré-requisitos

- Python 3.7 ou superior  
- pip (gerenciador de pacotes do Python)  

---

## Como usar

### Rodando o servidor

```bash

pyhton main.py

```
E o servidor irá iniciar em http://127.0.0.1:5000

### Endpoints

| Método | Rota                     | Descrição                            |
|:-------|:-------------------------|:-------------------------------------|
| `GET`  | `/`                      | Mensagem de boas-vindas             |
| `GET`  | `/candidatos`            | Lista todos os candidatos           |
| `GET`  | `/candidatos/<id>`       | Busca candidato por ID              |
| `POST` | `/candidatos`            | Cria um novo candidato              |
| `PUT`  | `/candidatos/<id>`       | Atualiza um candidato existente     |
| `DELETE`| `/candidatos/<id>`      | Remove um candidato por ID          |

## Estrutura do Banco de Dados

A aplicação utiliza um banco de dados SQLite chamado `candidatos.db`, que possui uma única tabela:

### 🧾 Tabela: `Candidatos`

| Campo     | Tipo         | Restrições                  |
|-----------|--------------|-----------------------------|
| `id`      | Integer      | Primary Key, AutoIncrement  |
| `nome`    | String(100)  | Obrigatório (NOT NULL)      |
| `semestre`| Integer      | Obrigatório (NOT NULL)      |
| `ira`     | Float        | Obrigatório (NOT NULL)      |
| `email`   | String(100)  | Obrigatório (NOT NULL)      |

### 📄 Representação em SQL

```sql
CREATE TABLE candidatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    semestre INTEGER NOT NULL,
    ira REAL NOT NULL,
    email TEXT NOT NULL
);
```
## Logs 

Na execução, a API imprime no terminal algumas mensagens simples sobre as requisições do usuário e se elas ocorreram sem erros. 

