from django.shortcuts import render, redirect
from movies.apis import RankApi
from datetime import datetime, timedelta
from movies.models import *

def ranks(request):
    daily_ranks = get_ranks(datetime.today() - timedelta(1), True)
    year_ago_ranks = get_ranks(datetime.today() - timedelta(364), True)
    weekly_ranks = get_ranks(datetime.today() - timedelta(7), False)

    if request.user.is_authenticated:
        user = request.user
        movies = user.like_movies.all()
        like_movies = [movie.cd for movie in movies]
        context = {
            'daily_ranks': daily_ranks,
            'year_ago_ranks': year_ago_ranks,
            'weekly_ranks': weekly_ranks,
            'like_movies': like_movies
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
    movie_thumbnail = request.POST.get('movie_thumbnail')
    if request.user.is_authenticated:
        user = request.user
        try:
            movie = Movie.objects.get(cd=movie_id)
            if user.like_movies.filter(id=movie.id).exists():
                user.like_movies.remove(movie)
            else:
                user.like_movies.add(movie)
        except Movie.DoesNotExist:
            movie = Movie(cd=movie_id, name=movie_name, thumbnail=movie_thumbnail)
            movie.save()
            user.like_movies.add(movie)
    return redirect('/movies/ranks/')

def movie_likes(request):
    user = request.user
    like_movies = user.like_movies.all()
    context = {
            'like_movies': like_movies
        }
    return render(request, 'like_list.html', context)


def get_ranks(target_date, is_day):
    if not Rank.objects.filter(date_week=is_day).filter(date=target_date).exists():
        save_rank(is_day, target_date)
    return Rank.objects.filter(date_week=is_day).filter(date=target_date)

def save_rank(is_day, target_date):
    api = RankApi()
    if is_day:
        api_ranks = api.get_day_ranks(target_date.strftime("%Y%m%d"))
    else:
        api_ranks = api.get_weekly_ranks(target_date.strftime("%Y%m%d"))

    for index, rank in enumerate(api_ranks):
        movie_thumbnail = api.get_naver_movie_api(rank['movieNm'])
        rank = Rank(cd=rank['movieCd'], date_week=is_day, rank=index+1, name=rank['movieNm'], date=target_date,
                    audi_cnt=rank['audiCnt'], audi_acc=rank['audiAcc'], thumbnail=movie_thumbnail)
        rank.save()