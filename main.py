from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<h1> Main Page </h1>'


@app.post('/perform_query')
def perform_foo():
    ...
    return app.response_class("", content_type="text/plain")


if __name__ == '__main__':
    app.run()
