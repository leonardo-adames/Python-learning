# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (`Las Tuplas`)

## 11.2.6 `Join De Tuplas` en python

### Unir tuplas

Para unir dos o más tuplas puedes usar el operador:`+`

### Ejemplo

Une dos tuplas:

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

### Multiplicar tuplas

Si quieres multiplicar el contenido de una tupla un número dado de veces, puedes usar el operador:`*`

### Ejemplo

Multiplica la tupla de frutos por 2:

```python
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```

### Métodos de tupla

Python tiene dos métodos integrados que puedes usar en tuplas.

**`count()`** Devuelve el número de veces que un valor especificado ocurre en una tupla.

**`index()`** Busca en la tupla un valor especificado y devuelve la posición donde se encontró.
