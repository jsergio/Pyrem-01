import os
from flask import Blueprint, render_template, request, jsonify

from ..ext import buscar

# Cria um objeto Blueprint
tmp = os.path.abspath('pyrem/app/blueprints/templates')

cotacao_bp = Blueprint(
    'cotacao', __name__, template_folder=tmp, static_folder='static'
)


def nomeia(cod):
    codigos = {'USDBRL': 'Dolar', 'EURBRL': 'Euro', 'GBPBRL': 'Libra'}
    if cod in codigos:
        return codigos[cod]
    else:
        return ''


def init_app(app):
    resp = app.config['RESP']
    print('Pricipal Views ',resp)
    # print(resp)
    var_geral = {}
    # for key, val in resp.items():
    #     variavel = {
    #         'nome_moeda': nomeia(key),
    #         'valor_moeda': val['bid'],
    #         'hora': val['create_date'][-9:],
    #         'dia': val['create_date'][0:-9],
    #     }
    #     # Guarda na variavel var_geral essa variavel
        # var_geral[key] = variavel

    # print('VARIAVEL = ', var_geral)
    # print('\nResp = ', resp)

    @cotacao_bp.route('/moedas')
    def cotacao():
        return render_template('cotacao.html', resp=var_geral)

    @cotacao_bp.route('/')
    def teste_dt():
        return render_template('teste_dt.html')

    @cotacao_bp.route('/b', methods=['GET', 'POST'])
    def teste2():
        if request.method == 'POST':

           data = request.get_json();

           print('Data = ',data);

           tmp = buscar.init_app(app,pobj=data);
     
           return jsonify(response=tmp); 
        #    return data           
        else:
            moedas = {'Dolar':'USD-BRL','Euro':'EUR-BRL','Libra':'GBP-BRL'}
            return render_template('teste2b.html',moedas=moedas)
    
    @cotacao_bp.route('/d')
    def teste0():
        return render_template('teste00.html')

    @cotacao_bp.route('/c')
    def teste3():
        return render_template('teste3b.html')
    
    @cotacao_bp.route('/a')
    def example_dt():
        return render_template('exemple_dt.html')

    @cotacao_bp.route('/data', methods=['GET','POST'])
    def get_data():
      if request.method == 'GET':
         # Aqui você pode retornar uma página HTML
         return render_template('teste01.html')
      elif request.method == 'POST':
            # Recebendo os dados enviados pelo cliente
            data_from_client = request.json

            # Manipulando os dados
            processed_data = {}
            for key, value in data_from_client.items():
                processed_data[key] = value.upper()

            # Preparando a resposta para o cliente
            response_data = {'processed_data': processed_data}

            # Retornando a resposta no formato JSON
            return jsonify(response_data)

            # Registra o Blueprint no aplicativo Flask
            app.register_blueprint(cotacao_bp)
    app.register_blueprint(cotacao_bp)