from django.urls import path
from rank.views import ranks

urlpatterns = [
    path('ranks/', ranks)
]
