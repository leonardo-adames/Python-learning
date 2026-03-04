# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Diccionarios `dict`)

## 11.4.5 Bucles diccionario en python

### Recorrer un diccionario<br>
Puedes recorrer un diccionario mediante un forbucle.

Al recorrer un diccionario, el valor de retorno son las claves del diccionario, pero también existen métodos para devolver los valores .

### Ejemplo

**Imprima todos los nombres de las claves en el diccionario, uno por uno:**

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)
```
---

**Imprima todos los valores del diccionario, uno por uno:**

### Ejemplo

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(thisdict[x])
```
---

**También puedes utilizar el values()método para devolver valores de un diccionario:**

### Ejemplo

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.values():
  print(x)
```
---

**Puede utilizar el keys()método para devolver las claves de un diccionario:**

### Ejemplo

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.keys():
  print(x)
```
---
Ejemplo

**Recorra tanto las claves como los valores , utilizando el método `items()`:**

```oython
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x, y in thisdict.items():
  print(x, y)
```

