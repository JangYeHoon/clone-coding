from django.shortcuts import render, redirect
from movies.apis import RankApi
from datetime import datetime, timedelta
from movies.models import *

def ranks(request):
    api = RankApi()

    yesterday_date = datetime.today() - timedelta(1)
    daily_ranks = api.get_day_ranks(yesterday_date.strftime("%Y%m%d"))

    year_ago_date = datetime.today() - timedelta(364)
    print(year_ago_date)
    year_ago_ranks = api.get_day_ranks(year_ago_date.strftime("%Y%m%d"))

    weekly_date = datetime.today() - timedelta(7)
    weekly_ranks = api.get_weekly_ranks(weekly_date.strftime("%Y%m%d"))

    if request.user.is_authenticated:
        user = request.user
        movies = user.like_movies.all()
        like_movies = [str(movie.cd) for movie in movies]
        print(like_movies)
        context = {
            'daily_ranks': daily_ranks,
            'year_ago_ranks': year_ago_ranks,
            'weekly_ranks': weekly_ranks,
            'like_movies': like_movies,
        }
    else:
        context = {
            'daily_ranks': daily_ranks,
            'year_ago_ranks': year_ago_ranks,
            'weekly_ranks': weekly_ranks
        }
    return render(request, 'index.html', context)

def movie_like(request, movie_id):
    movie_name = request.POST.get('movie_name')
    user = request.user
    try:
        movie = Movie.objects.get(cd=movie_id)
        if user.like_movies.filter(id=movie.id).exists():
            user.like_movies.remove(movie)
        else:
            user.like_movies.add(movie)
    except Movie.DoesNotExist:
        movie = Movie(cd=movie_id, name=movie_name)
        movie.save()
        user.like_movies.add(movie)
    return redirect('/movies/ranks/')