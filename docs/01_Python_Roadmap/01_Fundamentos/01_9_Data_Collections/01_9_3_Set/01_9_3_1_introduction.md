# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Conjuntos `set`)

## 11.3.1 `JSet` en python

```python
myset = {"apple", "banana", "cherry"}
```

### ¿Qué son?
En Python, un `set` (`conjunto`) es una colección desordenada de elementos únicos. No permite elementos duplicados y es muy útil para operaciones matemáticas de conjuntos como unión, intersección y diferencia.

Los conjuntos se utilizan para almacenar varios elementos en una sola variable.

Set es uno de los 4 tipos de datos integrados en Python que se utilizan para almacenar colecciones de los otros 3 son `Lista`, `Tuple` y `Diccionario`, todos con diferentes cualidades y usos.

### Características principales

**`No ordenado:** No mantiene el orden de inserción.

**`Elementos únicos:** Los duplicados se eliminan automáticamente.

**`Mutable:`** Puedes agregar o eliminar elementos.

**`Tipos permitidos:`** Solo admite elementos inmutables (`números`, `cadenas`, `tuplas nmutables`).

### Ejemplo básico de creación y uso

```python
# Crear un set
mi_set = {1, 2, 3, 4}
print(mi_set) # Salida: {1, 2, 3, 4}

# Agregar un elemento
mi_set.add(5)
print(mi_set) # Salida: {1, 2, 3, 4, 5}

# Eliminar un elemento
mi_set.remove(3)
print(mi_set) # Salida: {1, 2, 4, 5}
```

### Operaciones comunes con sets

**`Unión:`** Combina elementos de dos sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
print(union) # Salida: {1, 2, 3, 4, 5}
```

**`Intersección:`** Encuentra elementos comunes.

```python
interseccion = set1 & set2
print(interseccion) # Salida: {3}
```

**`Diferencia:`** Elementos en un set pero no en el otro.

```python
diferencia = set1 - set2
print(diferencia) # Salida: {1, 2}
```

**`Diferencia simétrica:`** Elementos únicos en ambos sets.

```python
dif_simetrica = set1 ^ set2
print(dif_simetrica) # Salida: {1, 2, 4, 5}
```

### Otros Ejemplos De Uso

```python
# Crear un set
frutas = {"manzana", "banana", "cereza"}
print(frutas)  # El orden puede variar

# Crear un set desde una lista (elimina duplicados)
numeros = set([1, 2, 2, 3, 4, 4])
print(numeros)  # {1, 2, 3, 4}

# Agregar elementos
frutas.add("pera")
print(frutas)

# Eliminar elementos
frutas.remove("banana")  # Lanza error si no existe
frutas.discard("kiwi")   # No lanza error si no existe

# Operaciones de conjuntos
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Unión: {1, 2, 3, 4, 5}
print(A & B)  # Intersección: {3}
print(A - B)  # Diferencia: {1, 2}
print(A ^ B)  # Diferencia simétrica: {1, 2, 4, 5}

```

### type()

Desde la perspectiva de Python, los conjuntos se definen como objetos con el tipo de dato 'set':

```python
<class 'set'>
```

### Ejemplo

¿Cuál es el tipo de dato de un conjunto?

```python
myset = {"apple", "banana", "cherry"}
print(type(myset))
```

### El constructor de conjuntos()

También es posible usar el constructor `set()` para crear un conjunto.

### Ejemplo

Usando el constructor set() para formar un conjunto:

```pytnon
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
```

### Consideraciones importantes

* Los sets no permiten duplicados.

* No son indexables ni ordenados.

* Para crear un set vacío usa `set()`, ya que `{}` crea un diccionario.

Los sets son ideales para trabajar con datos únicos y realizar operaciones rápidas de pertenencia o comparación.
