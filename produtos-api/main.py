from fastapi import FastAPI
from database import engine, Base
from router import router as produto_router

Base.metadata.create_all(bind=engine)

app= FastAPI(
    title="API de produtos maneiros",
    description="CRUD com FastAPI + SQLALchemy + SQLite",
    version="2.0.0"
)

app.include_router(produto_router)

app.get('/')
def raiz():
    return {"status": "online", "docs": "versao:" "2.0.0"}