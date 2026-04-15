from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "6a33fa384a1b6557ad8c1d65847bc987"

@app.get('/consulta/{cpf}')
def consultar(cpf: str):
    headers = {
        "chave-api-dados": API_KEY
    }
    url_pessoa = f"https://api.portaldatransparencia.gov.br/api-de-dados/pessoa-fisica?cpf={cpf}"
    pessoa = requests.get(url_pessoa, headers=headers).json()

    url_viagens = f"https://api.portaldatransparencia.gov.br/api-de-dados/viagens_por_cpf?cpf={cpf}"
    viagens = requests.get(url_viagens,headers=headers).json()

    url_bpc = f"https://api.portaldatransparencia.gov.br/api-de-dados/bpc_por_cpf_nis?cpf={cpf}"
    bpc = requests.get(url_bpc, headers=headers).json()

    resultado = {
        "Pessoa": pessoa if pessoa else "não encontrada",
        "Total de viagens": len(viagens) if isinstance(viagens, list) else 0,
        "recebe BPC": "sim" if bpc else "não"
    }

    return resultado

