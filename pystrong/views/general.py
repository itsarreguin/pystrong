from flask import Blueprint
from flask import render_template, url_for, flash

mod = Blueprint('general', __name__)


@mod.route('/', methods=('GET', 'POST'))
def index():
    render = render_template('index.html')
    return render


@mod.route('/contact')
def contact():
    render = render_template('contact.html')
    return render