# Learning Python Level 1 - Sesión 11 Colecciónes

## 11.5.1 - Enumerate - Iterar con índices en Python P1

### Uso de enumerate en Python

La función `enumerate()` **agrega un contador a una secuencia** y devuelve una tupla que contiene el número de índice y el elemento correspondiente en cada iteración del bucle.

Es especialmente útil cuando necesitamos saber tanto el índice como el valor de cada elemento durante la iteración.

### Sintaxis de enumerate()<br>
La sintaxis general de `enumerate()` es:

```python
enumerate(secuencia, inicio=0)
```

>- secuencia: La secuencia u objeto iterable sobre la cual iterar.
>- inicio: Valor inicial del contador. Por defecto, es 0.

`enumerate()` es eficiente y optimizado para manejar grandes volúmenes de datos, ya que no crea una lista adicional en memoria sino que devuelve un iterador.

`enumerate()` es compatible con todo tipo de iterables en Python, incluyendo **listas, tuplas, cadenas**.

---

### Ejemplo básico

En este ejemplo, enumerate se utiliza para recorrer una lista de nombres, imprimiendo el índice y el nombre de cada elemento.

```python

nombres = ['Luis', 'María', 'Carlos', 'Ana']

for indice, nombre in enumerate(nombres):
    print(f"Índice {indice}: {nombre}")

# Salida:
# Índice 0: Luis
# Índice 1: María
# Índice 2: Carlos
# Índice 3: Ana
```

### Ejemplos prácticos

**Especificando un inicio para el contador**<br>
Aquí se muestra cómo usar enumerate especificando un valor de inicio diferente para el contador de índices. En este caso, el conteo comienza en 1 en lugar de 0.

```python
nombres = ['Luis', 'María', 'Carlos', 'Ana']

for indice, nombre in enumerate(nombres, start=1):
    print(f"Estudiante {indice}: {nombre}")

# Salida:
# Estudiante 1: Luis
# Estudiante 2: María
# Estudiante 3: Carlos
# Estudiante 4: Ana
```
---

**Utilizando `enumerate()` con otros tipos de datos**<br>
Este ejemplo muestra cómo enumerate también puede ser utilizado con otros tipos de secuencias, como cadenas de texto, para obtener el índice y el carácter en cada iteración.

```python
cadena = "Python"

for indice, caracter in enumerate(cadena):
    print(f"Índice {indice}: {caracter}")

# Salida:
# Índice 0: P
# Índice 1: y
# Índice 2: t
# Índice 3: h
# Índice 4: o
# Índice 5: n
```
---