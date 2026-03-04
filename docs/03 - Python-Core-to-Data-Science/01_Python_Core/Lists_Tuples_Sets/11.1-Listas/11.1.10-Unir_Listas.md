# BootCamp Python Sesión 11- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.10 `Union De Listas` en python

### Listas de Incorporación

Existen varias formas de unir o concatenar dos o más listas en Python.

Una de las formas más sencillas es usando el operador.`+`

### Ejemplo

Únete a dos listas:

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
```

Otra forma de unir dos listas es añadiendo todos los elementos de la lista2 en Lista1, `uno por uno`:

### Ejemplo

Añadir lista2 a lista1:

```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
```

O puedes usar el método, donde el propósito es añadir elementos de una lista a otra Lista:`extend()`

### Ejemplo

Utiliza el método para añadir lista2 al final de lista1:extend()

```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
```
