from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        print('post')
        return render(request, 'login.html')
    else:
        print('just')
        return render(request, 'login.html')