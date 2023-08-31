from flask import Flask


def create_app():
    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = "Stats"

    register_blueprints(app)

    return app


def register_blueprints(app):
    """
    Registering the blueprints used by the flask app
    :param app: The flask app
    :return: None
    """
    from Stats.main.views import main
    from Stats.complex.views import complex_
    from Stats.simple.views import simple

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(complex_, url_prefix="/")
    app.register_blueprint(simple, url_prefix="/")
