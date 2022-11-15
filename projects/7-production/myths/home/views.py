from django.http import HttpResponse

def index(request):
  return HttpResponse("<h1>Hola mundo vil y malvado</h1>")