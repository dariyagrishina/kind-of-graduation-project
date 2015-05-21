# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from db import movie_search
app = Flask(__name__)


@app.route('/')
def first_page():
    search_query = request.args.get('search_query', '')
    movies = movie_search(search_query)
    number_of_movies = len(movies)

    found = u"Найдено"
    inflected_movie = u"фильмов"
    if number_of_movies == 1:
        found = u"Найден"
        inflected_movie = u"фильм"
    if (number_of_movies >= 2) and (number_of_movies <= 4):
        inflected_movie = u"фильма"

    return render_template("index.html", search_query=search_query, movies=movies,
                           number_of_movies=number_of_movies, found=found, inflected_movie=inflected_movie)


if __name__ == '__main__':
    app.run(debug=True)
