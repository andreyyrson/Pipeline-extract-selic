import requests
import json
import os
from datetime import datetime

def job_extracao():
    # URL correta pegando desde 2022
    URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2022&dataFinal=04/03/2026"

    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()
        dados = response.json()

        os.makedirs("data", exist_ok=True)

        data_hoje = datetime.now().strftime("%Y-%m-%d")
        caminho = f"data/selic_{data_hoje}.json"

        # CORREÇÃO: Salve 'dados' inteiro para ter o histórico desde 2022
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4)

        print(f"Sucesso: {len(dados)} registros salvos em {caminho}")

    except Exception as e:
        print(f"Erro na extração: {e}")
        exit(1)

if __name__ == "__main__":
    job_extracao()