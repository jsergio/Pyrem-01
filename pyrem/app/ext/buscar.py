import requests


def monta_url(*args):
    result = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    if args:
        result_local = result[0:-7]   # retira USD-BRL de result
        temp0 = ','.join(args)   # tjunta os argumentos entre virgulas
        result = result_local + temp0
        return result

    # URL da API que você deseja consumir


url = monta_url('USD-BRL', 'EUR-BRL', 'GBP-BRL')

response = requests.get(url)

if response.status_code == 200:
    # Convertendo a resposta para JSON, se aplicável
    data = response.json()
else:
    # Se a requisição falhou, imprima o código de status
    data = response.status_code


def init_app(app):
    app.config['RESP'] = data
