from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

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
    else:
        print('just')
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/rank/ranks')