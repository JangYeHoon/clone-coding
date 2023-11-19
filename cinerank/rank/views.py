from django.shortcuts import render
from rank.apis import RankApi

def ranks(request):
    api = RankApi()
    daily_ranks = api.get_day_rank("20231025")
    context = {'daily_ranks': daily_ranks}
    return render(request, 'index.html', context)