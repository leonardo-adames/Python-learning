# BootCamp Python Sesión 9 - Condicionales

## 9.3 Condicional `elif` en python

### La palabra clave Elif

* La palabra clave `elif` es la forma en que Python dice "si las condiciones anteriores no fueran ciertas, entonces prueba esta condición".

* La palabra clave `elif` te permite comprobar varias expresiones para True y ejecutar un bloque de código tan pronto como una de las condiciones se evalúe a True.

Ejemplo

```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

* En este ejemplo, `a` es igual a `b`, así que la primera condición no es verdadera, pero la condición de `elif` sí es cierta, por lo que imprimimos en pantalla que "a y b son iguales".

### Sentencias de Elif Múltiples

* Puedes tener tantas declaraciones de respuesta como necesites. Python comprueba cada condición en orden y ejecuta la primera que es verdadera.

Ejemplo

* Pruebas de múltiples condiciones:

```python
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
```

En este ejemplo, el programa comprueba cada condición en orden. Como la puntuación es 75, imprime "`Calificación: C`" (la primera condición que se evalúa como verdadera).

### Cómo funciona Elif

* Cuando usas elif, Python evalúa las condiciones de arriba a abajo. En cuanto encuentra una condición que es verdadera, ejecuta ese bloqueo y omite todas las condiciones restantes.

* Importante: Solo se ejecutará la primera condición verdadera. Incluso si se cumplen varias condiciones, Python se detiene tras ejecutar el primer bloque correspondiente.

Ejemplo

* Categorización de los grupos de edad:

```python
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
```

### Cuándo usar Elif

* Usa Elif cuando tengas varias condiciones mutuamente excluyentes para comprobar. Esto es más eficiente que usar varias sentencias if separadas porque Python deja de comprobar una vez que encuentra una condición verdadera.

Ejemplo

* Comprobador de día de semana:

```python
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
```
