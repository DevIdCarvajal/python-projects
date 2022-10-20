# Proyecto 4: Filtro anti-spam

## Índice

[1. Básicos en antispam](#1-básicos-en-antispam)  
[2. Clases. Programación orientada a objetos en Python](#2-clases-programación-orientada-a-objetos-en-python)  
[3. Ámbitos y namespaces](#3-ámbitos-y-namespaces)  
[4. Objetos Clase, Instancia y Método. Constructores](#4-objetos-clase-instancia-y-método-constructores)  
[5. Herencia y herencia múltiple](#5-herencia-y-herencia-múltiple)  
[6. Generadores e iteradores](#6-generadores-e-iteradores)  
[7. Expresiones regulares: Librería re](#7-expresiones-regulares-librería-re)  
[8. Más sobre urllib](#8-más-sobre-urllib)  
[9. Otras librerías estándar](#9-otras-librerías-estándar)

## 1. Básicos en antispam

- Definir un listado de términos de búsqueda que estén catalogados como spam (e.g., "cialis", "viagra")
- A partir de un fichero de texto que contiene algunos de los términos de búsqueda, un programa que devuelva cuántos hay, cuáles son y cuántas veces se repiten en el texto.
- Repetir el mismo ejercicio con patrones más complejos (e.g., emails o urls que acaben en ".thisisspam.com" o "@spammail.com")

## 2. Clases. Programación orientada a objetos en Python

### Fundamentos de la POO

- Abstracción
- Encapsulamiento
- Modularidad
- Herencia
- Polimorfismo

### Ejemplo de clase

    class Clicker:
      counter = 0

      def click(self):
        self.counter += 1

## 3. Ámbitos y namespaces

Los espacios de nombres son los identificadores de los objetos (variables o métodos/funciones) que sirven para delimitar el ámbito en el que otros objetos pueden ser accedidos.

Existen tres tipos, de mayor a menor:

- Built-in: En él están declarados todos los objetos, funciones, variables, etc., predefinidos en el lenguaje, que el intérprete entiende (según la versión) y pueden ser llamados en cualquier parte.
- Global: El ámbito general del código escrito en el programa, donde se declaran aquellas variables y funciones que serán llamadas en distintas partes del mismo.
- Local: El ámbito restringido al interior de una función, método o clase determinados, de manera que sus objetos contenidos solo son accesibles dentro de dicho ámbito.

Un ejemplo de ámbito podría ser el siguiente:

    # Global
    abuelo = 1
    
    def abuela():

      # Local
      padre = 2

      def madre():

        # Local (anidado)
        nieto = 3

Es posible acceder dentro de un ámbito local a objetos definidos globalmente (si bien no es buena práctica), para evitar ambigüedad:

    count = 5

    def incrementer():
      global count
      count = count + 1
      print(count)
    
    incrementer()

## 4. Objetos Clase, Instancia y Método. Constructores

Esto es una clase (con sus propiedades y métodos), de la que se pueden instanciar objetos:

    class Horse:
      alive = True

      def __init__(self, name = '', speed = 10):
        self.name = name
        self.speed = speed

      def run(self):
        if self.alive:
          self.speed += 5

          if self.speed > 50:
            self.alive = False
        else:
          print('No puedo más')

      def brake(self):
        self.speed -= 5

      def say(self, something):
        print(something)

    caballoNormal = Horse()
    caballoNormal.speed = 25

    print(f"{caballoNormal.name}, {caballoNormal.speed}")

    yeguaRapida = Horse(speed = 20)

    print(f"{yeguaRapida.name}, {yeguaRapida.speed}")

    laDelCid = Horse("Babieca", 15)
    
    laDelCid.run()
    laDelCid.say("Ou yeah")

    print(f"{laDelCid.name}, {laDelCid.speed}")

Además del constructor, en Python existen otros métodos especiales para sobrecargar otros "métodos mágicos" u operadores por defecto:

    class MagnifiedList:
      def __init__(self, normalList):
        self.data = normalList
      def __len__(self):
        return len(self.data) + 2

    myList = MagnifiedList([1, 2, 3])
    print(len(myList))

## 5. Herencia y herencia múltiple

Una clase puede heredar de otra, redefiniendo o añadiendo propiedades y/o métodos:

    class Meara(Horse):
      def __init__(self, name = '', speed = 30):
        super().__init__(name, speed)
        self.country = 'Rohan'
      def beMagic(self):
        print('Soy increíble')

    elDeGandalf = Meara(name = "Sombragrís")

    print(f"{elDeGandalf.name}, {elDeGandalf.speed}, {elDeGandalf.country}")

Incluso puede heredar de más de una clase, de manera que tendrá los miembros de todas sus superclases:

    class Flying():
      altitude = 0

      def flyUp(self):
        self.altitude += 10

      def flyDown(self):
        self.altitude += 10

    class Pegasus(Horse, Flying):
      secretName = "Saint Seiya"

      def special(self):
        print('Soy la leche')

    caballeroDelZodiaco = Pegasus(name = "Pegasus", speed = 50)
    
    caballeroDelZodiaco.run()
    caballeroDelZodiaco.flyUp()
    caballeroDelZodiaco.special()
    
    print(f"{caballeroDelZodiaco.name}, {caballeroDelZodiaco.secretName}, {caballeroDelZodiaco.speed}, {caballeroDelZodiaco.altitude}")

## 6. Generadores e iteradores

### Generadores

Son funciones capaces de generar un sinfín de resultados obtenidos "poco a poco", es decir, en pasos sucesivos y en tiempo de ejecución, lo que implica un menor coste de recursos:

    def getEven():
      index = 1
      
      # ¡Atención, bucle infinito!
      while True:
          
        # Devolvemos un valor
        yield index * 2
        index = index + 1

    for i in getEven():
        print(i)

### Iteradores

Son objetos que contienen un número finito de valores, que por tanto se pueden recorrer (iterar) de uno en uno para acceder a los mismos.

Strings, listas, tuplas, diccionarios y conjuntos son contenedores iterables de los que se puede extraer un iterador, a partir de los métodos `iter` y `next`, o recorrer mediante un `for .. in`:

    myFruits = ("apple", "banana", "cherry")
    myIterator = iter(myFruits)

    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))

    for f in myFruits:
      print(f)

    myFruit = "strawberry"
    myIterator = iter(myFruit)

    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))

    for f in myFruit:
      print(f)

Es posible crear iteradores propios mediante clases que implementen los métodos `__iter__()` y `__next__()`:

    class OddNumbersMax10:
      def __iter__(self):
        self.counter = 1
        return self
      
      def __next__(self):
        if self.counter < 21: # Límite máximo
          x = self.counter
          self.counter += 2
          return x
        else:
          raise StopIteration # Excepción de parada

    myOddNumbers = OddNumbers()
    myIterator = iter(myOddNumbers)

    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))

## 7. Expresiones regulares: Librería re

Son una notación o sintaxis para definir patrones en strings, de cara a compararlos con el patrón, de manera que pueda saberse si lo cumplen o no.

Algunos ejemplos de usos típicos de regexp son la validación de correos, contraseñas o códigos personalizados con un formato específico predeterminado (NIF, SKU, etc.).

[...]

## 8. Más sobre urllib

[...]

## 9. Otras librerías estándar

[...]

## Referencias

[Programación orientada a objetos](https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos)  
[Clases](https://www.w3schools.com/python/python_classes.asp)  
[Métodos especiales](https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html)  
[Ámbito](https://www.w3schools.com/python/python_scope.asp)  
[Espacios de nombres (I)](https://www.geeksforgeeks.org/namespaces-and-scope-in-python/)  
[Espacios de nombres (II)](https://realpython.com/python-namespaces-scope/)  
[Herencia](https://www.w3schools.com/python/python_inheritance.asp)  
[Herencia múltiple](https://pythones.net/herencia-simple-y-multiple-python-oop/)  
[Generadores](https://python-intermedio.readthedocs.io/es/latest/generators.html)  
[Iteradores](https://www.w3schools.com/python/python_iterators.asp)  
[Aprender regex (I)](https://learn-regex.com/)  
[Aprender regex (II)](https://regexone.com/)  
[Referencia regex](https://regexr.com/)  
[El módulo re](https://www.w3schools.com/python/python_regex.asp)  
[]()  
[]()