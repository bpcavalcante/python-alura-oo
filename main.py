from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get('/api/hello')
def hello_world():
    '''

    Endpoint que exibe Hello World

    '''
    return {'Hello': 'World'}


@app.get('/api/restaurantes/')
def listar_restaurantes(restaurante: str = Query(None)):
    '''

    Endpoint para ver os cardápios dos restaurantes

    :param restaurante:
    :return:
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:

            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "Item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

    else:
        return {'Erro': f'{response.status_code} - {response.text}'}
