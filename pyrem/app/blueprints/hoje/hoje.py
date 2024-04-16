from flask import Blueprint, render_template,request,jsonify

from ....app.ext import buscar
# from ....app.ext.tabelizar import obj_to_table
# Cria um objeto Blueprint
hoje_bp = Blueprint('hoje', __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/pyrem/app/blueprints/hoje'
    );


# def nomeia(cod):
#     codigos = {'USDBRL': 'Dolar', 'EURBRL': 'Euro', 'GBPBRL': 'Libra'}
#     if cod in codigos:
#         return codigos[cod]
#     else:
#         return ''


def init_app(app):
    var_geral = {}

    @hoje_bp.route('/hoje',methods=['GET','POST'])
    def hoje():
        if request.method == 'POST':
            print('POST AQUÍ')
            data_obj = request.get_json();
            print('Data_OBJ = ',data_obj)
            url,vmoeda,vnum = data_obj['obj_res']
            print('URL = ',url);

            tmp = buscar.init_app(app,url);
            # tabela = obj_to_table([tmp,vmoeda,vnum])
            return jsonify(tmp);
        else:
          return render_template('hoje.html', resp=var_geral)
       # app.register_blueprint(cotacao_bp)
    app.register_blueprint(hoje_bp);