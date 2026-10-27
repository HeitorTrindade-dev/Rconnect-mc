from sqlmodel import create_engine
import os

# URL de conexão com o PostgreSQL. O ideal é puxar isso de um arquivo .env depois!
DATABASEURL = "postgresql://usuario:senha@localhost:5432/nome_do_banco"

engine = create_engine(DATABASEURL, echo=True);