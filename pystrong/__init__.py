from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)
app.config.update(env="development")


"""
Import and register blue prints
"""
from pystrong.views import general
app.register_blueprint(general.mod)



"""
Manage page errors
"""
@app.errorhandler(404)
def not_found(error):
    render = render_template('404.html', error=error)
    return render


@app.errorhandler(500)
def server_error(error):
    render = render_template('500.html', error=error)
    return render