from app import pystrong
from flask import render_template, redirect
from flask import url_for, flash

app = pystrong()


@app.route('/')
def hello():
    render = render_template('index.html')
    return render


if __name__ == '__main__':
    app.run()