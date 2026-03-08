# Learn Python Levev 1 - Sesión 4 Tipos De Datos

## 4.1 Tipos de Datos en Python

En Python, los `tipos de datos` son fundamentales para almacenar y manipular información. Son los elementos que permiten almacenar datos de diferentes tipos, estos se podrían consideerar como `contenedores de datos` los cuales pueden usarse de muchas formas distintas.

### Tipos de Dato Integrados

En programación, el tipo de datos es un concepto importante.

Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer diferentes cosas.

Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorías:

TIPOS DADATOS EN PYTHON

```python
+-----------------------+-----------------------------+
|Categoría              |Tipos en Python              |
+-----------------------+-----------------------------+
|Tipo de texto          |str                          |
|Tipos numéricos        |int, float,complex           |
|Tipos de secuencia     |list, tuple,range            |
|Tipo de mapeo          |dict                         |
|Tipos de conjuntos     |set,frozenset                |
|Tipo booleano          |bool                         |
|Tipos binarios         |bytes, bytearray,memoryview  |
|Ninguno Tipo           |NoneType                     |
+-----------------------+-----------------------------+
```

**DESDE AQUÍ PODEMOS CLASIFICAR ESTA TABLA EN DOS GRUPOS:**

* **`Tipos De Datos Simples`**

* **`Tipos De Datos compuestos`**

---

<br>

## **Tipos de datos simples**

### **¿Qué son los datos simples en Python?**

Los `datos simples` (también llamados `tipos de datos básicos` o `primitivos`)<br>
son valores individuales que no están formados por otros datos internos.<br>
Son unidades básicas de información que Python usa para representar valores simples como números,
textos o valores lógicos.

No se dividen en partes más pequeñas dentro del lenguaje.

Principales datos simples en Python:

```python
 _____________________________________________________________
|Nombre                 Palabra reservada        Sintaxis     |
|-------------------------------------------------------------|
|Entero                 |int                      |0          |
|Flotante               |float                    |3.14       |
|Cadena de texto        |str                      |"Hola"     |
|Booleano               |bool                     |True/False |
|Complejo               |complex                  |1 + 2j     |
|Byte                   |bytes                    |b"Hola"    |
|Nulo                   |NoneType                 |None       |
|_______________________|_________________________|___________|
```

### 1. Enteros → int

**Representan:**

* números sin decimales.

* Positivos o Negativos.

* Longitud Ilimitada.

* Se puede usar el guión bajo (`_`) para leer mejor los miles.

### Ejemplo 1

```python
x = 10        # entero positivo
y = -10        # entero negativo
z = 1588714696552985    # entero con cat. ilimidada de elementos
a =20_000_000           # entero conguiones bajos para leer mejor los miles y millones.
b = 20000000            # entero sin guiones bajos, se lee menos laro que con guiones bajos.

# salida de datos

print("x = ", x)    # Wil be 10
print("y = ", y)    # Wil be -10
print("z = ", z)    # Wil be 1588714696552985
print("a = ", a)    # Wil be 20_000_000
print("b = ", b)    # Wil be 20000000
```
---

### 2. Números de punto Decimales o flotante → float

**Representan:**

* números con decimales o valores reales.

* Positivos o Negativos.

* Longitud Ilimitada.

### Ejemplo 2

```python
# Números Decimales
pi = 3.14
x = 1.11111
y = 1.0394030
z = -35.523333333330000000 # esto es igual a -35.52

print("pi =", pi)   # Wil be 3.14
print("x =", x)     # Wil be 1.11111
print("y =", y)     # Wil be 1.0394030 
print("z =", z)     # Wil be -35.52333333333
```
* **Podemos utilizar una especie de conversión para representar cualquier `número real`, Se usa para `longitud`, `peso`, `frecuencia`, ... donde `3.3`y `3.3000003` son iguales.**

```python

#Representación aproximada de números reales
real = 3.300000000003  

 # 3.30 - muestra 2 cifras dedcimales
print(f'{real:.2f}') 

# <num-decimales>
```
---

### 3. Cadenas de texto → str

Representan secuencias de caracteres, como palabras, frases o símbolos.
Aunque internamente son secuencias, Python las trata como datos simples al usarlas como valores indivisibles.

### Ejemplo 3

```python
nombre = "Leo"
print("nombre =", nombre)
```
---

### 4. Booleanos → bool

Representan valores lógicos:

* True
* False
Se usan en condiciones, comparaciones y lógica.

### Ejemplo 4

```python
es_mayor = True
es_menor = False

print("es_mayor =", es_mayor)  # Wil be True
print("es_menor =", es_menor)  # Wil be False
```
---

### 5. Numeros complejos → complex

Representan números de la forma:
`𝑎 + 𝑏𝑗`

donde:

`a` = parte real<br>
`b` = parte imaginaria<br>
`j` = unidad imaginaria (Python usa j, NO i)

* Podemos acceder individualmente a las dos partes.
    * Número Real => `real`.
    * Número Imaginario => `imag`.

* Teniendo en cuenta este Número: `x = 3 + 5j`
    * A. x.real = 3
    * B. x.imag = 5

* Podemos acceder al valor real y al imaginario por separado:

###  Ejemplo

```python
print("Real: " + str(x.real) + " / Imagunary: " + str(x.imag))
```

### EJEMPLO 5

```python
z = 3 + 4j
print("z.real =", z.real)   # 3.0
print("z.imag =", z.imag)   # 4.0
#UNIDAD IMAGINARIA
```
---

### 6. Bytes → bytes

**Representan una secuencia de valores enteros entre `0` y `255`, usados para:**

**manejar datos binarios**

* *imágenes*

* *archivos*

* *redes*

* *comunicaciones*

* *codificaciones*

### Ejemplo 6

```python
b = bytes([65, 66, 67])
print("b = bytes =", b)        # b'ABC'
#
```
---

### 7. None → NoneType

Representa la ausencia de valor o un valor nulo. este tipo de dato es util para inicializar variables que no tienen un valor asignado y que se podrían usar despues.

### Ejemplo 7

```python
dato = None
print("dato =", None)
#valor nulo o vacio
```
