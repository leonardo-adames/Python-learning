# Operadores de bitwise en Python

<div align="center">

| Operador | Descripción |
|----------|-------------|
| AND (&) | Realiza una operación AND bit a bit |
| OR (|) | Realiza una operación OR bit a bit |
| XOR (^) | Realiza una operación XOR bit a bit |
| Desplazamiento Izquierda (<<) | Desplaza los bits a la izquierda |
| Desplazamiento Derecha (>>) | Desplaza los bits a la derecha |
| Complemento (~) | Devuelve el complemento a uno del número |
</div>

## Operador AND (`&`)
El operador AND (`&`) compara cada bit de dos operandos y devuelve 1 si ambos bits son 1, de lo contrario devuelve 0.

```python
# Ejemplo de operador AND
a = 10  # 1010 en binario
b = 3   # 0011 en binario
resultado = a & b
print(resultado)  # Salida: 2
# Explicación: 1010 & 0011 = 0010 (decimal 2)
```
<br>

## Operador OR (`|`)
El operador OR (`|`) compara cada bit de dos operandos y devuelve 1 si al menos uno de los bits es 1, de lo contrario devuelve 0.

```python
# Ejemplo de operador OR
a = 10  # 1010 en binario
b = 3   # 0011 en binario
resultado = a | b
print(resultado)  # Salida: 11
# Explicación: 1010 | 0011 = 1011 (decimal 11)
```
<br>

## Operador XOR (`^`)
El operador XOR (`^`) compara cada bit de dos operandos y devuelve 1 si los bits son diferentes, de lo contrario devuelve 0.

```python
# Ejemplo de operador XOR
a = 10  # 1010 en binario
b = 3   # 0011 en binario
resultado = a ^ b
print(resultado)  # Salida: 9
# Explicación: 1010 ^ 0011 = 1001 (decimal 9)
```
<br>

## Operador Desplazamiento Izquierda (`<<`)
El operador de desplazamiento izquierda (`<<`) desplaza los bits del operando izquierdo hacia la izquierda por el número de posiciones especificado por el operando derecho.

```python
# Ejemplo de operador de desplazamiento izquierda
a = 10  # 1010 en binario
resultado = a << 1
print(resultado)  # Salida: 20
# Explicación: 1010 << 1 = 10100 (decimal 20)
```
<br>

## Operador Desplazamiento Derecha (`>>`)
El operador de desplazamiento derecha (`>>`) desplaza los bits del operando izquierdo hacia la derecha por el número de posiciones especificado por el operando derecho.

```python
# Ejemplo de operador de desplazamiento derecha
a = 10  # 1010 en binario
resultado = a >> 1
print(resultado)  # Salida: 5
# Explicación: 1010 >> 1 = 0101 (decimal 5)
```

## Operador Complemento (`~`)
El operador de complemento (`~`) devuelve el complemento a uno del número.

```python
# Ejemplo de operador de complemento
a = 10  # 1010 en binario
resultado = ~a
print(resultado)  # Salida: -11
# Explicación: ~1010 = 0101 (decimal -11)
```
