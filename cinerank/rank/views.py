from django.shortcuts import render
from rank.apis import RankApi
from datetime import datetime, timedelta

def ranks(request):
    api = RankApi()

    yesterday_date = datetime.today() - timedelta(1)
    daily_ranks = api.get_day_ranks(yesterday_date.strftime("%Y%m%d"))

    year_ago_date = datetime.today() - timedelta(365)
    year_ago_ranks = api.get_day_ranks(year_ago_date.strftime("%Y%m%d"))

    weekly_date = datetiem.today() - timedelta(7)
    weekly_ranks = api.get_weekly_ranks(weekly_date.strftime("%Y%m%d"))

    context = {
        'daily_ranks': daily_ranks,
        'year_ago_ranks': year_ago_ranks,
        'weekly_ranks': weekly_ranks,
    }
    return render(request, 'index.html', context)
