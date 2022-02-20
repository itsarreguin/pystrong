from flask import Flask
import random


def pystrong():
    app = Flask(__name__)

    app.config.update(
        DEBUG=True,
        ENV='development'
    )

    return app


def generate_password():
    upper= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chars = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    merge = upper + lower + numbs + chars

    password = []

    for i in range(16):
        caracter_random = random.choice(merge)
        password.append(caracter_random)

    password = ''.join(password)
    return password


def run():
    password = generate_password()
    print(password)


if __name__ == '__main__':
    run()