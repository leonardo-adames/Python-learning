# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Conjuntos `set`)

## 11.3.3 `Añadir Elementos En Set` en python

### Añadir elementos

Una vez creado un conjunto, no puedes cambiar sus objetos, pero sí puedes añadir nuevos.

Para añadir un elemento a un conjunto, utiliza el `método.add()`

### Ejemplo

Añade un elemento a un conjunto, usando el método:`add()`

```python
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```

### Añadir conjuntos

Para añadir elementos de otro conjunto al conjunto actual, utiliza el `método.update()`

Ejemplo

Añadir elementos de `tropical` en `thisset`: 

```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
```

### Añadir cualquier iterable

El objeto en el método no tiene Para ser un conjunto, puede ser cualquier objeto iterable (tuplas, listas, diccionarios, etc.).`update()`

### Ejemplo

Añadir elementos de una lista a en el conjunto:

```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
```
