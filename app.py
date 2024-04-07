from flask import Flask
from dynaconf import FlaskDynaconf
from flask_bootstrap import Bootstrap5

from .pyrem.app.ext import buscar
from .pyrem.app.ext import buscar_dias
from .pyrem.app.blueprints import principal_views

app = Flask(__name__)

FlaskDynaconf(app)
bootstrap = Bootstrap5(app)

buscar.init_app(app, pob={'data':'USD-BRL','moedas':{'USD-BRL'}})

# tmp = ['USD_BRL']
buscar_dias.init_app(app,'USD-BRL')
principal_views.init_app(app)

# Resp = app.config['RESP']

# app.config = settings

# for item in settings.items():           # dict like iteration
#     print(item)

# for item in app.config.items():           # dict like iteration
#     print(item)

# print('RESP = ',Resp)


# @app.route('/')
# def index():
#     return f'<h1>{Resp}</m1>'


if __name__ == '__main__':
    app.run(debug=True)
