from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return redirect('/rank/ranks')
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/rank/ranks')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=email).exists():
            return render(request, 'signup.html')
        if password1 != password2:
            return render(request, 'signup.html')
        user = User.objects.create_user(
            username=email,
            password=password1,
        )
        login(request, user)
        return redirect('/rank/ranks')
    return render(request, 'signup.html')