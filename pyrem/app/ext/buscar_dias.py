import requests
from datetime import datetime



def monta_resp(param):
    
    result_geral = {}

    sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

    for iten in param:
        result = {}
        # print('AQUI')
        if 'code' in iten:
            tmp = iten['code'];
            # print('TMP ',tmp)
            tmp = tmp + '-'+ iten['codein'];
            result['code'] = tmp;
            # print('TMP2 -> ',tmp)
        result['bid']=iten['bid']
        tstamp = int(iten['timestamp'])
        
        t2 = datetime.fromtimestamp(tstamp)
        # num = date.today().weekday()
        format = '%d-%m-%Y'  
        result['date']=t2.strftime(format)
        result['sem']= sem[t2.weekday()]
        format = '%H:%M'
        result['hora']=t2.strftime(format)
        result_geral[result['date']]=result
    print('Result Geral -> ',result_geral)
    return result_geral
    
def busca__url(url):
        
    # url = url_base 

    response = requests.get(url)
    
    if response.status_code == 200:
        
        # Convertendo a resposta para JSON, se aplicável
        resp = response.json()
        print('RESP -> ',resp)
        data = monta_resp(resp)
        print('\nResultado',data)        
    else:
        # Se a requisição falhou, imprima o código de status
        # print('Falha na requisição:', response.status_code)
        data = {}['status'] = response.status_code
    return data

def init_app(app,murl):
    print('Moeda -> ',ModuleNotFoundError)
    # resp é a cotacao da moeda nos dias escolhidos. E formatada.
    resp = busca__url(murl)
    print('RESP FINAL -> ',resp)
    return resp
    # print('NDIA -> ',ndia)
    # app.config['RESP_DIAS'] = busca__url(moeda,ndia)
