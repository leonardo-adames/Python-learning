<div align="center">
    <kbd><h1><b>CURSO DE PYTHON</b><br>SINTAXIS BÁSICA</b></h1></kbd>
        <img width="2064" height="100%" alt="Image" src="../../../../notes/resources/INTRO/Py_welcome8.3.png" altº="Image" width="100%"/>
    <br>
    <br>
    <h2><kbd>LOS DOCSTRINGS</kbd></h2>
</div>

<br>

En Python, `docstrings` se emplea para generar la documentación de funciones, que es importante para dar instrucciones a otros sobre cómo usar nuestro código.

Las docstrings (abreviatura de “documentation strings”) son cadenas de texto que se colocan al comienzo de una definición de módulo, clase, método o función para describir su propósito y cómo se debe utilizar.

Se definen utilizando triples comillas (`""" o '''`) y se pueden acceder mediante el atributo `__doc__`.

<br>

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

<br>

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

<br>

## Tipos de Docstrings

En Python, existen varios tipos de docstrings que se utilizan para diferentes propósitos. Algunos de los tipos más comunes son:

<br>

>- **Docstrings de funciones**<br>
Describen el propósito de una función, sus argumentos y lo que devuelve (es el que hemos visto en el ejemplo anterior)

**EJEMPPLO**

<br>

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

suma(a, b)
```
<br>

>- **Docstrings de métodos**<br>
Describen el propósito de un método, sus argumentos y lo que devuelve (es el que hemos visto en el ejemplo anterior)

<br>


>- **Docstrings de clases**<br>
Describen el propósito de una clase, sus atributos y métodos

**EJEMPPLO**

<br>

```python
class Persona:
    """
    Representa a una persona con un nombre y una edad.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """
        Saluda a la persona.

        Returns:
            str: Un saludo que incluye el nombre de la persona.
        """
        return f"Hola, mi nombre es {self.nombre}"

    def obtener_edad(self):
        """Devuelve la edad de la persona."""
        return self.edad

```
<br>

>- **Docstrings de módulos**<br>
Describen el propósito de un módulo y sus funciones, clases y variables

**EJEMPPLO**

<br>

```python
"""
Este módulo proporciona funciones para realizar operaciones matemáticas básicas.

Funciones:
    suma(a, b): Devuelve la suma de dos números.
    resta(a, b): Devuelve la resta de dos números.
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

```
<br>

## Acceso a la documentación

En Python, es posible que una función acceda a su propia documentación, usando la función `__doc__`

**EJEMPPLO**

<br>

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
<br>

## Generación automática de documentación

Existen herramientas como Sphinx y Doxygen que pueden generar documentación HTML y otros formatos a partir de docstrings.

Esto facilita crear la creación de documentación para librerías o proyectos.

<br>
<br>

---

## POR QUÉ ES IMPORTANTE Y NECESARIA DE LOS DOCKSTRINGS Y POR QUÉ SABERLO AHORA?

Imagina esto, Un **capitan** y su **tripulación** navegando sin unabrujula que los guíe o una bitáocra con la cual guiar a otros capitanes y trupulación, En palabras simples, los **`Docstring`** en python serían esa `BRUJULA` y esa `BITÁCORA`, sin implementación de `DOCSTRING` en el código de un proyecto totalmente real dentro de la industriatodo los colaboradores del proyecto caminarían a siegas y ahí es donde surge lo que se conoce como la `deuda tecnica`, con un código que solo entiendes tú o solo funciona en tu máquina esto al pasar del tiempo produce u nefecto dominó donde todo se derrumba.

Inclusive, la implementación de `docstring` en tu código está estrictamente señalizado en el manual de buenas prácticas de `Python` así que no lo pases por alto por que parezca sencilli e inutil a simple vista, porque no es así.