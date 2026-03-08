# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Diccionarios Dict)

## 11.4.2 Indexación de Diccionarios en python

### Acceder a los elementos

Puede acceder a los elementos de un diccionario consultando su nombre de clave, dentro de corchetes:

### Ejemplo

Obtenga el valor de la clave "`modelo`":

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
```

También hay un método llamado `get()` que te dará el mismo resultado:

### Ejemplo

Obtenga el valor de la clave "`modelo`":

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.get("model")
```

## Obtener llaves

El método `keys()` devolverá una lista de todas las claves del diccionario.

### Ejemplo

Obtenga una lista de las claves:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
```

La lista de claves es una vista del diccionario,<br>
lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de claves.

### Ejemplo

Agregue un nuevo elemento al diccionario original y observe que la lista de claves también se actualiza:

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
```
## Obtener valores

El método `values()` devolverá una lista de todos los valores del diccionario.

### Ejemplo

Obtenga una lista de los valores:

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = thisdict.values()
```

La lista de valores es una vista del diccionario,<br>
lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de valores.

### Ejemplo

Realice un cambio en el diccionario original y verá que la lista de valores también se actualiza:

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
```
```python
Ejemplo
Agregue un nuevo elemento al diccionario original y observe que la lista de valores también se actualiza:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
```

## Obtener artículos

El método `items()` devolverá cada elemento de un diccionario, como tuplas en una lista.

### Ejemplo

Obtenga una lista de los pares `clave:valor`

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = thisdict.items()
```

La lista devuelta es una vista de los elementos del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de elementos.

### Ejemplo

Realice un cambio en el diccionario original y verá que la lista de elementos también se actualiza:

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
```

### Ejemplo

Agregue un nuevo elemento al diccionario original y observe que la lista de elementos también se actualiza:

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
```

## Comprobar si existe la clave

Para determinar si una clave específica está presente en un diccionario, utilice la inpalabra clave:

### Ejemplo

Comprueba si "modelo" está presente en el diccionario:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
```
