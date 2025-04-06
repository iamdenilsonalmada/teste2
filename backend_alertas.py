
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Olho da República - API + Site")

alertas = [
    {
        "entidade": "Câmara Municipal de Oeiras",
        "empresa": "Infraestruturas Urbanas SA",
        "valor": 49500,
        "tipo": "Ajuste Direto",
        "data": "2024-11-20",
        "link": "https://www.base.gov.pt/Base4/pt/detalhe/?type=contrato&id=1098473"
    },
    {
        "entidade": "Município de Cascais",
        "empresa": "TechGlobal Solutions Lda",
        "valor": 48000,
        "tipo": "Ajuste Direto",
        "data": "2024-12-03",
        "link": "https://www.base.gov.pt/Base4/pt/detalhe/?type=contrato&id=1099238"
    },
    {
        "entidade": "ARS de Lisboa e Vale do Tejo",
        "empresa": "MedicPlus SA",
        "valor": 50000,
        "tipo": "Ajuste Direto",
        "data": "2024-12-07",
        "link": "https://www.base.gov.pt/Base4/pt/detalhe/?type=contrato&id=1099567"
    }
]

@app.get("/alertas")
def get_alertas():
    return JSONResponse(content={"alertas": alertas})

app.mount("/", StaticFiles(directory="static", html=True), name="static")
