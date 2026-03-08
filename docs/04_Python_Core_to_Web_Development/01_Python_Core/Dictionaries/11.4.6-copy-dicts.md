# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Diccionarios `dict`)

## 11.4.3 Copiar diccionarios en python

### Copiar un Diccionario<br>

No se puede copiar un diccionario simplemente escribiendo `dict`2 = `dict1`, porque: dict2solo será una referencia a dict1,<br>
y los cambios realizados en dict1se realizarán automáticamente también en `dict2`.

Hay formas de hacer una copia, una forma es utilizar el método Diccionario incorporado `copy()`.

### Ejemplo

Haz una copia de un diccionario con el método `copy()`:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
```
---
**Otra forma de hacer una copia es utilizar la función incorporada `dict()`.**

#### Ejemplo

**Hacer una copia de un diccionario con la dict() función:**

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```

## ¿Cuál es su propósito?

El propósito del método `dict.copy()` en Python es crear una copia superficial (`shallow copy`) de un diccionario, permitiendo modificar la copia sin afectar al diccionario original en el nivel superior,<br>
pero compartiendo referencias a objetos mutables anidados (como listas o diccionarios dentro del diccionario),<br>
lo que es ideal para duplicar datos simples o cuando los valores son inmutables, y se usa para trabajar con dos diccionarios independientes que no interfieran entre sí. 

## ¿Por qué usar `dict.copy()`?

**Independencia de nivel superior:** Si añades, eliminas o modificas pares clave-valor en la copia, el diccionario original no cambia, y viceversa.<br>
**Simplicidad y eficiencia:** Es más rápido y consume menos memoria que una copia profunda (deepcopy) porque no necesita clonar recursivamente todos los objetos anidados, solo la estructura principal.<br>
**Programación defensiva:** Permite devolver una versión de los datos que puede ser manipulada sin alterar la fuente original, evitando efectos secundarios inesperados. <br>

## Limitaciones (Copia Superficial):

**Objetos anidados mutables:** Si tu diccionario contiene listas o diccionarios como valores (ej. {`'data': [1, 2]`}),<br>
la copia superficial crea una nueva referencia a esa misma lista. Si modificas la lista en la copia, también se modificará en el original, lo cual puede no ser lo deseado. 

### Ejemplo

```python
original = {'a': 1, 'b': [10, 20]}
copia_superficial = original.copy()

# Modificando la copia (nivel superior)
copia_superficial['a'] = 99
print(f"Original: {original}") # {'a': 1, 'b': [10, 20]}
print(f"Copia: {copia_superficial}") # {'a': 99, 'b': [10, 20]}

# Modificando el objeto anidado (lista)
copia_superficial['b'].append(30)
print(f"Original: {original}") # {'a': 1, 'b': [10, 20, 30]} <--- ¡Se modificó!
print(f"Copia: {copia_superficial}") # {'a': 99, 'b': [10, 20, 30]}
```
## En resumen:<br>
Usa `dict.copy()` cuando necesites una copia independiente del diccionario principal,<br>
pero ten cuidado con los objetos mutables anidados; para aislarlos completamente, necesitarías `copy.deepcopy()`. 

