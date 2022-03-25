from flask import Blueprint
from flask import render_template, url_for, flash


mod = Blueprint('general', __name__)


@mod.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')