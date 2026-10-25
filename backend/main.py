from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Exemplo de import do seu controller de usuários
#from app.controllers import user_controller

app = FastAPI(title="Rconnect-mc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(#placeholder_da_silva) #colocar o router do controller

@app.get("/")
def read_root():
    return {"message": "API rodando"}
