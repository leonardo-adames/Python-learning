# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (`Las Tuplas`)

## 11.2.5 `Tuplas De Bucles` en python

### Bucle a través de una tupla

Puedes hacer un bucle entre los elementos de la tupla usando un bucle.`for`

### Ejemplo

Iterar entre los elementos e imprimir los valores:

```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```

### Loop a través de los números índice

También puedes recorrer los elementos de la tupla consultando su número de índice.

Utiliza las funciones y para crear un iterable adecuado.r`ange()` `len()`

### Ejemplo

Imprime todos los elementos consultando su número de índice:

```python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```

### Usando un bucle de tiempo

Puedes hacer un bucle entre los elementos de la tupla usando un bucle.`while`

Utiliza la función para determinar la longitud de la tupla, Luego empieza en 0 y recorre los elementos de la tupla consultando sus índices.`len()`

Recuerda aumentar el índice en 1 después de cada iteración.

### Ejemplo

```python
Imprime todos los elementos, usando un bucle para revisar todos los números de índice:while

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```
