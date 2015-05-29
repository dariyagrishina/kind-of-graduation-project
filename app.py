# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from db import movie_search
app = Flask(__name__)


@app.route('/')
def first_page():
    search_query = request.args.get('search_query', '')
    movies = movie_search(search_query)
    return render_template("index.html", search_query=search_query, movies=movies)


# R: используй декоратор, чтобы зарегистрировать фильтр, так сразу будет видно,
#    что ты делаешь, а не потом. Кроме того, можно избежать повторения имени.
def plural_filter(number_of_movies, single, plural_1, plural_2):
    # R: реализация корректная, но далеко не лучшая.
    #    Чтобы получить цифры числа следует использовать деление на 10 с остатком.
    reversed_number = str(number_of_movies)[::-1]
    if reversed_number[0:1] == '1' and reversed_number[0:2] != "11":
        return single
    if reversed_number[0:1] in ["2", "3", "4"] and reversed_number[1:2] !="1":
        return plural_1
    return plural_2

app.jinja_env.filters['plural'] = plural_filter


if __name__ == '__main__':
    app.run(debug=True)
