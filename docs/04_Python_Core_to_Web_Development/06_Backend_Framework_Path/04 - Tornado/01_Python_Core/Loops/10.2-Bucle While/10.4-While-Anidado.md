# Learning Python Level 1 - Sesión 10.1 Bucles

## 10.4 Bucle `while` anidado en Python

A diferencia de anidar bucles con `for`, Un bucle `while anidado` en Python consiste en colocar una estructura `while` dentro de otra. El bucle interno se ejecuta completamente en cada iteración del bucle externo, ideal para manejar estructuras de datos bidimensionales (matrices) o generar patrones. Se deben inicializar y actualizar los contadores para evitar bucles infinitos.

## Ejemplo:

```python
i = 1
# Bucle externo
while i <= 3:
    j = 1
    # Bucle interno
    while j <= 2:
        print(f"i:{i}, j:{j}")
        j += 1
    i += 1

# Salida:
# i:1, j:1
# i:1, j:2
# i:2, j:1
# i:2, j:2
# i:3, j:1
# i:3, j:2

```

## Diferencias clave respecto al `for`:

- En `while` debes inicializar los contadores (`i` y `j`) antes de usarlos.

- Es obligatorio incrementar los contadores dentro del bucle, si no, se quedará en un ciclo infinito.

- La lógica es idéntica: un bucle externo para filas y uno interno para columnas.


