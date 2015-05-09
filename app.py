# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def first_page():
    search_query = request.args.get('search_query', '')
    return render_template("index.html", search_query=search_query)


if __name__ == '__main__':
    app.run(debug=True)
