# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def form_post():
    keyword = request.form["search_keyword"]
    return render_template("form_action.html", keyword=keyword)

app.debug = True
if __name__ == '__main__':
    app.run()
