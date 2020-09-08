""" Arquivo de inicialização para o módulo app. """

import app.app_flask as app_flask
from app.registry import RegistryAPI
import app.routes as routes

def run ():
    """
        Criar e configurar app Flask
    """
    app = app_flask.create_app()
    app.add_url_rule('/', 'index', view_func=routes.index)
    
    registry_view = RegistryAPI.as_view('registry_api')
    app.add_url_rule('/registry/', view_func=registry_view, methods=['GET',])
    app.add_url_rule('/registry/', view_func=registry_view, methods=['POST',])
    app.add_url_rule('/registry/<int:reg_id>', view_func=registry_view,
                        methods=['GET', 'PUT', 'DELETE'])

    return app
