from app import app_flask

def test_created_app ():
    assert app_flask.create_app() != None