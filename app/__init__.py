import app.app_flask as app_flask

def run ():
    app = app_flask.create_app()

    @app.route('/')
    def index():
        return 'App Contas - Background'

    return app