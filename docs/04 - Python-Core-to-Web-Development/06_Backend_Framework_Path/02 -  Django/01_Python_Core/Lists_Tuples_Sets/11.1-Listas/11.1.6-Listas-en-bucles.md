# BootCamp Python Sesión 11- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.6 `Listas En bucles` en python

### Bucle a través de una lista

Puedes recorrer los elementos de la lista usando un bucle:`for`

### Ejemplo

Imprime todos los elementos de la lista, uno por uno:

```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```

**Descubre más sobre los bucles en nuestro capítulo Python For Loops.`for`**

### Loop a través de los números índice

También puedes recorrer los elementos de la lista consultando su número de índice.

Utiliza las funciones y para crear un iterable adecuado.`range()` `len()`

### Ejemplo

Imprime todos los elementos consultando su número de índice:

```python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```

**El iterable creado en el ejemplo anterior es .`[0, 1, 2]`**

### Usando un bucle de tiempo

Puedes recorrer los elementos de la lista usando un bucle.while

Utiliza la función para determinar la longitud de la lista, Luego empieza en 0 y recorre los elementos de la lista consultando sus índices.`len()`

Recuerda aumentar el índice en 1 después de cada iteración.

### Ejemplo

Imprime todos los elementos, usando un lazo para avanzar a través de todos los números de índicewhile

```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
```

### Bucles usando la comprensión de listas

List Comprehension ofrece la sintaxis más corta para recorrer listas en bucle:

### Ejemplo

Un lazo abreviado que imprimirá todos los elementos de una lista:`for`

```python
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
```
