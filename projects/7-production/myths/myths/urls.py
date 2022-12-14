from django.contrib import admin
from home import views
from django.urls import path, include

urlpatterns = [
  path('', views.index, name="index"),
  path('home/', include('home.urls')),
  path('bestiarium/', include('bestiarium.urls')),
  path('admin/', admin.site.urls),
]
