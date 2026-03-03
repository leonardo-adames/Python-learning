# BootCamp Python Sesión 101- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.5 `Eliminar Elementos a Una Listas` en python

### Eliminar el elemento especificado

El método elimina el elemento especificado.`remove()`

### Ejemplo

Quita "plátano":

```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

Si hay más de un elemento con el valor especificado, el método elimina el primero Ocurrencia:remove()

### Ejemplo

Elimina la primera aparición de `"plátano"`:

```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
```

### Eliminar índice especificado

El método elimina lo especificado Índice.`pop()`

### Ejemplo

Elimina el segundo elemento:

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
```

**Si no especificas el índice, el método elimina el último elemento.`pop()`**

### Ejemplo

Elimina el último elemento:

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
La palabra clave también elimina la especificación Índice:del
```

### Ejemplo

Elimina el primer elemento:

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```

**La palabra clave también puede eliminar la lista por completo.`del`**

### Ejemplo

Elimina toda la lista:

```python
thislist = ["apple", "banana", "cherry"]
del thislist
```

### Borrar la lista

El método vacía la lista.`clear()`

La lista sigue ahí, pero no tiene contenido.

### Ejemplo

Borrar el contenido de la lista:

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```

