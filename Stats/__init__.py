from flask import Flask


def create_app():
    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = "Stats"

    from Stats.main.views import main
    from Stats.normal.views import normal

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(normal, url_prefix="/distributions")

    return app
