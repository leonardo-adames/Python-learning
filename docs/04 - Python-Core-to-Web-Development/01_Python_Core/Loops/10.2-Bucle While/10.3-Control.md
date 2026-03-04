# Learning Python Level 1 - Sesión 10.1 Bucles

## 10.3 Control De Bucle `while` en Python

### CONTROL DE BUCLES EN PYTHON — EXPLICACIÓN PROFESIONAL

En Python existen tres instrucciones que modifican el flujo interno de un bucle:

`break`

`continue`

`pass`

Estas no solo afectan `“cuando imprimir algo”`, sino cómo se ejecuta `internamente el ciclo`, cómo se interrumpe, cómo se salta código, etc.

### 1 break → Detiene el bucle por completo

    Su función es romper el ciclo y salir inmediatamente de él, aunque queden iteraciones pendientes.

    Cómo funciona realmente en memoria

### Cuando Python encuentra un `break`

    Deja de evaluar las siguientes líneas en el bucle.

    Abandona el ciclo.

El programa continúa justo después del bucle.

Ejemplo claro

```python
for num in range(1, 11):
    if num == 5:
        break
    print(num)

# Imprime: 1, 2, 3, 4
# No imprime el 5 ni sigue hasta el 10.
```

### 2 continue → Salta a la siguiente iteración

    Detiene la ejecución solo de la iteración actual, no del bucle completo.

### Python hace lo siguiente al encontrarlo

    Ignora todo el código restante dentro del bucle.

    Vuelve inmediatamente al inicio del ciclo.

```python
#Ejecuta la siguiente vuelta del bucle.

#Ejemplo claro
for num in range(1, 6):
    if num == 3:
        continue
    print(num)


#✔ Imprime: 1, 2, 4, 5
#❌ Se salta el 3.
```

### 3 pass → No hace nada (literal)

No cambia el flujo.

Se usa como “placeholder” para evitar errores de sintaxis cuando la estructura necesita un bloque.

### Ideal para

    Código en construcción

    Bloques vacíos temporales

```python
#Evitar errores mientras se planea la lógica

#Ejemplo claro
for num in range(5):
    pass  # Aquí irá la lógica después


#Python simplemente avanza sin hacer nada.
```
