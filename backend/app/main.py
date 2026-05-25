from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, accounts, transactions, budgets, reports, notifications

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FinTrack - Sistema de Gestión Financiera",
    description="API para control de ingresos y egresos personales",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(budgets.router)
app.include_router(reports.router)
app.include_router(notifications.router)

@app.get("/", tags=["health"])
def root():
    return {"message": "FinTrack API funcionando"}
