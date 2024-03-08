from requests import get

url_cota = 'https://economia.awsomeapi.com.br/last/json/USD-BRL,EUR-BRL'
cota_hoje = get(url_cota)
print(dict(cota_hoje))
