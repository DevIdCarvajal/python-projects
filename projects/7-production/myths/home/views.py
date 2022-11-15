from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User

def index(request):
  return HttpResponse("<h1>Hola mundo vil y malvado</h1>")

def home(request):
  if 'user' in request.session:
    current_user = request.session['user']
    param = {'current_user': current_user}
    
    return render(request, 'home.html', param)
  
  return HttpResponseRedirect(reverse('login'))

def signup(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    pwd = request.POST['pwd']
    
    if User.objects.filter(username=uname).count() == 0:
      user = User(username=uname, password=pwd)
      user.save()

      return HttpResponseRedirect(reverse('login'))
    
    return HttpResponse('El usuario ya existe')
  
  return render(request, 'signup.html')

def login(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    pwd = request.POST['pwd']

    check_user = User.objects.filter(username=uname, password=pwd)

    if check_user:
      request.session['user'] = uname

      return HttpResponseRedirect(reverse('home'))
    
    return HttpResponse('Datos incorrectos')

  return render(request, 'login.html')

def logout(request):
  try:
    del request.session['user']
  finally:
    return HttpResponseRedirect(reverse('login'))