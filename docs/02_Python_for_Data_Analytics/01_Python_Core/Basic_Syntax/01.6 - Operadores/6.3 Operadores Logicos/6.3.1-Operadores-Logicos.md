# Learning Python Level 1 - Seccion 06 Operadores

## 06.3 Operadores lógicos

<div align="center">

| Operador | Nombre | Descripción |
|----------|--------|-------------|
| and | Y lógico | Retorna True si ambos operandos son True |
| or | O lógico | Retorna True si al menos uno de los operandos es True |
| not | No lógico | Retorna True si el operando es False |

</div>

<br>
<br>

## Lista de operadores lógicos

### Operador and
El operador and se utiliza para combinar dos condiciones, y la expresión resultante será True solo si ambas condiciones son True.

```python

a = 5
b = 10
c = 15

resultado = (a < b) and (b < c)  # True, ya que ambas condiciones son True
```

### Operador or
El operador or se utiliza para combinar dos condiciones, y la expresión resultante será True si al menos una de las condiciones es True.

```python

a = 5
b = 10
c = 3

resultado = (a > b) or (b < c)  # False, ya que ninguna de las condiciones es True
```

### Operador not
El operador not se utiliza para negar una condición, y la expresión resultante será True si la condición es False.

```python

verdadero = True
falso = not verdadero  # falso es False

numero = 5
es_mayor_a_10 = numero > 10
no_es_mayor_a_10 = not es_mayor_a_10
```

## Ejemplos de uso

### Combinación con and

```python
edad = 25
tiene_licencia = True

puede_conducir = (edad >= 18) and tiene_licencia  # True
```

### Combinación con or

```python
tiene_dinero = False
tiene_tarjeta = True

puede_comprar = tiene_dinero or tiene_tarjeta  # True
```

### Negación con not

```python
es_verdadero = True
es_falso = not es_verdadero  # False

numero = 5
es_menor_a_10 = numero < 10
no_es_menor_a_10 = not es_menor_a_10  # False
```
<br>
<br>

## Combinación de operadores lógicos
Es posible combinar varios operadores lógicos en una sola expresión para crear condiciones más complejas.

```python
numero = 15

es_multiplo_de_3 = (numero % 3 == 0)
es_multiplo_de_5 = (numero % 5 == 0)

es_multiplo_de_3_o_5 = es_multiplo_de_3 or es_multiplo_de_5  # True, ya que 15 es múltiplo de 3
es_multiplo_de_3_y_5 = es_multiplo_de_3 and es_multiplo_de_5  # False, ya que 15 no es múltiplo de 3 y 5 simultáneamente
no_es_multiplo_de_3 = not es_multiplo_de_3  # False
```

## Precedencia de operadores lógicos
Cuando se combinan múltiples operadores lógicos en una expresión, es importante entender su precedencia para evaluar correctamente la expresión.

La precedencia de operadores lógicos en Python sigue este orden:

1. **not**
2. **and**
3. **or**

Por lo tanto, en una expresión con `and` y `or`, `and` se evalúa antes que `or`.

> **Sin embargo, no conviene abusar de esto a la hora de escribir nuestro código. No os importa usar paréntesis si mejora la legibilidad.**
