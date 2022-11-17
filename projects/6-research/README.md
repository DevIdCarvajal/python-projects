# Proyecto 6: Scientific Research Inc.

## Índice

[1. Manejando arrays y visualizando información científica](#1-manejando-arrays-y-visualizando-información-científica)  
[2. Entornos virtuales](#2-entornos-virtuales)  
[3. Manejando paquetes con pip](#3-manejando-paquetes-con-pip)  
[4. Librerías externas de Python más importantes](#4-librerías-externas-de-python-más-importantes)  
[5. BBDD con Python](#5-bbdd-con-python)  
[6. Uso de SQL: Librería sqlite3](#6-uso-de-sql-librería-sqlite3)

## 1. Manejando arrays y visualizando información científica

- Crear un entorno virtual en el que se instalen las últimas versiones de los paquetes `numpy`, `pandas`, `matplotlib` y `scipy`.
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

Para trabajar con bases de datos, Python dispone de varios paquetes de terceros a instalar, que incluyen los llamados conectores, y que dependen del sistema gestor de base de datos (SGBD) con el que se quiera trabajar: MySQL, PosgreSQL, SQL Server, Oracle, etc., en el caso de relacionales, y MongoDB, etc., en el caso de NoSQL.

Sea cual sea el que se elija, implica también instalar en la máquina el SGBD en cuestión y tener un servidor activo y escuchando, configurado y listo para aceptar peticiones de la aplicación que estamos desarrollando, salvo que ya se disponga previamente de un servidor de base de datos levantado (sea un servicio en la nube de terceros o un servidor propio).

Además, desde la versión 2.5, Python incluye un gestor de SQLite integrado, que para pruebas en desarrollo puede resultar bastante útil sin necesidad de instalar un SGBD.

## 6. Uso de SQL: Librería sqlite3

Ejemplo básico completo de creación de base de datos con creación de una tabla, población de datos y obtención de datos:

    import sqlite3

    database = sqlite3.connect("example.db")
    cursor = database.cursor()

    def createTable():
      global cursor

      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS books(
            id INT PRIMARY KEY,
            title VARCHAR(50) NOT NULL,
            author VARCHAR(50) NOT NULL,
            genre VARCHAR(20) NULL,
            cost REAL NOT NULL
          );
        """
      )

    def populateData():
      global database
      global cursor

      cursor.execute(
        """
          INSERT INTO books
          VALUES
            (1, 'Los pilares de la tierra', 'Ken Follet', 'Suspense', 45),
            (2, 'Entrevista con el vampiro', 'Anne Rice', 'Fantasía', 25);
        """
      )

      database.commit()

    def selectData():
      global cursor

      cursor.execute(
        """
          SELECT *
            FROM books;
        """
      )

      return cursor.fetchall()

    # -------------------

    createTable()
    populateData()

    books = selectData()

    print(books)

## Referencias

[Entornos virtuales con Python (I)](https://openwebinars.net/blog/entornos-de-desarrollo-virtuales-con-python3/)  
[Entornos virtuales con Python (II)](https://code.tutsplus.com/es/tutorials/understanding-virtual-environments-in-python--cms-28272)  
[Tutorial de NumPy](https://www.w3schools.com/python/numpy/default.asp)  
[Tutorial de Pandas](https://www.w3schools.com/python/pandas/default.asp)  
[Tutorial de Matplotlib](https://www.w3schools.com/python/matplotlib_intro.asp)  
[Tutorial de SciPy](https://www.w3schools.com/python/scipy/index.php)  
[Aprende Python con Alf](https://aprendeconalf.es/docencia/python/manual/)  
[Introducción a SQLite con Python](https://parzibyte.me/blog/2017/11/21/python-3-sqlite-3-introduccion-ejemplos/)  
[Manual de SQLite](https://www.geeksforgeeks.org/python-sqlite/)  
[Tutorial MySQL Python](https://www.w3schools.com/python/python_mysql_getstarted.asp)