import requests
from datetime import datetime


url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/15'

print('\n\n\nURL = ',url,'\n\n\n')

response = requests.get(url)

if response.status_code == 200:

    # Convertendo a resposta para JSON, se aplicável
    data = response.json()

    # Agora você pode manipular os dados conforme necessário
    dts = [str(datetime.fromtimestamp(int(item['timestamp']))) for item in data]

    for item in dts:
        print(item)

else:
    # Se a requisição falhou, imprima o código de status
    print('Falha na requisição:', response.status_code)
    data = response.status_code


def init_app(app):
    app.config['RESP_DIAS'] = data
