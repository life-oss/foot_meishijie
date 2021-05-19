import flask
from flask import Flask

"""
    运行顺序
    首先运行get_data.py将所有的数据存到数据库当中
    再运行app.py将所有效果展示
"""

app = Flask(__name__)


# 前端页面
@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/cyclopedia')
def cyclopedia():
    return flask.render_template('cyclopedia.html')


@app.route('/show')
def show():
    return flask.render_template('show.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/bar')
def bar():
    return flask.render_template('echarts/bar.html')


@app.route('/pie')
def pie():
    return flask.render_template('echarts/pie.html')


@app.route('/ingredient1')
def ingredient1():
    return flask.render_template('wordcount/ingredient1.html')


@app.route('/ingredient2')
def ingredient2():
    return flask.render_template('wordcount/ingredient2.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8020)
