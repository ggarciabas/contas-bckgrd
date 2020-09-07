import app.app_flask as app_flask

app = app_flask.create_app()

@app.route('/')
def hello_world():
    return 'App Contas - Background'