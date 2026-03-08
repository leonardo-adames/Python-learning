# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Diccionarios `Dict`)

## 11.4.1 `Diccionarios` en python

### ¿Qué son?

Los diccionarios en Python son colecciones mutables y no ordenadas (a partir de `Python 3.7` son ordenados) que almacenan datos en pares de clave-valor (`key-value`), permitiendo acceder a un valor mediante su clave única, similar a un diccionario real donde buscas una palabra (`clave`) para obtener su definición (`valor`). Se definen con llaves `{}` y sus claves deben ser tipos inmutables (`cadenas`, `números`, `tuplas`), mientras que los valores pueden ser de cualquier tipo, incluyendo listas u otros diccionarios. 

## Características principales

* **Pares clave-valor:** Almacenan información como {`clave1: valor1`, `clave2: valor2`}.
* 
* **Claves únicas:** Cada clave dentro de un diccionario debe ser única; si se repite, el último valor asignado prevalece.
*  
* **Inmutables (claves):** Las claves deben ser tipos de datos inmutables como `str`, `int`, `float`, `tuple`, no `list` o `dict`.
* 
* **utables (valores y diccionario):** Los valores pueden ser cualquier tipo de dato y se pueden modificar, añadir o eliminar pares `clave-valor`.
* 
* **Acceso:** Se accede a los valores usando la clave entre corchetes, `mi_diccionario['clave']`, o con el método `.get('clave')`.
* 
* **Indexados por clave:** A diferencia de las listas (`indexadas por posición numérica`), se accede por un nombre significativo (`la clave`).

### Ejemplo

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid",
    "intereses": ["leer", "senderismo"]
}

# Acceder a un valor
print(persona["nombre"])  # Salida: Ana

# Modificar un valor
persona["edad"] = 26

# Añadir un nuevo par clave-valor
persona["email"] = "ana@ejemplo.com"

# Iterar sobre el diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

```
### Salida
```python

```

### ¿Ordenado o desordenado?

A partir de la versión `3.7` de `Python`, los diccionarios están ordenados . En `Python 3.6` y versiones anteriores, están desordenados .

Cuando decimos que los diccionarios están ordenados, significa que los elementos tienen un orden definido, y ese orden no cambiará.

Desordenado significa que los elementos no tienen un orden definido, no se puede hacer referencia a un elemento mediante un índice.

### Cambiable

Los diccionarios son modificables, lo que significa que podemos cambiar, agregar o eliminar elementos después de que se haya creado el diccionario.

### No se permiten duplicados

Los diccionarios no pueden tener dos elementos con la misma clave:

### Ejemplo

Los valores duplicados sobrescribirán los valores existentes:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
```

## Longitud del diccionario

Para determinar cuántos elementos tiene un diccionario, utilice la función `len()`

### Ejemplo
Imprima el número de elementos del diccionario:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
```

## Elementos del diccionario - Tipos de datos

Los valores de los elementos del diccionario pueden ser de cualquier tipo de datos:

### Ejemplo

Tipos de datos de `cadena `, `int`, `booleano` y `lista`:

```python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```

 ## tipo()
Desde la perspectiva de Python, los diccionarios se definen como objetos con el tipo de datos `'dict'`:

`<class 'dict'>`

### Ejemplo

Imprima el tipo de datos de un diccionario:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```

## El constructor `dict()`

También es posible utilizar el constructor `dict()` para crear un diccionario.

### Ejemplo<br>
Usando el método `dict()` para crear un diccionario:
```python
thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)
```

