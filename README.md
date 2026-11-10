# Rconnect-mc

API para gerenciar servidores de Minecraft via RCON, com usuários, servidores, produtos e aquisições. Projeto em desenvolvimento.

## Stack

- Python 3.12 + FastAPI
- SQLModel / SQLAlchemy
- PostgreSQL 16
- Docker e Docker Compose

## Pré-requisitos

- [Docker](https://docs.docker.com/engine/install/)
- Docker Compose v2 (comando `docker compose`). Já vem com o Docker Desktop; no Linux pode ser necessário instalar o plugin (`docker-compose-v2` ou `docker-compose-plugin`).

Confira com:

```bash
docker --version
docker compose version
```

## Rodando com Docker

**1. Clone o repositório**

```bash
git clone https://github.com/HeitorTrindade-dev/Rconnect-mc.git
cd Rconnect-mc
```

**2. Crie o arquivo `.env`**

```bash
cp .env.example .env
```

Abra o `.env` e troque `DB_PASSWORD` por uma senha sua. Se a porta `5432` já estiver em uso na sua máquina (por exemplo, por um Postgres local), mude `DB_PORT` para outra, como `5433`.

**3. Suba os containers**

```bash
docker compose up --build
```

Isso sobe o banco (Postgres) e a API juntos. A API só inicia depois que o banco estiver pronto, e as tabelas são criadas automaticamente na inicialização.

**4. Acesse**

| Serviço | URL |
| --- | --- |
| API | http://localhost:8000 |
| Documentação (Swagger) | http://localhost:8000/docs |
| Postgres | `localhost:<DB_PORT>` |

## Comandos úteis

```bash
docker compose up -d          # sobe em segundo plano
docker compose logs -f api    # acompanha os logs da API
docker compose restart api    # reinicia só a API
docker compose down           # derruba os containers (os dados do banco ficam)
docker compose down -v        # derruba e APAGA o volume do banco
docker compose up --build     # rebuilda a imagem (use ao mudar o requirements.txt)
```

A pasta `backend/` é montada dentro do container e a API roda com `--reload`, então alterações no código são aplicadas sem precisar rebuildar.

## Acessando o banco

Use qualquer cliente de Postgres (DBeaver, Beekeeper Studio, psql...) com:

| Campo | Valor |
| --- | --- |
| Host | `localhost` |
| Porta | valor de `DB_PORT` no `.env` |
| Usuário | valor de `DB_USER` |
| Senha | valor de `DB_PASSWORD` |
| Banco | valor de `DB_NAME` |

> A tabela de usuários se chama `user`, que é palavra reservada no Postgres. Em SQL escrito à mão, use `"user"` entre aspas.

## Rodando sem Docker (opcional)

Com um Postgres rodando na sua máquina e o `.env` apontando para ele (`DB_HOST=localhost`):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
```

## Estrutura

```
Rconnect-mc/
├── backend/
│   ├── controllers/   # rotas da API
│   ├── models/        # models do SQLModel (tabelas)
│   ├── repository/    # acesso ao banco
│   ├── services/      # regras de negócio e integrações (RCON)
│   ├── database.py    # conexão e sessão
│   └── main.py        # entrada da aplicação
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env.example
```

## Problemas comuns

- **`port is already allocated` / `address already in use`:** mude `DB_PORT` no `.env` e rode `docker compose down` antes de subir de novo.
- **Mudei a senha no `.env` e o banco não aceita:** o Postgres só lê a senha na primeira criação do volume. Rode `docker compose down -v` e suba de novo (isso apaga os dados).
- **Mudei um model e a tabela não atualizou:** o `create_all` só cria tabelas novas, não altera as existentes. Em desenvolvimento, use `docker compose down -v` para recriar o banco.
