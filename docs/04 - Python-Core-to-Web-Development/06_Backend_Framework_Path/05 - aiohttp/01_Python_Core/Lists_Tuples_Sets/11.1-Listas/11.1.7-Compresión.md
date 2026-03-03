# BootCamp Python Sesión 11- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.7 `Comprensión De Listas` en python

### Comprensión de listas

La comprensión de listas ofrece una sintaxis más corta cuando quieres crear una nueva lista basada en los valores de un lista existente.

### Ejemplo:

Según una lista de frutas, quieres una nueva lista, que contenga solo las frutas con la letra `"A"` en el nombre.

Sin comprensión de listas tendrás que escribir una declaración con una prueba condicional en el interior:for

### Ejemplo

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

Con la comprensión de listas puedes hacer todo eso con solo una línea de código:

### Ejemplo

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

### La sintaxis

```python
newlist = [expression for item in iterable if condition == True]
```

**El valor de retorno es una lista nueva, dejando la lista antigua sin cambios.**

### Estado

La condición es como un filtro que solo acepta los elementos que evalúan hasta .True

### Ejemplo

Solo acepta artículos que no sean + "apple"+ :

```python
newlist = [x for x in fruits if x != "apple"]
```

La condición devolverá para todos los elementos que no sean luego "manzana", haciendo que la nueva lista contenga todas las frutas excepto `"manzana"`.`True`

La condición es opcional y puede omitirse:

### Ejemplo

Sin declaración:`if`

```python
newlist = [x for x in fruits]
```

### Iterable

El iterable puede ser cualquier objeto iterable, como una lista, tupla, conjunto, etc.

### Ejemplo

Puedes usar la función para crear un iterable:`range()`

```

newlist = [x for x in range(10)]
```

Mismo ejemplo, pero con una condición:

### Ejemplo

Aceptar solo números inferiores a 5:

```python
newlist = [x for x in range(10) if x < 5]
```

### Expresión

La expresión es el elemento actual en la iteración, pero también es el resultado, que puedes manipular antes de que acabe como un elemento de lista en el nuevo Lista:

### Ejemplo

Establece los valores de la nueva lista en mayúsculas:

```python
newlist = [x.upper() for x in fruits]
```

Puedes ajustar el resultado a tu gusto:

### Ejemplo

Configura todos los valores de la nueva lista como 'hola':

```python
newlist = ['hello' for x in fruits]
```

La expresión también puede contener condiciones, no como un filtro, sino como un Forma de manipular el resultado:

### Ejemplo

Devuelve "naranja" en lugar de "plátano":

```python
newlist = [x if x != "banana" else "orange" for x in fruits]
```

La expresión en el ejemplo anterior dice:

**Devuelve el artículo si no es plátano, si es plátano devuélveme naranja.**
