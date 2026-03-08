# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Diccionarios `dict`)

## 11.4.3 Agregar elementos del diccionario en python

### Agregar elementos<br>
Para agregar un elemento al diccionario se utiliza una nueva clave de índice y se le asigna un valor:

### Ejemplo

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```

## Actualizar diccionario

El método `update()` actualizará el diccionario con los elementos de un argumento dado. <br>
Si el elemento no existe, se añadirá.

El argumento debe ser un diccionario o un objeto iterable con pares `clave:valor`.

### Ejemplo

Agregue un elemento de color al diccionario utilizando el método `update()`:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
```
# Eliminar elementos del diccionario en Python

## Eliminación de elementos

Existen varios métodos para eliminar elementos de un diccionario:

### Ejemplo

El método `pop()` elimina el elemento con el nombre de clave especificado:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```

### Ejemplo

El método `popitem()` elimina el último elemento insertado (en versiones anteriores a 3.7, se elimina un elemento aleatorio):

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
```

### Ejemplo

La delpalabra clave `del` el elemento con el nombre de clave especificado:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
```

### Ejemplo

La delpalabra clave `del` también puede eliminar el diccionario por completo:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
```

### Ejemplo

El método `clear()` vacía el diccionario:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
```
