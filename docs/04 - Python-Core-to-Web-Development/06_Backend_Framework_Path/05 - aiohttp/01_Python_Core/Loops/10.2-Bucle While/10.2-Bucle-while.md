# Learning Python Level 1 - Sesión 10.1 Bucles

## 10.2 Bucle `while` en Python

EL bucle `while` repite un bloque de código mientras una condición se verdadera. La cantidad
de repeticiones no está definida de antemano.

### EJEMPLO:

```PYTHON
contador = 1

while contador <= 3:
    print(contador)
    contador += 1
```

### ¿Cuándo usar el bucle `while`?

Úsalo cuando:

    No sabes cuantas veces se repetirá el ciclo.

    La repetición depende de la (condición lógica) que puede cambiar durante la ejecución

    Necesitas esperar a que algo ocurra (entrada del suario, un estado, un valor que cambie)
