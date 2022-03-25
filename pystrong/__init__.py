from flask import Flask
from flask import render_template, url_for


def create_app():
    
    app = Flask(__name__)
    app.config.update(env="development")


    # General blue prints
    from pystrong.views import general
    app.register_blueprint(general.mod)
    
    
    return app