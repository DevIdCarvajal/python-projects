# Proyecto 2: Gestión de librería

## Índice

[1. Requerimientos de cliente](#1-requerimientos-de-cliente)  
[2. Funciones lambda](#2-funciones-lambda)  
[3. Operaciones sobre listas, tuplas, diccionarios y conjuntos](#3-operaciones-sobre-listas-tuplas-diccionarios-y-conjuntos)  
[4. Creando módulos con nuestras funciones. Importando módulos](#4-creando-módulos-con-nuestras-funciones-importando-módulos)  
[5. Módulos estándar de Python](#5-módulos-estándar-de-python)  
[6. Paquetes. Importación](#6-paquetes-importación)  
[7. Formateo de la información de salida](#7-formateo-de-la-información-de-salida)  
[8. Lectura y escritura en disco](#7-lectura-y-escritura-en-disco)

## 1. Requerimientos de cliente

- Gestión de Autores (CRUD):
  - Crear Autor (id, Nombre, Apellidos)
  - Actualizar Autor por id (Nombre y/o Apellidos)
  - Borrar Autor por id
  - Obtener datos de Autor por id
  - Obtener datos de todos los Autores
- Gestión de Libros (CRUD):
  - Crear Libro (ISBN, Título, Año, idAutor)
  - Actualizar Libro por ISBN (Título, Autor y/o Año)
  - Borrar Libro por ISBN
  - Obtener datos de Libro por ISBN
  - Obtener datos de Libros por idAutor

## 2. Funciones lambda

Son funciones anónimas definidas "en una línea", es decir, de una sola expresión que normalmente se emplean en casos en los que se necesita un cálculo puntual por un breve periodo de tiempo.

Siguiendo las técnicas del paradigma de la programación funcional, los casos habituales de uso de las funciones lambda serían:

- Almacenarlas en una variable en caso de querer ser reutilizadas:

    ```
    levelUp = lambda level : level + 1
    print(levelUp(8))

    concatenateWithColon = lambda string1, string2 : f"{string1}:{string2}"
    print(concatenateWithColon(4,7))
    ```

- Pasarlas como parámetros a otras funciones como "callbacks":

    ```
    def calculateWithLambda(valor1, valor2, operatorFunction):
        return operatorFunction(valor1, valor2)

    print(calculateWithLambda(10, 3, lambda x1, x2 : x1 + x2))
    ```

- Devolverlas como valor de retorno de otras funciones ("currificación"):

    ```
    def multiplier(n):
        return lambda number : number * n

    duplicater = multiplier(2)
    triplicater = multiplier(3)

    print(duplicater(111))
    print(triplicater(111))

    # Currying version

    print(multiplier(4)(111))
    print(multiplier(5)(111))
    ```

## 3. Operaciones sobre listas, tuplas, diccionarios y conjuntos

### Listas

Es posible iterar listas aplicando funciones en cada iteración mediante las funciones específicas ya definidas map(), filter() y reduce().

En primer lugar está map, que sirve para aplicar una función a todos los elementos de una lista y devolver un nuevo objeto iterable con los elementos resultantes:

```
def startsWithA(string):
    return string[0] == "A"

fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
mapObject = map(startsWithA, fruits)

print(list(mapObject))
```

Después está filter, que sirve para, dada una función que devuelve una expresión de comparación lógica y una lista, aplica la condición determinada por la función a todos los elementos de la lista, y devuelve un nuevo objeto iterable con los elementos filtrados por dicha condición:

```
def endsWithE(string):
    return string[-1] == "e"

fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filterObject = filter(endsWithE, fruits)

print(list(filterObject))
```

Por último tenemos reduce, que dada una función acumuladora y una lista, aplica el resultado de ir recorriendo los elementos de la lista, acumulando el resultado generado por la función, y devuelve el valor resultante de la acumulación:

```
from functools import reduce

def sigma(x, y):
    return x + y

list = [2, 4, 7, 3]
print(reduce(sigma, list))
```

En el caso de reduce, opcionalmente es posible también establecer un valor inicial antes de empezar la acumulación, que también se procesará con el primer elemento de la lista:

```
print(reduce(sigma, list, 10))
```

### Tuplas

[...]

### Diccionarios

[...]

### Conjuntos

[...]

## 4. Creando módulos con nuestras funciones. Importando módulos

Un módulo es un fichero .py que agrupa un conjunto de funciones:

    def add(number1, number2):
      return number1 + number2
    def substract(number1, number2):
      return number2 - number1

Que después se pueden reutilizar:

    import mycalculator
    
    result = mycalculator.add(1,2)

O con un alias:

    import mycalculator as calc
    
    result = calc.add(1,2)

Permite acceso exterior a sus variables:

    # ---- myHeroes.py ----

    myHero1 = {
        "name": "V",
        "age": 42,
        "country": "UK"
    }

    # ---- otherFile.py ----

    import myHeroes

    heroCountry = myHeroes.myHero1["country"]
    print(heroCountry)

O preseleccionarlas en la importación:

    from myHeroes import myHero1

    heroCountry = myHero1["country"]
    print(heroCountry)

## 5. Módulos estándar de Python

El lenguaje aprovisiona una extensa colección de módulos de serie con diversas funcionalidades del mismo tipo para cada módulo:

    import platform

    x = platform.system()
    print(x)

Existen multitud de módulos estándar, algunos de los más usados como ejemplos podrían ser: datetime, math, re, sqlite3, etc.

## 6. Paquetes. Importación

Los módulos se despliegan en forma de paquetes para que puedan compartirse y ser usados según las necesidades de cada proyecto.

Para poder usarlos, es necesario un gestor de paquetes que se encarga de su instalación y desinstalación, en este caso pip:

    pip install camelcase

    pip uninstall camelcase

Y después se usa como un módulo más:

    import camelcase

    c = camelcase.CamelCase()
    txt = "hello world"

    print(c.hump(txt))

## 7. Formateo de la información de salida

[...]

## 8. Lectura y escritura en disco

[...]

## Referencias

[Funciones lambda](https://www.w3schools.com/python/python_lambda.asp)  
[Currificación](https://www.campusmvp.es/recursos/post/Que-es-la-Currificacion-en-programacion-funcional.aspx)  
[map(), filter() y reduce()](https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/)  
[Listas](https://www.w3schools.com/python/python_lists.asp)  
[Tuplas](https://www.w3schools.com/python/python_tuples.asp)  
[Diccionarios](https://www.w3schools.com/python/python_dictionaries.asp)  
[Conjuntos](https://www.w3schools.com/python/python_sets.asp)  
[Módulos](https://www.w3schools.com/python/python_modules.asp)  
[Ejemplos de Módulos Estándar](https://docs.hektorprofe.net/python/modulos-y-paquetes/modulos-estandar/)  
[Gestor de paquetes](https://www.w3schools.com/python/python_pip.asp)  
[Repositorio oficial de paquetes](https://pypi.org/)  
[Documentación de pip](https://pip.pypa.io/en/stable/cli/index.html)  
[Tipos de formateo de salida](https://www.geeksforgeeks.org/python-output-formatting/)  
[Formateo de salida con f-strings (I)](https://realpython.com/python-f-strings/)  
[Formateo de salida con f-strings (II)](https://datagy.io/python-f-strings/)  
[Manejo de ficheros](https://www.w3schools.com/python/python_file_handling.asp)