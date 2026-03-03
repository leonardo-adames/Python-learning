# BootCamp Python Sesión 101- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.3 `Añadir Elementos a Una Listas` en python

### Añadir elementos

Para añadir un elemento al final de la lista, utiliza el método:`append()`

### Ejemplo

Usando el método para añadir un elemento:append()

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```

### Elementos insertados

Para insertar un elemento de lista en un índice especificado, utiliza el método.`insert()`

El método inserta un ítem en el índice especificado:insert()

### Ejemplo

Inserta un elemento como segunda posición:

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```

**Nota:** Como resultado de los ejemplos anteriores, las listas ahora contendrán 4 elementos.

### Extender la lista

Para añadir elementos de otra lista a la lista actual, utiliza el método.`extend()`

### Ejemplo

Añadir los elementos de a :tropicalthislist

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```

***Los elementos se añadirán al final de la lista.***

### Añadir cualquier iterable

El método no tiene que añadir listas, puedes añadir cualquier objeto iterable (tuplas, conjuntos, diccionarios etc.).`extend()`

### Ejemplo

Añadir elementos de una tupla a una lista:

```python
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
```
