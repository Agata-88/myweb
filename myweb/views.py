from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.
'''
Functions below specify .html files which will be displayed when specific function is called.
'''
def index(request):
    return render(request, "index.html")

def history(request):
    return render(request, "history.html")

def links(request):
    return render(request, "links.html")

def shop(request):
    return render(request, "shop.html")

def login(request):
    return render(request, "login.html")
'''
authenticate_user function requestes username and login from the user and authenticate
input based on the information from the database.
'''
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('login')
)
    else:
        #(request, '')
        return HttpResponseRedirect(
            reverse('shop')
)

def show_user(request):
    print(request.user.username)
    return render(request, 'shop.html', {
        "username": request.user.username,
        "password": request.user.password
})

def register(request):
    return render (request, 'register.html')
