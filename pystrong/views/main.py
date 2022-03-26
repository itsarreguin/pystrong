from flask import Blueprint
from flask import render_template, url_for, flash, request
from time import sleep
import random


mod = Blueprint('general', __name__)


@mod.route('/', methods=('GET', 'POST'))
def index():
    upper = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'
    ]

    lower = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'
    ]

    numbs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = [
        '*', '+', '/', '@', '¿', '?', '¡', '!', '[', '{', '(', ')', '}', ']', '|', '>', '<', '&', '$', '#', '='
    ]

    create = upper + lower + numbs + symbols

    password = list()


    if request.method == 'POST':

        if request.form.get('generate') == 'generate-btn':
            for _ in range(20):
                select_rand = random.choice(create)
                password.append(select_rand)
            password = ''.join(password)

        elif request.form.get('clear') == 'clear-btn':
            password.clear()

        flash(password)

    return render_template('main/index.html')