# Proyecto 3: Web Capturer

## Índice

[1. Creación de un dataset a partir de web](#1-creación-de-un-dataset-a-partir-de-web)  
[2. Gestión de excepciones](#2-gestión-de-excepciones)  
[3. Acciones de limpieza](#3-aciones-de-limpieza)  
[4. Almacenamiento de datos estructurados](#4-almacenamiento-de-datos-estructurados)  
[5. Acceso a Internet: librería urllib](#5-aceso-a-internet-librería-urllib)  
[6. Extracción de datos: librería beautifulsoup](#6-extracción-de-datos-librería-beautifulsoup)

## 1. Creación de un dataset a partir de web

- Captura (scraping) de datos resultado de una búsqueda en un website (a elegir)
- Extracción y manipulación de datos "brutos" para obtener un dataset "limpio"
- Almacenamiento del dataset en un nuevo fichero de texto en formato CSV

## 2. Gestión de excepciones

Una excepción es un error en tiempo de ejecución, que normalmente no es previsible en tiempo de codificación, de ahí que haya que "manejar" la excepción en caso de que ocurra:

    try:
      print(x)
    except:
      print("Ocurrió una excepción genérica")

Se pueden manejar los distintos tipos de excepciones predefinidas de forma separada:

    try:
      print(x)
    except NameError:
      print("No existe esa variable")
    except:
      print("Ocurrió una excepción genérica")

Realizar alguna operación en caso de que no haya excepciones que manejar:

    try:
      print(x)
    except:
      print("Ocurrió una excepción genérica")
    else:
      print("Todo va bien")

O realizar alguna operación en cualquiera de los casos (con o sin excepciones):

    try:
      print(x)
    except:
      print("Ocurrió una excepción genérica")
    finally:
      print("Todo terminó")

Al igual que en los condicionales y bucles, la anidación está permitida para distintas operaciones dependientes entre sí:

    try:
      f = open("dummy.txt")
      try:
        f.write("En un lugar de La Mancha")
      except:
        print("El fichero no se pudo escribir")
      finally:
        f.close()
    except:
      print("El fichero no se pudo abrir")

Por último, en tiempo de codificación se puede establecer el lanzamiento de excepciones voluntariamente:

    x = "hello"

    if not type(x) is int:
      raise TypeError("No es un número entero")

## 3. Acciones de limpieza

La captura de excepciones puede tener varios usos, además de depurar el código u ofrecer una alternativa al usuario ante posibles efectos adversos de la aplicación.

Uno de ellos es lo que en programación se conoce como acciones de limpieza, que son aquellas que deben ejecutarse siempre, sean cuales sean los resultados, tras haber hecho ciertas operaciones previamente.

Un buen ejemplo de estas operaciones podría ser la apertura de ficheros, de bases de datos o de cualquier recurso compartido en general. En estos casos, los accesos abiertos deben ser cerrados.

Para ello, el lugar adecuado para hacerlo es en la cláusula finally del try-except:

    def div(a,b):
      try:
        q = a//b

      # División por cero
      except ZeroDivisionError:
        print("No se puede dividir por cero")
    
      # Si todo va bien
      else:
        print("El resultado es", q)

      # Acción de limpieza
      finally:
        print("Operación terminada")

Si se prueba esta función con números, realizará la operación de división normalmente salvo si el segundo es un cero, en cuyo caso emitirá la excepción contemplada.

Sin embargo, si llega una excepción no contemplada, como por ejemplo:

    div(10, "2")

El intérprete realizará en primer lugar las acciones de limpieza del finally y después emitirá el error correspondiente, a diferencia de si se tratara de una excepción contemplada.

## 4. Almacenamiento de datos estructurados

Las estructuras de datos en memoria (listas, tuplas, diccionarios y conjuntos) pueden ser convertidas (o exportadas, si se prefiere) a ficheros de texto con un formato determinado, como por ejemplo JSON, CSV o XML:

### Ejemplo CSV
    
    import csv

    fields = ['Name', 'Type', 'Level']

    rows = [['Pikachu', 'Electric', '15'],
            ['Charmander', 'Fire', '20'], 
            ['Koffing', 'Poison', '10']]

    with open('pokedesk.csv', 'w') as f:
      write = csv.writer(f)
      
      write.writerow(fields)
      write.writerows(rows)

### Ejemplo JSON
    
    import json

    x = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }

    y = json.dumps(x)

    print(y)

## 5. Acceso a Internet: librería urllib

La librería urllib permite realizar peticiones http como si fuera un navegador web:

    import urllib.request

    response = urllib.request.urlopen('https://es.wikipedia.org/wiki/Kumano_Kodo')

    print(response.read())

Obtener las cabeceras de la respuesta:

    print(response.headers)

En caso de ser datos en formato JSON en lugar de HTML, "parsearlos" en un diccionario:

    from urllib.request import urlopen
    import json

    response = urlopen("https://futuramaapi.herokuapp.com/api/quotes?search=humans")

    body = response.read()

    quotes = json.loads(body)

    print(quotes)

Puede "trocear" URLs para obtener datos a partir de ellas (así como el efecto contrario):

    from urllib.parse import *

    splitUrl = urlsplit('https://futuramaapi.herokuapp.com/api/quotes?search=humans')
    print(splitUrl)

    print("\n")

    unSplitUrl = urlunsplit(splitUrl)
    print(unSplitUrl)

Si se trata de HTML, para convertir los datos ("chorro de bytes") en un string, hay que descodificarlos en el juego de caracteres adecuado:

    import urllib.request

    response = urllib.request.urlopen('https://es.wikipedia.org/wiki/Kumano_Kodo')

    body = response.read()
    
    # Es recomendable cerrar el flujo (stream) de datos
    response.close()

    decodedBody = body.decode("utf-8")

    print(decodedBody)

## 6. Extracción de datos: librería beautifulsoup

La librería beautifulsoup sirve para trabajar con grandes cadenas de texto que representan un código HTML, para buscar elementos que cumplan unas determinadas condiciones.

En combinación con la librería urllib, puede realizarse un proceso conocido como web scraping, que consiste en obtener datos "depurados" a partir de una URL online:

    import urllib.request
    from bs4 import BeautifulSoup

    # Petición urllib (ver ejemplo más arriba)
    # ...
    
    soup = BeautifulSoup(decodedBody, features='html.parser')

    topics = soup.find_all("span", "mw-headline")

    for topic in topics:
      print(topic.text)

## Referencias

[Manejo de excepciones](https://www.w3schools.com/python/python_try_except.asp)  
[Listado de excepciones predefinidas](https://www.w3schools.com/python/python_ref_exceptions.asp)  
[Acciones de limpieza](https://www.tutorialspoint.com/defining-clean-up-actions-in-python)  
[Conversión a JSON](https://www.w3schools.com/python/gloss_python_convert_into_JSON.asp)  
[Conversión a CSV](https://www.geeksforgeeks.org/python-save-list-to-csv/)  
[Librería urllib (I)](https://www.geeksforgeeks.org/python-urllib-module/)  
[Librería urllib (II)](https://realpython.com/urllib-request/)  
[Librería beautifulsoup (I)](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python)  
[Librería beautifulsoup (II)](https://aprendepython.es/pypi/scraping/beautifulsoup/)  
[Librería beautifulsoup (III)](https://realpython.com/beautiful-soup-web-scraper-python/)  
[Leer y escribir XML](https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/)