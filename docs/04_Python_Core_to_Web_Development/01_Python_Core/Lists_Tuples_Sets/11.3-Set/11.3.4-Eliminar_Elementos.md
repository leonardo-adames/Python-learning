# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Conjuntos `set`)

## 11.3.4 `Eliminar Elementos En Set` en python

### Eliminar elementos

Para eliminar un elemento de un conjunto, utiliza el método`.remove()`, o el método.`discard()`

### Ejemplo

Elimina "plátano" usando el método: `remove()`

```python
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print
(thisset)
```

**Nota:** Si el elemento a eliminar no existe, se generará un error.`remove()`

### Ejemplo

```python
Elimina "plátano" usando el método:discard()

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
```

**Nota:** Si el elemento a eliminar no existe, NO aparecerá un error.`discard()`

También puedes usar el método para eliminar un objeto, pero este método eliminará un objeto aleatorio, así que no puedes estar seguro de qué objeto se elimina.`pop()`

El valor de retorno del método es el Artículo eliminado.`pop()`

### Ejemplo

```python
Elimina un elemento aleatorio usando el método:`pop()`

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
```

**Nota:** Los conjuntos no están ordenados, así que al usar el método, No sabes qué artículo se elimina.`pop()`.

El método vacía el conjunto:`clear()`

```python
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
```

La palabra clave eliminará el conjunto Completamente:`del`

```python
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
```
