"""
    Arquivo de inicialização para o módulo app.
"""

import app.app_flask as app_flask
import app.routes as routes

def run ():
    """
        Criar e configurar app Flask
    """
    app = app_flask.create_app()
    app.add_url_rule('/', 'index', view_func=routes.index)

    return app
