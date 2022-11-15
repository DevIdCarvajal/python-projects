# Proyecto 7: Produciendo

## Índice

[1. Ejecutables en Python. Web dinámicas con Django](#1-ejecutables-en-python-web-dinámicas-con-django)  
[2. Compilación de ficheros .py](#2-compilación-de-ficheros-py)  
[3. Argumentos en ficheros ejecutables](#3-argumentos-en-ficheros-ejecutables)  
[4. Desarrollo web con Python-Django](#4-desarrollo-web-con-python-django)  
[5. Plantillas, modelos y vistas](#5-plantillas-modelos-y-vistas)  
[6. Formularios y vistas avanzadas. URLConf](#6-formularios-y-vistas-avanzadas-urlconf)  
[7. Desplegando Django](#7-desplegando-django)  
[8. Sesiones y usuarios en Django](#8-sesiones-y-usuarios-en-django)  
[9. Integración con bases de datos y aplicaciones](#9-integración-con-bases-de-datos-y-aplicaciones)  
[10. Seguridad](#10-seguridad)

## 1. Ejecutables en Python. Web dinámicas con Django

- Desarrollar una aplicación de agenda que permita al usuario gestionar sus citas, con las siguientes funcionalidades:
  - Crear cita
  - Borrar cita
  - Modificar cita
  - Ver todas las citas
  - Ver citas de un día concreto
  - Ver citas de un día y rango de horas concretos

  Las citas deberán tener los siguientes campos:
    - Fecha (DD/MM/AAAA)
    - Hora (HH:MM:SS)
    - Descripción

- Generar un fichero ejecutable de la aplicación, que pueda lanzarse de tres formas:
  - Sin argumentos: Al inicio, se mostrarán todas las citas
  - Recibiendo un argumento `day`: Al inicio, se mostrarán las citas de un día concreto
  - Recibiendo tres argumentos `day`, `starttime` y `endtime`: Al inicio, se mostrarán las citas de un día y rango de horas concretos

## 2. Compilación de ficheros .py

Es posible compilar un programa Python generando un ejecutable para un sistema operativo concreto mediante el programa `pyinstaller`:

    pip install pyinstaller

    pyinstaller --onefile holamundo.py

Además de las carpetas `build` y `dist` (siendo esta última donde reside el ejecutable generado), creará un fichero `.spec`, en el que se indica configuración extra para futuras compilaciones (e.g., rutas de ficheros de imagen, texto, etc.).

Otra opción multiplataforma es `nuitka`, aunque también se pueden usar las aplicaciones que compilan para plataformas concretas como `py2exe` en Windows, o `py2app` en MacOS.

## 3. Argumentos en ficheros ejecutables

Todo script Python puede recibir parámetros o argumentos de entrada cuando se interpreta (o ejecuta, en caso de ser un compilado para una plataforma concreta):

    python3 myscript.py arg1 arg2

Para acceder a dichos parámetros dentro del programa, se debe leer la lista `argv` del módulo `sys`, cuyo primer elemento será el propio nombre del script, y del segundo en adelante los parámetros recibidos:

    import sys

    print(f"Nombre del script: {sys.argv[0]}")
    print(f"Número de parámetros: {len(sys.argv)}")

    for i in sys.argv[1:]:
      print(i)

## 4. Desarrollo web con Python-Django

A continuación se detallan los pasos para crear una aplicación de "Hola Mundo" con Django, el framework de desarrollo web para Python:

1. (Opcional pero recomendable) Crear el entorno de desarrollo:

        virtualenv env-django
        source env-django/bin/activate

2. Instalar el paquete:

        pip install django

3. Crear el proyecto mediante el CLI de Django:

        django-admin startproject myths

4. Arrancar el servidor web local de desarrollo de Django en la carpeta del proyecto recién creado:
        
        cd myths
        python3 manage.py runserver

5. (Opcional) Para cambiar el idioma, abrir el fichero de configuración `settings.py` y editarlo:
        
        LANGUAGE_CODE = 'es-es'

6. Aplicar las migraciones pertinentes (creación de tablas SQL en base de datos):
        
        python3 manage.py migrate

7. Crear una aplicación de ejemplo:
        
        python3 manage.py startapp home

8. Dentro de la carpeta generada, editar la primera línea del fichero `views.py`:
        
        from django.http import HttpResponse

        def index(request):
          return HttpResponse("<h1>Hola mundo</h1>")

9. En la carpeta del proyecto ( `myths` ), editar `urls.py`:
        
        from django.contrib import admin
        from home import views
        from django.urls import path

        urlpatterns = [
          path('', views.index, name="index"),
          path('admin/', admin.site.urls),
        ]

## 5. Plantillas, modelos y vistas

*Nota: En los ejemplos siguientes, se asume que se está trabajando con una aplicación previamente creada mediante:*

    python3 manage.py startapp bestiarium

### Vistas y plantillas

Las vistas de una aplicación son las funciones que generan la respuesta http que se enviará de vuelta al cliente, y que pueden hacerlo enviando un string que expresa texto HTML:

    from django.http import HttpResponse
    
    def index(request):
      return HttpResponse('<h1>Bestiarium</h1><p><a href="list">Ver criaturas</a></p>')

O como una plantilla, que es un fichero `.html` alojado en una subcarpeta de la aplicación llamada `templates/`, e importado de este modo:

    from django.http import HttpResponse
    from django.template import loader

    def indexWithTemplate(request):
      template = loader.get_template('index.html')
      return HttpResponse(template.render())

Además, es necesario añadir la aplicación a las `settings.py` del proyecto:

    INSTALLED_APPS = [
      ...
      'bestiarium.apps.BestiariumConfig',
    ]

Para incluir ficheros estáticos (e.g., CSS, JS o imágenes), estos se deben alojar en una subcarpeta de la aplicación llamada `static/`, y llamarlos en la plantilla de la siguiente manera:

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
      ...

      <link rel="stylesheet" href={% static "css/style.css" %}>
    </head>
    <body>
      ...
      <img src={% static "img/chimera.jpg" %} alt="Quimera">
      ...
    </body>
    </html>

### Modelos

Los modelos en Django son abstracciones de la información almacenada en base de datos, lo que permite crear los esquemas así como realizar las operaciones CRUD de lectura y escritura correspondientes.

Para crear un modelo se debe crear una clase que extienda de `models.Model` en el fichero `models.py`:

    from django.db import models

    class Creatures(models.Model):
      name = models.CharField(max_length=255)
      image = models.CharField(max_length=255)
      weight = models.IntegerField()

Y después crear las migraciones correspondientes y aplicarlas:

    python3 manage.py makemigrations bestiarium

    python3 manage.py migrate

Para poblar las tablas, se puede hacer desde una *shell* de Python:

    python3 manage.py shell

Una vez dentro, se pueden lanzar los métodos específicos de `QuerySet` para trabajar con los modelos:

    >>> from bestiarium.models import Creatures

    >>> creature = Creatures(name="Quimera",image="chimera.jpg",weight=1800)
    >>> creature.save()

    >>> Creatures.objects.all().values()

## 6. Formularios y vistas avanzadas. URLConf

### Vistas avanzadas

Django ofrece una buena colección de directivas para construir las vistas del lado del servidor (*server-side rendering*), mediante variables, condicionales, bucles, etc.

Las variables se expresan mediante dobles llaves ( `{{ ... }}` ) y se pueden definir en la plantilla:

    {% with copy="Myths &amp; Legends, Inc." %}
    <small>&copy;, {{ copy }}</small>
    {% endwith %}

O en el fichero de vistas ( `views.py` ), estableciendo los datos literalmente o cargándolos del modelo:

    from django.http import HttpResponse
    from django.template import loader
    from .models import Creatures

    def indexWithTemplate(request):
      template = loader.get_template('index.html')
      
      # QuerySet
      creatures = Creatures.objects.all().values()
      context = {
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit.',
        'creatures': creatures
      }

      return HttpResponse(template.render(context, request))

En cuanto a la lógica de presentación, esta se puede establecer en las plantillas con bucles, condicionales, usando filtros, etc.:

    <!-- If there are creatures -->
    {% if creatures|length > 0 %}
    <div class="flex">
      {% for c in creatures %}
        <div class="creature">
        {% with 'img/'|add:c.image as src %}
          <img src={% static src %} alt={{ c.name }}>
          <br>
          Peso: {{ c.weight }} 
        {% endwith %}
        </div>
      {% endfor %}
    </div>
    {% else %}
    <p>No hay criaturas</p>
    {% endif %}

### Formularios

Django facilita las operaciones típicas que requiere la construcción y procesamiento de formularios HTML, proporcionando algunas clases y *helpers* específicos.

En primer lugar se debe crear un fichero `forms.py` dentro de la carpeta de la aplicación ( `bestiarium/` ) para especificar formato y condiciones de validación de los campos:

    from django import forms

    class CreaturesForm(forms.Form):
      name = forms.CharField(max_length=255, label="Criatura")
      image = forms.CharField(max_length=255, label="Imagen")
      weight = forms.IntegerField(label="Peso")

*Nota: Existen muchos tipos de campos con sus opciones correspondientes, así como otras más genéricas (e.g., `value` o `required`), e incluso es posible crear el formulario directamente del modelo.*

El siguiente es crear una vista en `views.py` que importe la clase creada y renderice el formulario en HTML en el fichero de la plantilla correspondiente (e.g., `add.html`):

    from django.shortcuts import render
    from .forms import CreaturesForm

    def add(request):
      form = CreaturesForm()
      return render(request, 'add.html', {"addform": form})

Enrutándola debidamente en `urls.py`:

    urlpatterns = [
      ...
      path('add/', views.add, name='add'),
    ]

Para la plantilla, simplemente se debe llamar a la variable `addform` creada el formulario, opcionalmente con un contenedor para los campos (e.g., `as_p` genera párrafos para envolverlos):

    <form action="addcreature/" method ="post">
      {% csrf_token %}
      {{ addform.as_p }}
      <input type="submit" value="Crear">
    </form>

*Nota: El tag `{% csrf_token %}` es obligatorio cuando el método es POST, y sirve para que Django maneje los posibles ataques CSRF*

Por último, hay que procesar el formulario una vez enviado, lo que implica acceder a los datos recibidos, procesarlos dependiendo de cada caso (almacenar en el caso de POST, por ejemplo) y finalmente indicar una redirección al navegador.

Para ello, hay que enrutar en `urls.py` el `action` indicado en el formulario ( `addcreature/` ) con la función en el fichero de vistas que realizará todo el proceso ( `addcreature` ):

    path('add/addcreature/', views.addcreature, name='addcreature'),

Y en el fichero de vistas añadir dicha función:

    from django.http import HttpResponse, HttpResponseRedirect
    from django.urls import reverse
    
    def addcreature(request):
      name = request.POST['name']
      image = request.POST['image']
      weight = request.POST['weight']

      creature = Creatures(name=name, image=image, weight=weight)
      creature.save()

      return HttpResponseRedirect(reverse('index'))

### URLConf

En cuanto al enrutamiento de URLs de Django, conocido como URLConf, simplemente hay que crear una lista de `paths` en el fichero `urls.py` de la aplicación a enrutar:

    # bestiarium/urls.py
    
    from django.urls import path
    from . import views

    urlpatterns = [
      path('', views.index, name='index'),
      path('list/', views.indexWithTemplate, name='indexWithTemplate'),
    ]

E importar (o incluir) esas rutas en el `urls.py` global del proyecto:

    # myths/urls.py
    
    ...
    from django.urls import path, include

    urlpatterns = [
      ...
      path('bestiarium/', include('bestiarium.urls')),
      ...
    ]

También se pueden establecer patrones con expresiones regulares para un enrutamiento avanzado.

## 7. Desplegando django

Existen varias formas de desplegar un proyecto desarrollado con Django, pero en todas ellas es necesaria la presencia de un servidor web (e.g., Apache Web Server) y una interfaz de comunicación entre el servidor y el framework.

Los siguientes pasos son los que hay que realizar para un despliegue con la aplicación uWSGI basada en la interfaz WSGI y nginx como servidor web.

*Nota: Si bien es opcional, es conveniente trabajar siempre en un entorno virtual, máxime siendo una máquina de producción, para después una vez probado y comprobado que funciona correctamente, pasar al entorno real de Python.*

En primer lugar, instalar el paquete:

    pip install uwsgi

Verificar que la aplicación funciona correctamente:

    python manage.py runserver

Lanzar la aplicación vía `uwsgi` para comprobar que la puede servir por `http://localhost:8000/`, que hará de interfaz intermedia con `nginx`:

    uwsgi --http :8000 --module myths.wsgi

Habiéndose instalado previamente `nginx` en la máquina, se debe crear un fichero de configuración `myths_nginx.conf`:

*Nota: Dado que este paso depende de cada sistema operativo, a partir de este punto se asumirá que se está trabajando en un Linux Debian 11.*

    upstream django {
      server 127.0.0.1:8001;
    }

    server {
      listen                8000;
      server_name           localhost;
      charset               utf-8;
      client_max_body_size  75M;

      location /media  {
        alias /<ruta_a_la_carpeta_del_proyecto>/myths/media;
      }

      location /static {
        alias /<ruta_a_la_carpeta_del_proyecto>/myths/static;
      }
      
      location / {
        uwsgi_pass django;
        include /<ruta_a_la_carpeta_del_proyecto>/myths/uwsgi_params;
      }
    }

A continuación se debe crear un enlace simbólico a producción:

    sudo ln -s /etc/nginx/sites-available/myths_nginx.conf /etc/nginx/sites-enabled/

Después hay que recolectar todos los ficheros estáticos, añadiendo a `settings.py`:

    import os

    ...

    STATIC_ROOT = os.path.join(BASE_DIR, "static/")

Y ejecutar lo siguiente:

    python manage.py collectstatic

Tras reiniciar nginx:

    sudo systemctl restart nginx

Se puede levantar el servidor de nuevo pero esta vez en modo producción ( `cliente web` <-> `servidor web` <-> `socket` <-> `uWSGI` <-> `Python` ):

    uwsgi --socket myths.sock --module myths.wsgi --chmod-socket=664

## 8. Sesiones y usuarios en django

.

## 9. Integración con bases de datos y aplicaciones

Cada sistema gestor de base de datos tiene sus propias particularidades, así que a modo de ejemplo concreto se van a dar a continuación los pasos para conectar Django con MySQL.

*Nota: Se asume que ya existe el proyecto creado previamente y, aunque no es obligatorio pero sí conveniente, se está trabajando en un entorno virtual.*

En primer lugar instalar el *driver* o conector correspondiente:

    pip install mysqlclient

Modificar la configuración de `DATABASES` en el fichero `settings.py` (sustituyendo `mydb`, `root` y `admin` por lo que proceda en cada caso):

    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':'3306',
      }
    }

Hacer las migraciones correspondientes:

    python manage.py makemigrations

    python manage.py migrate

## 10. Seguridad

.

## Referencias

[Generación de ejecutables (I)](https://www.pythonparatodo.com/?p=74)  
[Generación de ejecutables (II)](https://codigofacilito.com/articulos/archivos-ejecutables-python)  
[Documentación pyinstaller: Fichero spec](https://pyinstaller.org/en/stable/spec-files.html)  
[Argumentos por línea de comandos](https://www.pythonforbeginners.com/system/python-sys-argv)  
[Crea tu primera web con Django](https://medium.com/@rickyp.11107/crea-tu-primera-web-con-django-2d0876321f6f)  
[Introducción a Django y MVC](https://pythondiario.com/tutorial-django-desde-cero)  
[Tutorial Django](https://www.w3schools.com/django/index.php)  
[Formularios con Django](https://www.geeksforgeeks.org/django-forms/)  
[Enrutamiento con URLConf](https://data-flair.training/blogs/django-urls-and-urlconf/)  
[Desplegar un proyecto Django con uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)  
[Documentación Django: Despliegue](https://docs.djangoproject.com/en/4.1/howto/deployment/)  
[]()  
[Integración de Django con MySQL](https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/)  
[Documentación Django: Bases de datos](https://docs.djangoproject.com/en/4.1/ref/databases/)  
[]()