# Learning Python Level 1 - Sesión 11 Colecciónes

## 11.3.7 - Frozenset - Sets inmutables en Python

### Qué son y cómo usar Sets en Python

Los `Sets`, o conjuntos, son estructuras de datos que nos permiten almacenar colecciones de elementos únicos y no ordenados.

Esto significa que no puede haber duplicados en un `set` y los elementos no están ordenados por posición

>Características de los sets:<br>
>- Elementos Únicos: Los sets no pueden contener elementos duplicados, por lo que cada elemento es único<br>
>- Desordenados: Los elementos en un set no tienen un orden específico y no se garantiza que se mantenga el orden >- en el que fueron agregados

### Creación de sets
Los conjuntos en Python se pueden crear utilizando llaves `{}`.

En este caso, se enumeran los elementos separados por comas dentro de las llaves para inicializar el conjunto.

```python
# Crear un set con elementos
mi_set = {1, 2, 3}
```
>Por ejemplo, aquí hemos creado un Set `{1, 2, 3}` a partir de una Lista que contenía `[1, 2, 3]`.

---
<br>

### Ejemplos prácticos

**Eliminación de duplicados en listas**<br>
Para eliminar duplicados de una lista en Python, se puede convertir la lista a un conjunto utilizando la función `set()`.

```python
lista_con_duplicados = [1, 2, 3, 4, 1, 2, 5]
conjunto_sin_duplicados = set(lista_con_duplicados)
```
>Los `Sets` en Python no permiten elementos duplicados, por lo que al convertir la lista a un conjunto, automáticamente se eliminarán los duplicados.

---

**Verificación de pertenencia**<br>
Para verificar si un elemento está presente en un conjunto, se puede utilizar la expresión in. Esta expresión devuelve True si el elemento está presente en el conjunto y False si no lo está.

```python
if 3 in mi_set:
    print("El elemento 3 está presente en el set.")
```
---
**Operaciones de conjuntos**<br>
Python ofrece varios métodos integrados para realizar operaciones de conjuntos, como unión, intersección y diferencia.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Unión de sets
union = set1.union(set2)  # Resultado: {1, 2, 3, 4, 5}

# Intersección de sets
interseccion = set1.intersection(set2)  # Resultado: {3}

# Diferencia de sets
diferencia = set1.difference(set2)  # Resultado: {1, 2}
```
## Por último, recalcar que al igual quer los conjuntos generales, también se puede ejerceroperaciones de conjunto sobre los `frozenset`
