from flask import Blueprint
from flask import render_template, url_for

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    render = render_template('index.html')
    return render


@mod.route('/contact')
def contact():
    render = render_template('contact.html')
    return render