import os
from flask import Blueprint, render_template,request

# from ..ext import buscar

# Caminhos absolutos: templates e satic
templ_abs = os.path.abspath('pyrem/app/blueprints/init/templates')
stati_abs = os.path.abspath('static')

print('Locais Template e Static',templ_abs, stati_abs)

# Cria um objeto Blueprint
init_bp = Blueprint('init', __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/pyrem/app/blueprints/init'
    );


def nomeia(cod):
    codigos = {'USDBRL': 'Dolar', 'EURBRL': 'Euro', 'GBPBRL': 'Libra'}
    if cod in codigos:
        return codigos[cod]
    else:
        return ''


def init_app(app):
    # resp = app.config['RESP']
    # print('Pricipal Views ',resp)
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

    @init_bp.route('/init')
    def init():
        return render_template('init.html', resp=var_geral)
       # app.register_blueprint(cotacao_bp)
    app.register_blueprint(init_bp);