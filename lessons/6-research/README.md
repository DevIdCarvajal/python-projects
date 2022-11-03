# Proyecto 6: Scientific Research Inc.

## Índice

[1. Manejando arrays y visualizando información científica](#1-manejando-arrays-y-visualizando-información-científica)  
[2. Entornos virtuales](#2-entornos-virtuales)  
[3. Manejando paquetes con pip](#3-manejando-paquetes-con-pip)  
[4. Librerías externas de Python más importantes](#4-librerías-externas-de-python-más-importantes)  
[5. BBDD con Python](#5-bbdd-con-python)  
[6. Uso de SQL: Librería sqlite3](#6-uso-de-sql-librería-sqlite3)

## 1. Manejando arrays y visualizando información científica

- Crear un entorno virtual en el que se instalen la súltimas versiones de los paquetes `numpy`, `pandas`, `matplotlib` y `scipy`.
- Definir un dataset en CSV del tiempo atmosférico (temperatura, velocidad del viento, precipitaciones, etc.) para distintas ciudades, por días, durante una semana.
- Implementar funciones que obtengan valores promedio, moda, etc. de algunas de las variables registradas.
- Representar con gráficas de dos o más tipos los datos del CSV.

Nota: Se debe usar la mayor cantidad de librerías instaladas posible para resolver el ejercicio.

## 2. Entornos virtuales

Se pueden crear fácilmente instancias secundarias del intérprete de Python de manera que estas tengan su propio contexto, independientemente de la instancia principal.

Estas instancias son conocidas como entornos virtuales, y actúan como contenedores aislados y encapsulados, permitiendo generar así entornos seguros de pruebas, sin "ensuciar" el entorno principal.

Para gestionar y trabajar con entornos virtuales, se puede utilizar el paquete `virtualenv`, que se instala con `pip`:

    pip install virtualenv

  - Crear entorno:
  
        virtualenv my-env

  - Activar entorno:
  
        source my-env/bin/activate

  - Desactivar entorno:
  
        deactivate

Para el caso de Visual Studio Code, se debe seleccionar el entorno virtual en el que se va a trabajar, pulsando `Ctrl+Shift+P` y después seleccionando `Python: Select Interpreter`.

## 3. Manejando paquetes con pip

El gestor de paquetes de Python, conocido como `pip`, es dependiente del entorno, de manera que los paquetes instalados en un entorno no afectan al de otro.

Esto, entre otras ventajas, tiene por ejemplo la de que permite desarrollar aplicaciones que trabajen con distintas versiones de intérpretes o de módulos.

Una vez creado y activado un entorno, podemos instalar paquetes:

    pip install numpy
    pip install matplotlib
    pip install pandas
    pip install scipy

Listar paquetes instalados:

    pip list numpy

Desinstalar paquetes:

    pip uninstall numpy

Buscar paquetes:

    pip search requests

Crear un fichero con la lista de paquetes instalados y sus versiones actuales:

    pip freeze > requirements.txt

Que se puede reutilizar para instalar rápidamente esos mismos paquetes en otro entorno:

    pip install -r requirements.txt

## 4. Librerías externas de Python más importantes

- ### NumPy

- ### Pandas

- ### Mathplotlib

- ### SciPy

## 5. BBDD con Python

[...]

## 6. Uso de SQL: Librería sqlite3

[...]

## Referencias

[Entornos virtuales con Python (I)](https://openwebinars.net/blog/entornos-de-desarrollo-virtuales-con-python3/)  
[Entornos virtuales con Python (II)](https://code.tutsplus.com/es/tutorials/understanding-virtual-environments-in-python--cms-28272)  
[Tutorial de NumPy](https://www.w3schools.com/python/numpy/default.asp)  
[Tutorial de Pandas](https://www.w3schools.com/python/pandas/default.asp)  
[Tutorial de Matplotlib](https://www.w3schools.com/python/matplotlib_intro.asp)  
[Tutorial de SciPy](https://www.w3schools.com/python/scipy/index.php)  
[Introducción a SQLite con Python](https://parzibyte.me/blog/2017/11/21/python-3-sqlite-3-introduccion-ejemplos/)  
[Manual de SQLite](https://www.geeksforgeeks.org/python-sqlite/)