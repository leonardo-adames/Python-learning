# BootCamp Python Sesión 11- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.8 `Sort List` en python

### Ordenar lista alfanuméricamente

Los objetos de la lista tienen un método que ordena la lista alfanuméricamente, ascendente, por defecto:sort()

### Ejemplo

Ordena la lista alfabéticamente:

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```

### Ejemplo

Ordena la lista numéricamente:

```python
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
```

### Ordenamiento descendente

Para ordenar descendente, usa el argumento de la palabra clave :reverse = True

### Ejemplo

Ordena la lista descendiente:

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```

### Ejemplo

Ordena la lista descendiente:

```python
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
```

### Función de ordenación personalizada

También puedes personalizar tu propia función usando el argumento de la palabra clave .`key = function`

La función devolverá un número que se usará para ordenar la lista (la número más bajo primero):

### Ejemplo

Ordena la lista según lo cerca que esté el número de 50:

```python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
```

### Clasificación insensible a mayúsculas minúsculas

Por defecto, el método es sensible a mayúsculas y mayúsculas, lo que resulta en que todas las letras mayúsculas se ordenen antes que las minúsculas:`sort()`

### Ejemplo

La clasificación con distinción de mayúsculas minúsculas puede dar un resultado inesperado:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
```

Por suerte, podemos usar funciones integradas como funciones clave al ordenar una lista.

Así que si quieres una función de ordenación insensible a mayúsculas minúsculas, usa `str.lower` como función clave:

### Ejemplo

Haz una especie de lista insensible a mayúsculas y minúsculas:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```

### Orden inverso

¿Y si quieres invertir el orden de una lista, independientemente del alfabeto?

El método invierte el orden de ordenación actual de los elementos.reverse()

### Ejemplo

Invierte el orden de los elementos de la lista:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
```
