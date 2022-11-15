from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('list/', views.indexWithTemplate, name='indexWithTemplate'),
  path('add/', views.add, name='add'),
  path('add/addcreature/', views.addcreature, name='addcreature'),
]
