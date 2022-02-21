from app import pystrong
from flask import render_template, redirect
from flask import url_for, flash

app = pystrong()


@app.route('/')
def index():
    render = render_template('index.html')
    return render

@app.errorhandler(404)
def not_found(error):
    render = render_template('404.html', error=error)
    return render


if __name__ == '__main__':
    app.run()