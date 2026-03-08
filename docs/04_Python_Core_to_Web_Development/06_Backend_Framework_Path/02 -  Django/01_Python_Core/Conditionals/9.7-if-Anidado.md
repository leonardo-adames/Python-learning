# BootCamp Python Sesión 9 - Condicionales

## 9.7 Condicionales // `If Anidados` en python

### Sentencias If anidadas

Puedes tener declaraciones dentro de declaraciones. Esto se llama sentencias anidadas.ififif

Ejemplo

```python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```

* En este ejemplo, la sentencia interna `if` solo se ejecuta si la condición exterior (`x > 10`) es verdadera.

### Cómo funciona el si anidado

* Cada nivel de anidamiento crea un nivel más profundo de toma de decisiones. El código evalúa desde la condición más externa hacia dentro.

Ejemplo

* Comprobación de múltiples condiciones con el anidamiento:

```python
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")
```

### Múltiples niveles de anidación

* Puedes anidar tantos niveles como necesites, pero ten en cuenta que demasiados niveles pueden dificultar la lectura del código.

Ejemplo

* Tres niveles de anidación:

```python
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
```

### if anidado frente a operadores lógicos

* A veces, las sentencias if anidadas pueden simplificarse usando operadores lógicos como y. La elección depende de tu lógica.

Ejemplo

Esto anidaba si:

```python
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")
```

Ejemplo

* También podría escribirse con y:

```python
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")
```

* Ambos enfoques producen el mismo resultado. Utiliza sentencias if anidadas cuando la lógica interna sea compleja o dependa de la condición externa. Usar y cuando ambas condiciones son simples e igualmente importantes.

### Más ejemplos

Ejemplo

* Validación de inicio de sesión con comprobaciones anidadas:

```python
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")
```

Ejemplo

* Cálculo de calificaciones con lógica anidada:

```python
score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")
```
