import os
from flask import Blueprint, render_template,request,jsonify

from ....app.ext import buscar_dias
from ....app.ext.tabelizar import obj_to_table
# Cria um objeto Blueprint
dias_bp = Blueprint('dias', __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/pyrem/app/blueprints/dias/'
    );


def nomeia(cod):
    codigos = {'USDBRL': 'Dolar', 'EURBRL': 'Euro', 'GBPBRL': 'Libra'}
    if cod in codigos:
        return codigos[cod]
    else:
        return ''


def init_app(app):
    var_geral = {}

    @dias_bp.route('/dias',methods=['GET','POST'])
    def dias():
        if request.method == 'POST':
            print('POST AQUÍ')
            data_obj = request.get_json();
            print('Data_OBJ = ',data_obj)
            url,vmoeda,vnum = data_obj['obj_res']
            print('URL = ',url);

            tmp = buscar_dias.init_app(app,url);
            tabela = obj_to_table([tmp,vmoeda,vnum])
            return jsonify(tabela);
        else:
          return render_template('dias.html', resp=var_geral)
       # app.register_blueprint(cotacao_bp)
    app.register_blueprint(dias_bp);