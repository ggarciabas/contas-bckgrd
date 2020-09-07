"""
    Realizar teste da aplicação flask.
"""
from app import app_flask
from app import routes

def test_created_app ():
    """
        Testar a criação da aplicação.
    """
    assert app_flask.create_app() is not None

def test_route_index ():
    """
        Testar a rota padrão.
    """
    assert routes.index() == 'App Contas - Background'
