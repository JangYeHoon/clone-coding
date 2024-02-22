from django.urls import path
from movies.views import ranks, movie_like

urlpatterns = [
    path('ranks/', ranks),
    path('<int:movie_id>/like/', movie_like),
]
