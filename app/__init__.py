from flask import Flask


def pystrong():
    app = Flask(__name__)

    app.config.update(
        DEBUG=True,
        ENV='development'
    )

    return app