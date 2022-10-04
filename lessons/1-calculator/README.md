# Proyecto 1: Calculadora financiera

## Índice

[0. Prerrequisitos](#0-prerrequisitos)  
[1. Operaciones a implementar](#1-operaciones-a-implementar)  
[2. Estructura de un programa Python](#2-estructura-de-un-programa-python)  
[3. Comentarios y documentación de programas](#3-comentarios-y-documentación-de-programas)  
[4. Entrada y salida de información en consola (input y print)](#4-entrada-y-salida-de-información-en-consola-input-y-print)  
[5. Variables y tipos de datos en Python: Números, textos, listas, tuplas y diccionarios](#5-variables-y-tipos-de-datos-en-python-números-textos-listas-tuplas-y-diccionarios)  
[6. Asignaciones](#6-asignaciones)  
[7. Operadores: Aritméticos, lógicos, relacionales, a nivel de bit](#7-operadores-aritméticos-lógicos-relacionales-a-nivel-de-bit)  
[8. Condicionales. Indentación y PEP8](#8-condicionales-indentación-y-pep8)  
[9. Bucles for y while](#9-bucles-for-y-while)  
[10. Sentencias de control: continue, break y pass](#10-sentencias-de-control-continue-break-y-pass)  
[11. Funciones. Argumentos](#11-funciones-argumentos)  
[12. Uso de la librería estándar math](#12-uso-de-la-librería-estándar-math)

## 0. Prerrequisitos

- Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Extensión de Python para VS Code: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Git: [https://git-scm.com/download/](https://git-scm.com/download/)

## 1. Operaciones a implementar

- Calculadora común: Suma, resta, multiplicación, división y resto
- Calculadora de cambio de divisa: € <-> $, $ <-> BTC, BTC <-> €
- Calculadora/generación de facturas: IVA (0/4/10/21) e IRPF (0/15)

## 2. Estructura de un programa Python

1. Crear un fichero hello.py
2. Añadir estas dos líneas:

    ```
    msg = "Hello World"
    print(msg)
    ```

3. Ejecutar fichero en la terminal:

- Windows:

    ```
    python hello.py
    ```

- Mac/Linux:

    ```
    python3 hello.py
    ```

4. Depurar el fichero (en VS Code):

   - Punto de parada (F9)
   - Modo de depuración (F5)
   - Consola de depuración

## 3. Comentarios y documentación de programas

Se puede comentar código de una sola línea:

    ```
    # Esto es un comentario simple
    ```

O de varias líneas:

    ```
    """
    Esto es un comentario
    un poco más complejo
    """
    ```

De este modo se puede documentar el código mediante Docstrings:

    ```
    def square(a):
        '''Returned argument a is squared.'''
        return a**a

    print(square.__doc__)

    help(square)
    ```

## 4. Entrada y salida de información en consola (input y print)

Podemos mostrar su valor:

```
print('Espagueti')
```

Y su tipo:

```
print(type('Espagueti'))
```

Podemos capturar un valor y asignárselo:

```
name = input("Escribe tu nombre: ")
print(name)
```

## 5. Variables y tipos de datos en Python: Números, textos, listas, tuplas y diccionarios

Python presenta todos estos tipos:

```
String - str
Integer - int
Float - float
Complex - complex
Boolean - bool
List - list
Tuple - tuple
Set - set
Dictionary - dict
None
```

Podemos convertir el tipo de un valor (casting):

```
age = int(input("Escribe tu edad: "))
print(age)
```

Si es un string, concatenar varios:

```
# - Con el operador:
print("Hola, " + name + " " + lastname + ", tienes " + age + " años")

# - Con la notación f-string:
print(f"Adiós, {name} {lastname}, tienes {age} años")
```

### Listas

Esto son ejemplos de listas:

```
colors = ["red", "blue", "green"]
stuff = ["thing", 3, True]
```

Se accede por su índice numérico (empieza en cero, acaba en menos uno):

```
print(colors[0])
print(colors[-1])
```

Se pueden añadir y eliminar elementos:

```
colors.remove("blue")
colors.append("orange")
print(colors)
```

Se pueden recorrer:

```
for color in colors:
    print(color)
```

### Tuplas

Esto es un ejemplo de tupla:

```
position = (2, 3, -1)
```

Las tuplas no se pueden modificar parcialmente, pero sí totalmente:

```
position.remove(2) # Error
```

### Diccionarios

Esto son ejemplos de diccionarios:

```
dictionary = {1:"X", "X":2}
godness = {"name": 'Unicornio', "lastname": 'Rosa Invisible', 'age': 31}
```

Se accede por su clave:

```
print(dictionary[1])
print(godness["name"])
```

Se pueden añadir y eliminar elementos:

```
godness["place"] = "rainbow"
print(godness)

godness.pop("place")
print(godness)

# Otra opción para borrar:
# del godness["place"]
```

Se pueden recorrer:

```
# Claves:

for key in godness:
    print(key)

# Otra forma:

for key in thisdict.keys():
    print(key)

# Valores:

for value in godness:
    print(godness[value])

# Otra forma:

for value in godness.values():
    print(value)

# Claves y valores:

for key, value in godness.items():
    print(key, value)
```

## 6. Asignaciones

Estas son asignaciones de variables:

```
name = 'Espagueti'
lastname = "Volador"
age = 16
```

Y estas realizan además una operación:

```
age += 2
age %= 10
```

## 7. Operadores: Aritméticos, lógicos, relacionales, a nivel de bit

Para las operaciones matemáticas se usan operadores aritméticos:

```
+ - * / % ** //
```

Para las estructuras de control de flujo se usan operadores de comparación (o relacionales) y operadores lógicos:

```
== != < <= > >=
and or not
```

Para operaciones y comparaciones con números binarios se usan operadores a nivel de bit:

```
& | ^ ~ << >>
```

## 8. Condicionales. Indentación y PEP8

```
a = 1
b = 2
if b > a:
    print("b es mayor que a")
```

Puede haber condicionales de dos o más ramas:

```
a = 1
b = 2
c = 3
if a > b:
    print("a es mayor que b")
else:
    print("b es mayor que a")

if a > c:
    print("a es mayor que c")
elif a > b:
    print("a es mayor que b")
else:
    print("a es el más pequeño de todos")
```

Existen algunas reglas de estilo definidas en el PEP8, como por ejemplo:

- La indentación determina subordinación/anidación: 4 espacios (tabuladores no)
- Longitud de líneas (79, 72, 99) y líneas en blanco
- Posición de operadores y parámetros de funciones
- Comentarios y convenciones de nomenclatura

    etc.

## 9. Bucles for y while

Un bucle debe tener tres elementos:

- Inicialización previa
- Condición de parada
- Cambios en cada iteración

```
## While

i = 0

while i < 5:
    print(i)
    i += 1

## For .. in

for i in range(5):
    print(i)

for letter in "abracadabra":
    print(letter)
```

## 10. Sentencias de control: continue, break y pass

Es posible romper (break) un bucle y salir de él en una iteración concreta:

```
for letter in "abracadabra":
    if letter == 'c':
        break
    print(letter)
```

O también saltar (continue) a la siguiente iteración en un punto dado de la iteración actual:

```
for letter in "abracadabra":
    if letter == 'c':
        continue
    print(letter)
```

O no hacer nada (pass), al menos por el momento:

```
for letter in "abracadabra":
    if letter == 'c':
        pass
    print(letter)
```

## 11. Funciones. Argumentos

Una función se define de la siguiente manera:

```
def learn():
    print("¡Estoy aprendiendo Python!")
```

Y se la llama (invoca) así:

```
learn()
```

Puede recibir argumentos:

```
def learn(subject):
    print(f"¡Estoy aprendiendo {subject}!")
```

Puede devolver valores:

```
def learnMore(subject, level):
    print (f"¡Estoy aprendiendo {subject}!")

    return level + 1

level = 0
level = learnMore(subject, level)
```

¡Cuidado con el ámbito (local vs global)!

## 12. Uso de la librería estándar math

Hay algunas funciones matemáticas que vienen de serie:  

```
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)
```

Y otras importando la librería (o módulo) math:

```
import math

x = math.sqrt(64)

print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)

x = math.pi

print(x)
```

## Referencias

[Documentación oficial de VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)

[Variables](https://www.w3schools.com/python/python_variables.asp)  
[Tipos de datos](https://www.w3schools.com/python/python_variables.asp)  
[Operadores](https://www.w3schools.com/python/python_operators.asp)  
[Listas](https://www.w3schools.com/python/python_lists.asp)  
[Tuplas](https://www.w3schools.com/python/python_tuples.asp)  
[Diccionarios](https://www.w3schools.com/python/python_dictionaries.asp)  
[Condicionales](https://www.w3schools.com/python/python_conditions.asp)  
[Bucles While](https://www.w3schools.com/python/python_while_loops.asp)  
[Bucles For](https://www.w3schools.com/python/python_for_loops.asp)  
[Funciones](https://www.w3schools.com/python/python_functions.asp)  
[Ámbito](https://www.w3schools.com/python/python_scope.asp)

[Python Tutor](https://pythontutor.com/)
