from app import pystrong

app = pystrong()


@app.route('/')
def hello():
    return 'Hello Pystrong'


if __name__ == '__main__':
    app.run()