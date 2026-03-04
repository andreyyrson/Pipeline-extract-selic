Pipeline de Extração e Dashboard Selic

Este projeto é uma solução automatizada de Data Engineering e Visualização de Dados. Ele extrai diariamente a taxa Selic do Banco Central do Brasil, armazena o histórico em JSON e gera um dashboard interativo com a média dos últimos 3 anos.
🚀 Funcionalidades

    Extração Automática: Script Python que consome a API do Banco Central (SGS).

    Armazenamento de Dados: Histórico salvo na pasta /data em formato JSON.

    Transformação com Pandas: Filtra e calcula a média aritmética da Selic dos últimos 36 meses.

    Dashboard Interativo: Gráfico gerado via Plotly e hospedado no GitHub Pages.

    CI/CD com GitHub Actions: Pipeline configurada para rodar diariamente e atualizar o site sem intervenção humana.

🛠️ Tecnologias Utilizadas

    Linguagem: Python 3.12

    Bibliotecas:

        Pandas: Manipulação e análise de dados.

        Plotly: Criação de gráficos interativos.

        Requests: Consumo de APIs REST.

    Infraestrutura: GitHub Actions (Automação) e GitHub Pages (Hospedagem).

📊 Estrutura do Projeto
Bash

├── .github/workflows/  # Configuração da automação (YAML)
├── data/               # Arquivos JSON extraídos da API
├── docs/               # Arquivo index.html (Dashboard)
├── extract.py          # Script de extração (ETL)
├── dashboard.py        # Script de análise e geração de gráfico
├── requirements.txt    # Dependências do projeto
└── .venv/              # Ambiente virtual local

⚙️ Como rodar localmente

    Clone o repositório:
    Bash

    git clone https://github.com/andreyyrson/Pipeline-extract-selic.git
    cd Pipeline-extract-selic

    Crie e ative o ambiente virtual:
    Bash

    python3 -m venv .venv
    source .venv/bin/activate

    Instale as dependências:
    Bash

    pip install -r requirements.txt

    Execute os scripts:
    Bash

    python3 extract.py    # Para baixar os dados
    python3 dashboard.py  # Para gerar o dashboard

🌐 Dashboard Online

O resultado final pode ser visualizado em tempo real aqui:

👉 [Link do seu GitHub Pages aqui]
