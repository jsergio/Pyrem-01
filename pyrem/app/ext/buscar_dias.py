import requests
from datetime import datetime

url_base = 'https://economia.awesomeapi.com.br/json'

def monta_busca__url(moedas):
        
    tmp = ','.join(moedas)
    url = url_base + tmp 
    response = requests.get(url)
    if response.status_code == 200:
        
        # Convertendo a resposta para JSON, se aplicável
        data = response.json()

        # Agora você pode manipular os dados conforme necessário
        dts = [
            str(datetime.fromtimestamp(int(item['timestamp']))) for item in data
        ]

        data['dts'] = dts
        # for item in dts:
        #     print(item)

    else:
        # Se a requisição falhou, imprima o código de status
        # print('Falha na requisição:', response.status_code)
        data = {}['status'] = response.status_code


def init_app(app,moedas):
    app.config['RESP_DIAS'] = monta_busca__url(moedas)
