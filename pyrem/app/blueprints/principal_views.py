import os
from flask import Blueprint, render_template


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
    # print(resp)
    var_geral = {}
    for key, val in resp.items():
        variavel = {
            'nome_moeda': nomeia(key),
            'valor_moeda': val['bid'],
            'hora': val['create_date'][-9:],
            'dia': val['create_date'][0:-9],
        }
        # Guarda na variavel var_geral essa variavel
        var_geral[key] = variavel

    print('VARIAVEL = ', var_geral)
    print('\nResp = ', resp)

    @cotacao_bp.route('/moedas')
    def cotacao():
        return render_template('cotacao.html', resp=var_geral)

    @cotacao_bp.route('/')
    def teste_dt():
        return render_template('teste_dt.html')

    @cotacao_bp.route('/b')
    def teste2():
        return render_template('teste02.html')

    @cotacao_bp.route('/c')
    def teste3():
        return render_template('teste03.html')
    
    @cotacao_bp.route('/a')
    def example_dt():
        return render_template('exemple_dt.html')

    # Registra o Blueprint no aplicativo Flask
    app.register_blueprint(cotacao_bp)
