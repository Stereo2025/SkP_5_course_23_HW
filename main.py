from flask import Flask, request, abort
from config import FileNotFound
from config import DATA_DIR

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<h1> Main Page </h1>'


@app.post('/perform_query')
def perform_foo():
    try:
        cmd1 = request.args.get('cmd1')
        cmd2 = request.args.get('cmd2')
        value1 = request.args.get('value1')
        value2 = request.args.get('value2')

    except ValueError:
        abort(404)
    try:
        if not DATA_DIR:
            return FileNotFound
        with open(DATA_DIR) as file:
            ...
    except:
        ...

    return app.response_class("", content_type="text/plain")


if __name__ == '__main__':
    app.run()
