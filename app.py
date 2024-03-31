#!/usr/bin/python
# -*- coding: utf-8 -*-
# @ 南无阿弥陀佛，不要有太多bug……
# @ Author: tukechao
# @ Date: 2024-03-31 19:16:01
# @ LastEditors: tukechao
# @ LastEditTime: 2024-03-31 19:21:20
# @ FilePath: /shellauction-net-tool/app.py
# @ description:意拍查询站后台程序

from flask import Flask
from search_engine import search_engine

app = Flask(__name__)
app.register_blueprint(search_engine, url_prefix="/search/")


@app.route("/")
def home():
    return "欢迎来到我的Flask网站!"


if __name__ == "__main__":
    app.run(debug=True)
