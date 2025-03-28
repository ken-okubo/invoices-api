
# 💰 Invoices API

Uma API simples para gerenciamento de clientes, rotas e invoices.

A simple API to manage clients, routes and invoices.

---

## 📦 Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Docker + Docker Compose

---

## ✅ Pré-requisitos | Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Como rodar localmente | How to run locally

```bash
# 1. Apagar qualquer instância anterior (containers, volumes, redes)
# 1. Stop and remove any previus containers, volumes, and networks
docker compose down -v

# 2. Construir as imagens
# 2. Build the images
docker compose build

# 3. Subir os containers
# 3. Start the containers
docker compose up
```

Abra outro terminal e aplique as migrações:

Open another terminal and run the migrations:

```bash
# 4. Executar as migrações
# 4. Run the migrations
docker compose exec api alembic upgrade head
```

---

## 🧪 Dados de exemplo | Mock data

Um script opcional (`mock_data.py`) está incluído para popular o banco com 3 clientes, 15 rotas e 5 invoices.

An optional script (`mock_data.py`) is included to populate the database with 3 clients, 15 routes, and 5 invoices.

```bash
docker compose exec api python mock_data.py
```

---

## 🔐 Autenticação | Authentication

A autenticação é baseada em JWT. Para acessar endpoints protegidos:

Authentication is based on JWT. To access protected endpoints:

1. Faça `POST /auth/register` com `email` e `password`
2. Faça `POST /auth/login` para obter o `access_token`
3. Clique em "Authorize" no Swagger e insira: `Bearer <access_token>`

1. Make a `POST /auth/register` request with `email` and `password`
2. Make a POST /auth/login request to get the access_token
3. Click "Authorize" in Swagger and enter: Bearer <access_token>

---

## 📚 Documentação da API | API Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- OpenAPI JSON: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 📁 Estrutura do projeto | Project structure

```
invoices-api/
├── app/
│   ├── api/
│   ├── core/
│   ├── crud/
│   ├── models/
│   ├── schemas/
│   └── main.py
├── alembic/
├── mock_data.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ✍️ Autor | Author

**Ken Okubo**  
Backend Developer  
[LinkedIn](https://www.linkedin.com/in/ken-okubo-8b484978/) | [GitHub](https://github.com/ken-okubo)
