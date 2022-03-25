from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.update(ENV='development', DEBUG=True)


    # General blueprint
    from pystrong.views import general
    app.register_blueprint(general.mod)
    
    @app.errorhandler(404)
    def not_found(error):
        render = render_template('404.html', error=error)
        return render


    @app.errorhandler(500)
    def server_error(error):
        render = render_template('500.html', error=error)
        return render


    return app