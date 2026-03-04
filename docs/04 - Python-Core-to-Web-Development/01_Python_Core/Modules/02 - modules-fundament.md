# Qué son y cómo usar modulos en Python

Los módulos son archivos que contienen código Python, que nos permiten dividir el código en múltiples ficheros de forma que quede más organizado y sea más sencillo reutilizar código.

Un módulo en Python es simplemente un archivo con extensión .py que contiene código Python (dentro de este fichero, podemos incluir definiciones de funciones, variables, clases, etc).

Creando un módulo
Para crear un módulo en Python, simplemente creamos un archivo con extensión .py y escribimos nuestro código en él.

Por ejemplo, podemos crear un módulo llamado operaciones.py con algunas funciones de operaciones matemáticas:

```python
# operaciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
```

## Importando un módulo

Para utilizar las funciones y variables de un módulo en otro archivo de Python, primero necesitamos importarlo.

Podemos importar un módulo completo o importar solo las funciones que necesitamos.

### Importando un módulo completo

Una de las formás de importar un módulo en otro, es importarlo completo (lo que importaría todas las funciones y definiciones que contenga)

```python
import operaciones

resultado_suma = operaciones.suma(5, 3)
print("Resultado de la suma:", resultado_suma)

resultado_resta = operaciones.resta(10, 4)
print("Resultado de la resta:", resultado_resta)
```
- En este ejemplo, importamos el módulo operaciones completo y utilizamos las funciones suma y resta que están definidas en ese módulo.

### Importando funciones específicas de un módulo
También podemos importar funciones específicas de un módulo (lo que puede ser útil si solo necesitamos algunas funciones y no queremos cargar todo el módulo).

```python
from operaciones import multiplicacion, division

resultado_multiplicacion = multiplicacion(6, 2)
print("Resultado de la multiplicación:", resultado_multiplicacion)

resultado_division = division(15, 3)
print("Resultado de la división:", resultado_division)
```
- En este ejemplo, importamos solo las funciones `suma` y `resta` del módulo operaciones y las utilizamos directamente.

## Alias en la Importación

También podemos utilizar alias al importar módulos o funciones. Esto nos permite utilizar un nombre más corto o conveniente en nuestro código.

```python
import operaciones as ops

resultado_suma = ops.suma(5, 3)
print("Resultado de la suma:", resultado_suma)

from operaciones import resta as restar

resultado_resta = restar(10, 4)
print("Resultado de la resta:", resultado_resta)
```

## Módulos Estándar de Python

Además de crear nuestros propios módulos, Python incluye una biblioteca estándar con una amplia variedad de módulos útiles para diversas tareas. Algunos ejemplos son:

<div align="center">

| Módulo | Descripción |
|--------|-------------|
| math | Contiene funciones matemáticas comunes |
| random | Permite generar números aleatorios |
| datetime | Proporciona clases para manejar fechas y horas |
| os | Proporciona funciones para interactuar con el sistema operativo

</div>
<br>
Para utilizar estos módulos, simplemente los importamos de la misma manera que hicimos con nuestro propio módulo operaciones.

## Ejemplo básico

En muchos casos, es común tener un archivo principal que actúe como punto de entrada a nuestro programa. Este archivo puede importar los módulos necesarios y ejecutar el código principal.

Por ejemplo, supongamos que tenemos un archivo main.py que importa y utiliza las funciones del módulo operaciones.

```python
# main.py

import operaciones as ops

resultado_suma = ops.suma(5, 3)
print("Resultado de la suma:", resultado_suma)

resultado_resta = ops.resta(10, 4)
print("Resultado de la resta:", resultado_resta)
```

Al ejecutar main.py, se importarán las funciones del módulo operaciones y se imprimirán los resultados de la suma y resta.

