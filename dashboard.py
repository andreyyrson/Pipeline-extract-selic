import pandas as pd
import plotly.express as px
import json
import os


def gerar_dashboard():
    # 1. Carregar o dado mais recente da pasta data/
    arquivos = sorted([f for f in os.listdir('data') if f.endswith('.json')])
    if not arquivos:
        print("Nenhum dado encontrado.")
        return

    with open(f'data/{arquivos[-1]}', 'r') as f:
        dados = json.load(f)

    # 2. Transformação com Pandas
    df = pd.DataFrame(dados)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = pd.to_numeric(df['valor'])

    # Filtrar últimos 3 anos (36 meses)
    df = df.sort_values('data').tail(36)

    # Calcular média anual
    df['ano'] = df['data'].dt.year
    media_anual = df.groupby('ano')['valor'].mean().reset_index()

    # 3. Criar Gráfico
    fig = px.line(df, x='data', y='valor', title='Evolução da Taxa Selic (Últimos 3 Anos)')
    fig.add_bar(x=media_anual['ano'].apply(lambda x: pd.to_datetime(f'{x}-06-01')),
                y=media_anual['valor'], name='Média Anual')

    # 4. Salvar como HTML
    os.makedirs('docs', exist_ok=True)
    fig.write_html('docs/index.html')
    print("Dashboard gerado em docs/index.html")


if __name__ == "__main__":
    gerar_dashboard()