from django.urls import path
from movies.views import ranks

urlpatterns = [
    path('ranks/', ranks)
]
