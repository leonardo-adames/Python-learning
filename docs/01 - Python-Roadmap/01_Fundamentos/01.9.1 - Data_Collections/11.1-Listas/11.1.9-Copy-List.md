# BootCamp Python Sesión 11- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.9 `Copy List` en python

### Copiar una lista

No se puede copiar una lista simplemente escribiendo , porque: solo será una referencia a , y los cambios realizados en también se harán automáticamente en .`list`= `list1` `list2` `list1` `list1` `list2`

### Usa el método `copy()`

Puedes usar el método integrado de la lista para copiar una lista.copy()

### Ejemplo

Haz una copia de una lista con el método:`copy()`

```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```

### Utiliza el método list()

Otra forma de hacer una copia es usar el método incorporado .`list()`

### Ejemplo

Haz una copia de una lista con el método:`list()`

```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
```

### Usa el operador de corte

También puedes hacer una copia de una lista usando el operador (slice).:

### Ejemplo

Haz una copia de una lista con el operador:`:`

```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
```
