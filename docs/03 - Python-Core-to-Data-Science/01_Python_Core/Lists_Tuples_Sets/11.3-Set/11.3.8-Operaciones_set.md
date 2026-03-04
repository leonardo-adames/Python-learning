# Learning Python Level 1 - Sesión 11 Colecciónes

## 11.3.8 - Frozenset - Sets inmutables en Python

### Operaciones con Sets en Python

**Agregar elementos**<br>
Los conjuntos en Python tienen el método add() que se utiliza para agregar un solo elemento al conjunto.

```PYTHON
mi_set.add(6)  # Agrega el elemento 6 al set
```
---

**Eliminar elementos**<br>
Los conjuntos en Python tienen **el método** `remove()` **que se utiliza para eliminar un elemento específico del conjunto**.

Además, el método `discard()` también se puede utilizar para eliminar un elemento, pero no arrojará un error si el elemento no está presente en el conjunto.

```python
mi_set.remove(3)  # Elimina el elemento 3 del set
mi_set.discard(2)  # Elimina el elemento 2 si está presente
```
---

**Unión de sets**<br>
La unión de conjuntos se puede realizar utilizando el método `union()` o el operador `|`. Esto crea un nuevo conjunto que contiene todos los elementos de ambos conjuntos originales, eliminando duplicados.

```python
union_set = mi_set.union(mi_otro_set)  # Une los dos sets en uno nuevo
union_set = mi_set | mi_otro_set  # Lo mismo utilizando el operador |
```
---

**Intersección de sets**<br>
La intersección de conjuntos se puede realizar utilizando el método intersection() o el operador &. Esto crea un nuevo conjunto que contiene solo los elementos que están presentes en ambos conjuntos originales.

```python
interseccion_set = mi_set.intersection(mi_otro_set)  # Obtiene la intersección de los sets
interseccion_set = mi_set & mi_otro_set  # Lo mismo utilizando el operador &
```
---

**Diferencia de sets**<br>
La diferencia entre conjuntos se puede calcular utilizando el método difference() o el operador -. Esto crea un nuevo conjunto que contiene solo los elementos que están presentes en el primer conjunto pero no en el segundo.

```python
diferencia_set = mi_set.difference(mi_otro_set)  # Obtiene la diferencia entre los sets
diferencia_set = mi_set - mi_otro_set  # Lo mismo utilizando el operador -
```