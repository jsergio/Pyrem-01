import requests
from ..ext import dt_final

def monta_url(**args):
    result = 'https://economia.awesomeapi.com.br/json/last/USD-BRL';
    # result = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    result_tmp = []
    if 'p2' in args:

        tmp = args['p2']
        print('Tmp = ',tmp)
        # Esse if a seguir, por enquato nao importa muito
        if 'data' in tmp:
            ldata = tmp['data'];
            result_tmp.append(f"{ldata}");
        
        # Esse if realiza a funcao de montar url
        if 'moedas' in tmp:    
            lmoedas = tmp['moedas'];
            list_moedas = []
            if type(lmoedas == 'dict'):
                print('É UM DICT !')
                for key in lmoedas:
                    if key in {'Dolar','Euro','Libra','Shekel'}:
                        list_moedas.append(lmoedas[key])
                    # list_moedas = lmoedas['key']
            print('Lista = ',list_moedas)    
            # result_tmp.append(f"{list_moedas}")
            # if(type(lmoedas) == 'dict'):
            # lista_values = lmoedas.values()
            # print('Lista1',lmoedas['dolar'])
            print('Tipo = ',type(lmoedas))
            print('Lmoedas = ',lmoedas)
            # print('List Moedas = ',list_moedas)
            result_local = result[0:-7]   # retira USD-BRL de result
            temp0 = ','.join(list_moedas)   # tjunta os argumentos entre virgulas
            result = result_local + temp0+'/';
            print('Result = ',result)
    return result

    # URL da API que você deseja consumir


def busca(**args):
    # url = monta_url(*args)
    
    if 'p1' in args:
        print('P1 = ',args['p1'])
        url = monta_url(p2=args['p1'])
    else:
        url = monta_url(pobj={'moedas':['USD-BRL', 'EUR-BRL', 'GBP-BRL']})
    
    print('URL = ',url);
    
    response = requests.get(url)

    if response.status_code == 200:
        # Convertendo a resposta para JSON, se aplicável
        data = response.json()
        # if args:
        #    data['moedas'] = args
    else:
        # Se a requisição falhou, imprima o código de status
        data = response.status_code
    
    return data

# def pega(moedas):
#     result = monta_url(moedas)
#     return {'data':data}

def init_app(app,**args):
    data = {'pob':{'Dolar':'USD:BRL'}}
    if 'pobj' in args:
        print('Pobj = ',args['pobj'])
        data = busca(p1=args['pobj'])
        # print('Data Final ',data)
        dt_res = dt_final.tratar(p=data)
        print('Dt-Res ',dt_res);
        return dt_res   
    app.config['RESP'] = data
    return data
