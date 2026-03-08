# Bootcamp Python SESIÓN 3 -  VARIABLES & CONSTANTES

## 4. ASIGNACIÓN DE MULTIPLES VARIABLES

En Python, es posible asignar `múltiples variables` en una sola línea de código. Esto se puede hacer utilizando comas para separar las variables y los valores correspondientes. Aquí hay un ejemplo:

```python
# Asignación múltiple
a, b, c = 1, 2, 3
print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3
```

En este ejemplo, las variables `a`, `b` y `c` se asignan a los valores `1`, `2` y `3`, respectivamente.
También es posible asignar el mismo valor a múltiples variables al mismo tiempo:

```python
# Asignación del mismo valor a múltiples variables
x = y = z = 0
print(x)  # Salida: 0
print(y)  # Salida: 0
print(z)  # Salida: 0
```

En este caso, las variables `x`, `y` y `z` se asignan al valor `0`.

## 2. ASIGNACIÓN DE MULTIPLES VALORES NO VALIDOS

Es importante tener en cuenta que la asignación múltiple requiere que el número de variables coincida con el número de valores. Si no coinciden, Python generará un error. Aquí hay un ejemplo de una asignación inválida:

```python
# Asignación inválida
a, b = 1, 2, 3  # Esto generará un error
```

En este caso, hay dos variables (`a` y `b`) pero tres valores (`1`, `2` y `3`), lo que resulta en un error de "ValueError: too many values to unpack".

## 3. ASIGNACIÓN DE MULTIPLES VARIABLES CON LISTAS O TUPLAS

También es posible asignar múltiples variables utilizando listas o tuplas.

Aquí hay un ejemplo con una lista:

```python
# Asignación múltiple con lista
valores = [4, 5, 6]
a, b, c = valores
print(a)  # Salida: 4
print(b)  # Salida: 5
print(c)  # Salida: 6
```

Y aquí hay un ejemplo con una tupla:

```python
# Asignación múltiple con tupla
valores = (7, 8, 9)
a, b, c = valores
print(a)  # Salida: 7
print(b)  # Salida: 8
print(c)  # Salida: 9
```

En ambos casos, las variables `a`, `b` y `c` se asignan a los valores correspondientes de la lista o tupla.
