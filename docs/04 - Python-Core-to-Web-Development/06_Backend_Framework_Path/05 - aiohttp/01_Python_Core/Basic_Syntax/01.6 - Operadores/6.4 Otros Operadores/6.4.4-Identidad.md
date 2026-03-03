# Operadores de identidad en Python

Los operadores de identidad en Python nos permiten verificar si dos variables se refieren al mismo objeto en la memoria. Estos operadores son útiles para comparar la identidad de objetos (es decir, si dos variables apuntan al mismo lugar en la memoria).

Los operadores is y is not son muy eficientes ya que simplemente comparan las direcciones de memoria de dos objetos (no realizan ninguna operación adicional).

<div align="center">

| Operador | Nombre | Descripción |
|----------|--------|-------------|
| is | Es | Verifica si dos variables apuntan al mismo objeto |
| is not | No es | Verifica si dos variables no apuntan al mismo objeto |

</div>

<br>

## Lista de operadores de identidad
Operador is
El operador is se utiliza para verificar si dos variables se refieren al mismo objeto en la memoria.

```python
a = [1, 2, 3]
b = a

es_igual = (a is b)  # True, ya que a y b se refieren al mismo objeto
```
>En este ejemplo, tanto `x` como `y` apuntan al mismo objeto en la memoria (en Python, los enteros pequeños se almacenan en la misma ubicación), por lo que la expresión `x is not y` es `False`.

<br>

## Operador is not
El operador is not se utiliza para verificar si dos variables NO se refieren al mismo objeto en la memoria.

```python
x = 10
y = 10

no_es_igual = (x is not y)  # False, ya que x e y se refieren al mismo objeto
```
En este ejemplo, tanto `x` como `y` apuntan al mismo objeto en la memoria (en Python, los enteros pequeños se almacenan en la misma ubicación), por lo que la expresión `x is not y` es `False`.

## Ejemplos de uso

### Verificación de identidad de variables

```python
x = 100
y = x

son_iguales = (x is y)  # True, ya que x e y son el mismo objeto en memoria
```

### Verificación de identidad de listas

```python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

son_iguales = (lista1 is lista2)  # False, ya que lista1 y lista2 no son el mismo objeto
son_iguales2 = (lista1 is lista3)  # True, ya que lista1 y lista3 son el mismo objeto
```
### Verificación de identidad de objetos

```python
class MiClase:
    pass

objeto1 = MiClase()
objeto2 = MiClase()
objeto3 = objeto1

son_iguales = (objeto1 is objeto2)  # False, ya que objeto1 y objeto2 no son el mismo objeto
son_iguales2 = (objeto1 is objeto3)  # True, ya que objeto1 y objeto3 son el mismo objeto
```

