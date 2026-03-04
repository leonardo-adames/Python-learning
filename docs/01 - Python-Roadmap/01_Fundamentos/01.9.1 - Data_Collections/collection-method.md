# Learning Python Level 1 - Sesión 11 Colecciónes

## 11.5.3 - Métodos de Colecciones

### Cómo usar comprensiones en Python Introducción

`Python` ofrece una serie de funciones y métodos integrados que facilitan la manipulación y el procesamiento de listas, tuplas y otros iterables

<div align="center">

| Método | Descripción |
|--------|-------------|
| `map()` | Aplica una función a cada elemento de un iterable |
| `filter()` | Filtra elementos de un iterable basándose en una condición |
| `any()` | Retorna True si al menos un elemento del iterable es verdadero |
| `all()` | Retorna True si todos los elementos del iterable son verdaderos |
| `sorted()` | Retorna una nueva lista ordenada a partir de los elementos de un iterable |
| `sum()` | Calcula la suma de los elementos de un iterable |
| `enumerate()` | Agrega un índice a cada elemento de un iterable |
| `reduce()` | Reduce una secuencia de elementos a un valor aplicando una función acumulativa |
| `zip()` | Combina elementos de múltiples iterables en tuplas |

</div>

---
<br>

## Funciones sobre iterables

**Función `map()`**

**La función `map()`** en Python se utiliza para aplicar una función a cada elemento de una secuencia** y devolver un iterable con los resultados.

```python
# Uso básico de map():
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)

print(list(cuadrados)) # [1, 4, 9, 16, 25]
```
>En este ejemplo,<br>
>- map(cuadrado, numeros) aplica la función cuadrado() a cada elemento de la lista numeros,
>- Devuelve un objeto map que contiene los cuadrados de los números.

En muchas ocasiones, emplearemos la función `map()` con una función lambda, para hacer el código más conciso:

```python

# Uso de map() con función lambda:

numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)

print(list(cuadrados)) # [1, 4, 9, 16, 25]
print(list(cuadrados)) # [1, 4, 9, 16, 25]
```

---
**Función `filter()`**

La función filter() en Python se utiliza para filtrar elementos de una secuencia basándose en una condición definida por una función.

```python
# Uso básico de filter():
def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(es_par, numeros)
```

>En este ejemplo,
>- filter(es_par, numeros) filtra los números de la lista numeros
>- Devuelve un objeto filter que contiene solo los números pares

Al igual que con map(), también se puede utilizar una función lambda con filter():

```python
# Uso básico de filter():
def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(es_par, numeros)

print(list(pares))  # Output: [2, 4, 6, 8, 10]
```
---

**Funciones `any()` y `all()`**

Las funciones `any()` y `all()` en Python son funciones booleanas que retornan True en función de los valores de un iterable

    any() si al menos un elemento es True
    all() si todos los elementos son True
`(any())` o todos los elementos `(all())` de un iterable son verdaderos, respectivamente.

```python
# Uso de any() y all():
valores = [True, False, True, False, True]
hay_algun_verdadero = any(valores)  # True
todos_verdaderos = all(valores)     # False
```

Estas funciones son útiles para verificar condiciones en iterables (como listas o generadores).

En muchas ocasiones se emplean junto con map para aplicar una función a los valores de un iterable. Por ejemplo asi,

```python
valores = [1, 2, 3, 4, 5]
algun_mayor_que_diez = any(map(lambda x: x > 10, valores))  # False
```
--

**Función `sorted()`**<br>

La función sorted() en Python retorna una nueva lista ordenada a partir de los elementos del iterable especificado.

```
# Uso básico de sorted():
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numeros_ordenados = sorted(numeros)

print(numeros_ordenados) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
```

>En este ejemplo, `sorted(numeros)` ordenará la lista `numeros` de forma ascendente y asignará el resultado a `numeros_ordenados`.

Opcionalmente, podemos especificar,

Una función `key` para personalizar el ordenamiento
Un argumento `reverse` para invertir el orden

```python
# Uso de sorted() con key y reverse:
palabras = ["python", "java", "c++", "ruby", "javascript"]
palabras_ordenadas = sorted(palabras, key=len, reverse=True)

print(palabras_ordenadas) # ['javascript', 'python', 'java', 'c++', 'ruby']
```

Aquí, sorted(palabras, key=len, reverse=True) ordena la lista palabras por la longitud de las cadenas de forma descendente.

**Función `sum()`**

La función `sum()` en Python retorna la suma de los elementos del iterable especificado, opcionalmente comenzando desde un valor inicial especificado (por defecto, 0).

```python
# Uso básico de sum():
numeros = [1, 2, 3, 4, 5]

suma_total = sum(numeros)  # 15
```

Este ejemplo suma todos los números en la lista numeros.

**Función `enumerate()`**

La función `enumerate()` en Python retorna un objeto enumerado que produce tuplas con un contador y un elemento del iterable especificado, opcionalmente comenzando desde un índice especificado (por defecto, 0).

```python
# Uso básico de enumerate():
equipos = ["Real Madrid", "Barcelona", "Atlético de Madrid"]
enumeracion_equipos = list(enumerate(equipos, start=1))

print(enumeracion_equipos) # [(1, 'Real Madrid'), (2, 'Barcelona'), (3, 'Atlético de Madrid')]
```

>En este ejemplo,<br>
>- enumerate(equipos, start=1) enumera los equipos de fútbol comenzando desde 1
>- Genera una lista de tuplas (índice, equipo).

**Función `reduce()`**

La función `reduce()` en Python se utiliza para reducir una secuencia de elementos a un solo valor aplicando repetidamente una función de dos argumentos a los elementos de la secuencia.

```python
# Uso básico de reduce():
from functools import reduce

def suma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]
suma_total = reduce(suma, numeros)

print(suma_total) # Salida: 15
```

>En este ejemplo,
>- `reduce(suma, numeros)` aplica la función suma() de manera acumulativa a los elementos de la lista numeros
>- Resulta en la suma total de todos los números.

Desde Python 3 la función `reduce()` se movió al módulo functools, por lo que es necesario importarla desde allí

**Función `zip()`**

La función `zip()` en Python combina elementos de varios iterables en tuplas hasta que se agoten los elementos del iterable más corto.

```python
# Uso básico de zip():
nombres = ["Luis", "María", "Pedro"]
edades = [30, 25, 35, 40]

print(personas) # [("Luis", 30), ("María", 25), ("Pedro", 35)]
```

>En este ejemplo, `zip(nombres, edades)` combina las listas nombres y edades en una lista de tuplas (`nombre, edad`).
>- En este caso, devuelve una colección de 3 tuplas, porque nombres sólo tiene 3 valores. Cada tupla combina un valor del iterable nombres y del iterable edades.

