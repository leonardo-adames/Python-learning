# Learning Python Level 1 - Sesión 10.1 Bucles

## 10.1.2 - Bucles for anidados

El `anidado de bucles` en Python consiste en colocar un bucle dentro de otro, lo que permite iterar sobre estructuras de datos complejas como matrices o listas dentro de listas. En el bucle `for` el `anidado de bucles`funciona de la siguiente manera: 

- El bucle interno se ejecuta completamente por cada iteración del bucle externo.
- Se utiliza comúnmente para patrones, tablas de multiplicar y manipulación de datos multidimensionales. 

**EJEMPLO:**

```python
# Iterar sobre filas y columnas
for i in range(1, 4):  # Bucle externo
    for j in range(1, 4):  # Bucle interno
        print(f"({i}, {j})", end=" ")
    print()  # Salto de línea después de cada fila

```
Explicación del ejemplo:

- El bucle externo itera sobre las filas (1, 2, 3).
- El bucle interno itera sobre las columnas (1, 2, 3) para cada fila.
- El resultado es una tabla de coordenadas (fila, columna).

## Características Clave

- El bucle interno se reinicia en cada iteración del bucle externo.
- Estructura: Se requiere el uso de sangría (indented) para definir el alcance de cada bucle.
- Complejidad: El número total de iteraciones es el producto de las iteraciones de ambos bucles `(\(N\times M\))`.
- Control: Se puede usar break para salir del bucle interno, lo que solo afecta al ciclo más interno. 

## Casos de Uso Comunes

Matrices: Recorrer una lista de listas `(matriz[i][j])`.
Generación de Patrones: Crear formas, formas geométricas o tablas.
Comparación: Comparar elementos de dos listas diferentes. 
<!--Este video explica la sintaxis y el uso de los bucles anidados en Python:-->
<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->

## Consejo: 

Tenga cuidado con la `legibilidad` y el `rendimiento` si anida demasiados bucles, ya que esto puede disminuir la velocidad del programa. 