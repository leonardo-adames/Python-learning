# BootCamp Python Sesión 9 - Condicionales

## 9.2 Condicional `else` en python

### La palabra clave Else

* La palabra clave `else` detecta cualquier cosa que no esté captada por las condiciones anteriores, es decir, todo lo que no este captado dentro de las condiciones con las sentencias `if` y/o `elif`.

* La sentencia `else` se ejecuta cuando la condición `if` (y cualquier condición de `elif`) se evalúa como `False`.

Ejemplo

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

* En este ejemplo, a es mayor que b, Entonces la primera condición no es verdadera, también la condición de Elif no es verdadera, Así que vamos a la condición else e imprimimos en pantalla que "A es mayor que B".

### Si no, sin Elif

*También puedes tener un sin los :`else` `elif`

```python
Ejemplo
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
```

* Esto crea una elección simple de dos vías: si la condición es verdadera, ejecutar un bloque; de lo contrario, ejecuta el bloque else.

### ¿Cómo funciona Else?

* La sentencia else proporciona una acción predeterminada cuando ninguna de las condiciones anteriores es cierta. Piénsalo como un "`catch-all`" para cualquier escenario que no cubra tus declaraciones `if` y `ellif`.

* **Nota:** La afirmación else debe ser la última. No puedes tener una elixida después de otra cosa.

Ejemplo

* Números pares o impares comprobados:

```python
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
```

### Cadena completa de `If-Elif-Else`

* Puedes combinar if, elif y other para crear una estructura integral de toma de decisiones.

Ejemplo

* Clasificador de temperatura:

```python
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")
```

### Else como respaldo

* La sentencia else actúa como un respaldo que se ejecuta cuando ninguna de las condiciones anteriores es verdadera. Esto lo hace útil para el manejo de errores, la validación y la provisión de valores por defecto.

Ejemplo

* Validación de la entrada del usuario:

```python
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
```
