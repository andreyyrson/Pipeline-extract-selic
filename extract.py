import requests
import json
import os
from datetime import datetime


def job_extracao():
    # URL da API do Banco Central (Série 4390 - Selic)
    URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json"

    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()
        dados = response.json()

        # Criar pasta de dados se não existir
        os.makedirs("data", exist_ok=True)

        # Salvar com a data de hoje para manter histórico
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        caminho = f"data/selic_{data_hoje}.json"

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados[-12:], f, indent=4)  # Salva apenas os últimos 12 meses

        print(f"Sucesso: Dados salvos em {caminho}")

    except Exception as e:
        print(f"Erro na extração: {e}")
        exit(1)


if __name__ == "__main__":
    job_extracao()