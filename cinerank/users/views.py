from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import requests

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8001/users/login/'
        data = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        # user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return redirect('/movies/ranks')
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/movies/ranks')

def signup_view(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8001/users/register/'
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'password2': request.POST.get('password2')
        }
        response = requests.post(url, data=data)
        if response.status_code == 201:
            return redirect('/movies/ranks')
        else:
            return redirect('/users/signup/')
    return render(request, 'signup.html')