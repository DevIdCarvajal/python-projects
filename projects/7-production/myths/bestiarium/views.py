from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Creatures
from .forms import CreaturesForm

def index(request):
  return HttpResponse('<h1>Bestiarium</h1><p><a href="list">Ver criaturas</a></p>')

def indexWithTemplate(request):
  template = loader.get_template('index.html')
  
  # QuerySet
  creatures = Creatures.objects.all().values()
  context = {
    'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit.',
    'creatures': creatures
  }

  return HttpResponse(template.render(context, request))

def add(request):
  form = CreaturesForm()
  return render(request, 'add.html', {"addform": form})

def addcreature(request):
  name = request.POST['name']
  image = request.POST['image']
  weight = request.POST['weight']

  creature = Creatures(name=name, image=image, weight=weight)
  creature.save()

  return HttpResponseRedirect(reverse('index'))
