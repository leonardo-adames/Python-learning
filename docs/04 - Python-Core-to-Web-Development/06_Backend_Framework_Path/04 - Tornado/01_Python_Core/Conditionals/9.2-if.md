# BootCamp Python Sesión 9 - Condicionales

## 9.2 Condicionales en python

### Sentencias `If` En Python

Python soporta las condiciones lógicas habituales de las matemáticas:

    Igual: a == b
    No es igual: a != b
    Menos que: a < b
    Menor o igual a: a <= b
    Mayor que: a > b
    Mayor o igual a: a >= b
    
* Estas condiciones pueden usarse de varias maneras, siendo las más comunes en sentencias `"if"` y `bucles`.

* Una sentencia `"if"` se escribe usando la palabra clave `if`.

### SINTAXIS BÁSICA:

```python
if(condicion):
    Bloque de instrucciones 
```

Ejemplo

* Afirmación del si:

```python
a = 33
b = 200
if b > a:
  print("b is greater than a") # el print siempre se identa dentor del if.
```

* En este ejemplo usamos dos variables, `a` y `b`, que se utilizan como parte de la sentencia `if` para comprobar si b es mayor que `a`. Como a es `33`, y `b` es `200`, Sabemos que `200` es mayor que `33`, así que imprimimos en pantalla que "`B` es mayor que `A"`.

### Cómo funcionan las sentencias de si

* La sentencia `if` evalúa una condición (una `expresión` que resulta en `Verdadero o Falso`). Si la condición es verdadera, se ejecuta el bloque de código dentro de la instrucción `if`. Si la condición es falsa, se omite el bloque de código.

Ejemplo

* Comprobar si un número es positivo:

```python
number = 15
if number > 0:
  print("The number is positive")
```

### Hendidura

* Python se basa en la `sangría` (espacio en blanco al inicio de una línea) para definir el alcance en el código. Otros lenguajes de programación suelen usar corchetes para este propósito.

Ejemplo

* *entencia de `'If' sin sangría` (generará un error):

```python
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
```
**Nota:** Puedes usar espacios o tabulaciones para la sangría, pero debes usar la misma cantidad de sangría para todas las sentencias dentro del mismo bloque de código.

### Sentencias múltiples en el bloque If

* Puedes tener varias sentencias dentro de un bloque if. Todas las sentencias deben estar indentadas al mismo nivel.

Ejemplo

* Múltiples sentencias en un bloque `if`:

```python
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
```

### Uso de variables en condiciones

* Las variables booleanas pueden usarse directamente en sentencias if sin operadores de comparación.

Ejemplo

* Usando una variable booleana:

```python
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
```

* Python puede evaluar muchos tipos de valores como `Verdadero `o `Falso` en una sentencia `if`.

* Cero (`0`), cadenas vacías (`"""`), Ninguna y colecciones vacías se tratan como `Falsas`. Todo lo demás se trata como `Verdadero`.

* Esto incluye números positivos (`5`), números negativos (`-3`) y cualquier cadena no vacía (incluso "`Falso`" se considera `Verdadero` porque es una cadena no vacía).
