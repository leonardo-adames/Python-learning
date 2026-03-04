# Learning Python Level 1 - Sesión 10.1 Bucles

## 10.1.1 - Bucles `for` en Python

### ¿Qué son los Bucles?

Un `bucle` en Programación es una `estructura iterativa` que permite `repetir` un `bloque de código` varias veces como sea necesario `mientras se cumpla una condición` o `mientras haya elementos que recorrer`.

Los `Bucles` son escenciales para: 

    ✔️ 1. Automatizar tareas repetitivas
    Ejemplo: mostrar números del 1 al 100 sin escribir 100 líneas.

    ✔️ 2. Recorrer estructuras de datos
    Ejemplo: ir elemento por elemento en una lista, tupla, string, dataframe, etc.

    ✔️ 3. Procesar datos de forma eficiente
    Ejemplo: limpiar datos, filtrar elementos, sumar valores.

    ✔️ 4. Construir algoritmos
    Ejemplo: búsqueda, ordenamiento, cálculos matemáticos paso a paso.

    ✔️ 5. Interactuar con el usuario hasta que cumpla un requisito
    Ejemplo: seguir pidiendo una entrada válida.

Existen Dos Tipos De Bucles: el bucle `for` & el bucle `While`, acontinuación, veremos ests dos estructuras iterativas dentro del lenguaje de `Python`

### Bucle `for`

EL bucle `for`en **Python** sirve para iterar sobre una secuencia ya sean: `listas`, `cadenas`, `rangos`, `tuplas`, `diccionarioa`, **etc**. En otras palabraas recorre elemento por elemento hasta terminar.

### EJEMPLO

Iterando sobre secuencia con `for`:

```python
print("SALIDA:")
print("\n")
for numero in range(1, 6):
    print(numero)
    #SALIDA:
#1
#2
#3
#4
#5
#EL 6 SE NO SEALE YA QUE PYTHON SIEMPE EXLUYES EL LIMITE DERECHO  EN TODA EJECUCIÓN

```

Recuerden que el bucle `"for"` solo se usa para recorrer secuensias ya establecidad dentro de estructuras de datos como:

    listas

    tuplas

    diccionarios

    conjuntos

    rangos

    Strings

### ¿Cuándo uso bucles for?

Los bucles for se utilizan cuando se tiene un bloque de código que se desea repetir un número fijo de veces . El bucle for siempre se usa junto con un objeto iterable , como una lista o un rango. La instrucción `for` de Python itera sobre los miembros de una secuencia en orden, ejecutando el bloque cada vez,

### EJEMPLO

Bucle for del 0 al 2, por lo tanto se ejecuta 3 veces

```PYTHON

for x in range (3):
    print("Llegamos a tiempo")
    print(x)

#para x en el rango (0, 3):
    #print("Llegamos a tiempo %d" % (x))
```

| Tipo de bucle | ¿Qué hace?                                  | ¿Cuándo usarlo?                            |
| ------------- | ------------------------------------------- | ------------------------------------------ |
| `for`         | Recorre elementos de una secuencia          | Cuando ya sabes qué vas a recorrer         |
| `while`       | Repite mientras una condición sea verdadera | Cuando no sabes cuántas repeticiones habrá |

___

**Verificación del contenido**

La descripción de fory whilecoincide con el documento. Fuente De Documentación de Python 3: Flujo de control

https://docs.python.org/3/tutorial/controlflow
