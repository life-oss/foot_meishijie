import flask
from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return flask.render_template('./wordcount/ingredient1.html')


@app.route('/')
def a():
    return flask.render_template('index.html')


@app.route('/cyclopedia')
def b():
    return flask.render_template('cyclopedia.html')


@app.route('/show')
def c():
    return flask.render_template('show.html')


@app.route('/bar')
def e():
    return flask.render_template('echarts/bar.html')


@app.route('/pie')
def f():
    return flask.render_template('echarts/pie.html')


@app.route('/ingredient1')
def g():
    return flask.render_template('wordcount/ingredient1.html')


@app.route('/ingredient2')
def h():
    return flask.render_template('wordcount/ingredient2.html')


@app.route('/about')
def d():
    return flask.render_template('about.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8020)
