# Cómo documentar con Docstrings en Python

En Python, `docstrings` se emplea para generar la documentación de funciones, que es importante para dar instrucciones a otros sobre cómo usar nuestro código.

Las docstrings (abreviatura de “documentation strings”) son cadenas de texto que se colocan al comienzo de una definición de módulo, clase, método o función para describir su propósito y cómo se debe utilizar.

Se definen utilizando triples comillas (`""" o '''`) y se pueden acceder mediante el atributo `__doc__`.

## Sintaxis de los docstrings

La estructura básica de una docstring para funciones incluye:

```python
def mi_funcion():
    """
    Descripción breve de la función.
    
    Args:
        parametro1 (tipo): Descripción del primer parámetro.
        parametro2 (tipo): Descripción del segundo parámetro.
    
    Returns:
        tipo: Descripción del valor de retorno.
    
    Raises:
        Excepcion: Descripción de la excepción que puede ser lanzada.
    """
    # Código de la función
    pass
```
>**Generalmente el docstring contendrá:**
>- Una descripción detallada de los parámetros (si los hay)
>- Una descripción detallada del valor de retorno (si lo hay)
>- Una descripción detallada de las excepciones que pueden ser lanzadas (si las hay)
>- Ejemplos de uso (opcional)

Es principalmente una convención. Pero es importante seguirla para que las herramientas de documentación de Python puedan procesar correctamente los docstrings.

## Ejemplo de docstring

Vamos a verlo con un ejemplo sencillo de como podría ser un docstring para una función que calcula el promedio de una serie de números:

```python
def calcular_promedio(lista):
    '''
    Esta función calcula el promedio de una lista de números.

    Args:
        lista (list): Una lista de números para calcular el promedio.

    Returns:
        float: El promedio de los números en la lista.
    '''
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
```
En este ejemplo, la docstring describe el propósito de la función calcular_promedio, sus argumentos (`lista`) y lo que devuelve (`float`).

## Tipos de Docstrings

En Python, existen varios tipos de docstrings que se utilizan para diferentes propósitos. Algunos de los tipos más comunes son:

>- **Docstrings de funciones**<br>
Describen el propósito de una función, sus argumentos y lo que devuelve (es el que hemos visto en el ejemplo anterior)

>- **Docstrings de clases**<br>
Describen el propósito de una clase, sus atributos y métodos

>- **Docstrings de módulos**<br>
Describen el propósito de un módulo y sus funciones, clases y variables

## Acceso a la documentación

En Python, es posible que una función acceda a su propia documentación, usando la función __doc__

```python
def suma(a, b):
    """
    Devuelve la suma de a y b.
    
    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.
    
    Devuelve:
    int, float: La suma de a y b.
    """
    return a + b

print(suma.__doc__)
```

## Generación automática de documentación

Existen herramientas como Sphinx y Doxygen que pueden generar documentación HTML y otros formatos a partir de docstrings.

Esto facilita crear la creación de documentación para librerías o proyectos.




