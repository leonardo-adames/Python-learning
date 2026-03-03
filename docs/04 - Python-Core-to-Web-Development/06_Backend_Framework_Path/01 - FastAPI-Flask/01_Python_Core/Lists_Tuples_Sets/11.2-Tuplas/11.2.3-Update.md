# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (`Las Tuplas`)

## 11.2.3 `Actualización De Tuplas` en python

Las tuplas son inmutables, lo que significa que no puedes cambiar, añadir ni eliminar elementos una vez creada la tupla.

Pero hay algunas alternativas.

### Cambiar los valores de la tupla

Una vez que se crea una tupla, no se pueden cambiar sus valores. Las tuplas son inmutables, como también se le llama.

Pero hay una solución alternativa. Puedes convertir la tupla en una lista, cambiar la y convertir la lista de nuevo en una tupla.

### Ejemplo

Convierte la tupla en una lista para poder cambiarla:

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```

### Añadir elementos

Como las tuplas son inmutables, no tienen un método incorporado, pero Hay otras formas de añadir elementos a una tupla.`append()`

1. `Convertir en lista`: Al igual que la solución para cambiar una tupla, puedes convertirla en una lista, añadir tu(s) elemento(s) y volver a convertirla en tupla.

### Ejemplo

Convierte la tupla en una lista, añade "naranja" y vuelve a convertirla en tupla:

```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
```

2. `Añadir tupla a una tupla`. Se permite añadir tuplas a tuplas, así que si quieres añadir un elemento, (o varios), crea una nueva tupla con el ítem(es) y añádelo a la tupla existente:

### Ejemplo

Crea una nueva tupla con el valor "`naranja`" y añade esa tupla:

```python
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
```

**Nota:*** Al crear una tupla con un solo elemento, recuerda incluir una coma Después del ítem, de lo contrario no se identificará como tupla.

### Eliminar objetos

**Nota:** No puedes eliminar objetos de una tupla.

Las tuplas son **inmutables**, así que no puedes eliminar objetos De ella, pero puedes usar la misma solución que usamos para cambiar y añadir elementos de la tupla:

### Ejemplo

Convierte la tupla en una lista, elimina "apple" y vuelve a convertirla en tupla:

```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
```

O puedes eliminar la tupla por completo

La palabra clave puede eliminar la tupla Completamente:`del`

```python
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
```
