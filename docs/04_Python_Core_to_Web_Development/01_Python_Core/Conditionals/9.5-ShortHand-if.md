# BootCamp Python Sesión 9 - Condicionales

## 9.5 Condicionales `Short Hand if` en python

### Abreviatura si

* Si solo tienes una sentencia que ejecutar, puedes ponerla en la misma línea que la sentencia.if

Ejemplo

* Una frase:`if`

```python
a = 5
b = 2
if a > b: print("a is greater than b")
```

**Nota:** Aun así, necesitas el colon después de la condición.:

### Abreviatura Si ... Si no

* Si tienes una sentencia para y otra para , puedes ponerlas en la misma línea usando una expresión condicional:ifelse

Ejemplo

* Una línea / que imprime un valor:ifelse

```python
a = 2
b = 330
print("A") if a > b else print("B")
```

Esto se denomina `expresión condicional` (a veces conocida como "operador ternario").

### Asignar un valor con si ... Si no

* También puedes usar una línea / para elegir un valor y asignarlo a una variable:`if` `else`

```python
Ejemplo
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
```

La sintaxis sigue este patrón:

    variable =  value_if_true if condition else value_if_false

### Múltiples condiciones en una misma línea

* Puedes encadenar expresiones condicionales, pero mantenlo corto para que siga siendo legible:

Ejemplo

* Una línea, tres resultados:

```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

Ejemplos prácticos

* Los operadores ternarios son especialmente útiles para asignaciones simples e instrucciones de retorno.

Ejemplo

* Encontrar el máximo de dos números:

```python
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
```

Ejemplo

* Establecer un valor por defecto:

```python
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
```

### Cuándo usar la taquigrafía si

* Abreviatura de las sentencias if y los operadores ternarios deben usarse cuando:

* La condición y las acciones son sencillas

* Mejora la legibilidad del código

* Quieres hacer una tarea rápida basada en una condición

**Importante:** Aunque si las sentencias pueden ser más concisas, evita usarlas en exceso para condiciones complejas. Para facilitar la legibilidad, utiliza sentencias if-else normales cuando se trate de múltiples líneas de código o lógica compleja.
