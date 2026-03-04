# BootCamp Python Sesión 9 - Condicionales

## 9.6 Condicionales y `Operadores Lógicos` en python

### Operadores lógicos en Python

Los operadores lógicos se utilizan para combinar sentencias condicionales. Python tiene tres operadores lógicos:

    and - Devuelve Verdadero si ambas afirmaciones son verdaderas

    or - Devuelve Verdadero si una de las afirmaciones es verdadera

    not - Revierte el resultado, devuelve False si el resultado es verdadero

### El operador `and`

* La palabra clave es un operador lógico, y se utiliza para combinar sentencias condicionales. Ambas condiciones deben ser verdaderas para que toda la expresión sea cierta. `and`

Ejemplo

Prueba si `a` es mayor que `b`, Y si `a`es mayor que `c`: `a > b` or `c > a`

```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Entonces c es mayor que b")
```

### El operador de `or`

* La palabra clave es un operador lógico, y se utiliza para combinar sentencias condicionales. Al menos una condición debe ser verdadera para que toda la expresión sea verdadera.or

Ejemplo

Prueba si `a` es mayor que `b`, O si `b`es mayor que `c`: `a > b` or `b > c`

```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```

### El operador not

* La palabra clave es un operador lógico, y se utiliza para revertir el resultado de la afirmación condicional.not

Ejemplo

* Prueba si `a` `not` es mayor que `b`: `a` > `b`

```python
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```

### Combinación de múltiples operadores

* Puedes combinar múltiples operadores lógicos en una sola expresión. Python evalúa no first, then y, then o.

Ejemplo

* Combinando , , `y` :`and` `or` `not`

```python
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
```

### Tablas de Verdad

* Entender cómo funcionan los operadores lógicos con diferentes valores:

### Tabla de Verdad de Operador `and`

| Condición 1 | Condición 2 | Resultado |
| ----------- | ----------- | --------- |
| Cierto      | Cierto      | Cierto    |
| Cierto      | Falso       | Falso     |
| Falso       | Cierto      | Falso     |
| Falso       | Falso       | Falso     |

### Tabla de Verdad de Operador `or`

| Condición 1 | Condición 2 | Resultado |
| ----------- | ----------- | --------- |
| Cierto      | Cierto      | Cierto    |
| Cierto      | Falso       | Cierto    |
| Falso       | Cierto      | Cierto    |
| Falso       | Falso       | Falso     |

### Uso de paréntesis para mayor claridad

* Al combinar múltiples operadores lógicos, utiliza paréntesis para dejar claras tus intenciones y controlar el orden de la evaluación.

Ejemplo

* Uso de paréntesis para condiciones complejas:

```python
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
```

### Más ejemplos

Ejemplo

* Comprobación de autenticación de usuario:

```python
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
```

Ejemplo

* Comprobación de distancia con operadores lógicos:

```python
score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")
```
