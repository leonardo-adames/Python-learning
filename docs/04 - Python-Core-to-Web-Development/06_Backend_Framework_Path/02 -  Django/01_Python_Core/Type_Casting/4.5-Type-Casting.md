# BootCamp Python Sesión 4 - Tipos De Datos

## 4.5 Type Casting & Funciones constructoras en Python

## Conversión Explicita

En `python` Puede haber ocasiones en las que quieras especificar un tipo en una variable. Esto se puede hacer con el lanzamiento. Python es un lenguaje orientado a objetos y, como tal, utiliza clases para definir tipos de datos, incluidos sus tipos primitivos.

Por tanto, el casting en python se le conoce como  `Conversión Explicita`, y  realiza usando funciones constructoras:

* **int()** - construye un número entero a partir de un literal entero, un literal flotante (eliminando todos decimales), o un literal de cadena (siempre que la cadena represente un número entero)

* **float()**- construye un número float a partir de un literal entero, un literal float o un literal de cadena (siempre que la cadena represente un float o un entero)

* **Str()** - construye una cadena a partir de una gran variedad de tipos de datos, incluyendo cadenas, literales enteros y literales float.

## CONVERSIÓN DEMANERA MANUAL

### Ejemplo

Enteros:

```python
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
```

Decimales:

```python
Carrozas:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
```

### Ejemplo

string:

```python
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```

## EXISTEN MAS FUNCIONES CONSTRUCTORAS PARA LOS DEMAS TIPOS DE DATOS TANTO PARA LOS SIMPLES COMO TAMBIÉN PARA LOS COMPUESTOS, GRACIAS A ESO PODEMOS ESPESIFICAR EL TIPO DE DATOS AL ASIGNAR UN VALOR, CON SU CONSTRUCTOR

### Ejemplo

**ESPESIFICACIÓN DE TIPOS DE DATOS AL ASIGNARLOS, CON SU CONSTRUCTOR:**

```python
#Sintaxis de declaración
a = complex(23 + 5j)                    #complex--> numero complejo
b = list(["python", "java", "C#"])      #list-->lista
c = tuple(("python", "java", "C#"))     #tuple--> tuple
d = range(8)                            #range--> rango
e = dict(name= "python", hours= 3)      #dict--> diccionario
f = set(("python", "java", "C#"))       #set--> conjunto
g = bool(5)                             #bool--> booleano
h = float("4.2")                        #float--> decimal
i = int(21)                             #int--> entero
j = str("Hola Leonardo")                #str--> cuerda o texto

#Sintaxis de Salida
print(type(a))              # salida--> <class 'complex'>
print(type(b))              # salida--> <class 'list'>
print(type(c))              # salida--> <class 'tuple'>
print(type(d))              # salida--> <class 'range'>
print(type(e))              # salida--> <class 'dict'>
print(type(f))              # salida--> <class 'set'>
print(type(g))              # salida--> <class 'boll'>
print(type(h))              # salida--> <class 'float'>
print(type(i))              # salida--> <class 'int'>
print(type(j))              # salida--> <class 'str'>
```

## Type Casting (Conversión Implicita)

Es el proceso de convertir un tipo de dato en otro.
Lo conocemos como `Type Casting`
Tenemos dos tipos los ciales son `Explicita` e `Implicita`, ya vimos la `Explicita`:

* **Inplicita:**
es la transformación automática de un tipo de dato a otro por el intérprete, sin intervención del programador, para evitar pérdida de información en operaciones entre tipos compatibles, como sumar un `int` y un `float`, donde el int se convierte a float para mantener la `precisión decimal` del resultado. Python eleva el tipo de dato a uno "superior" (como `float`) para asegurar que no se pierdan datos.

### Ejemplos

**CONVERSIÓN DE int / float**

```python
num_int = 5
num_flo =4.5
num_new = num_int + num_flo
print('type of num_int is : ', type(num_int))
print('type of num_flo is : ', type(num_flo))
print('value of num_new is : ', num_new)
print('type of num_new is : '. type(num_new))

# Python convierte x (5) a 5.0 y luego suma 5.0 + 4.5 = 9.5.
```

### ¿Cómo funciona?

Combinación de tipos compatibles: Ocurre al realizar operaciones aritméticas, comparaciones, etc., entre tipos de datos que Python puede fusionar sin problemas (ej. `int, float, complex`).
Evita pérdida de datos: Python siempre elige el tipo que puede contener toda la información. Por ejemplo, int (`entero`) puede ser contenido en float (`decimal`), pero no al revés, por lo que convierte el entero a flotante.

### Ejemplos

**CONVERSIÓN DE int / complex**

```python
num_int = 123
num_complex = 1.23 + 45j
num_new = num_int + num_complex
print('type of num_int is : ', type(num_int))
print('type of num_complex is : ', type(num_complex))
print('value of num_new is : ', num_new)
print('type of num_new is : ', type(num_new))
```

### Ejemplos

**CONVERSIÓN DE int / bool**

```python
value_bool = true
num_int =21
num_new = value_bool + num_int
print('type of num_int is : ', type(num_int))
print('type of value_bool is : ', type(value_bool))
print('value of num_new is : ', num_new)
print('type of num_new is : ', type(num_new))
```
### Ejemplos

**CONVERSIÓN DE int / str**

```python
num_int = 123
num_str = '456'
num_new = num_int + num_str
print('type of num_int is : ', type(num_int))
print('type of num_str is : ', type(num_str))
print('value of num_new is : ', num_new)
print('type of num_new is : ', type(num_new))
```

### Ejemplos

**División de enteros:**

```python
a = 10 # int
b = 3 # int
division = a / b
print(f"{division} es de tipo {type(division)}") # Salida: 3.333... es de tipo <class 'float'>

#Incluso si ambos son enteros, la división / siempre produce un float para no perder la parte decimal.
```

## Cuándo NO ocurre (y se necesita conversión explícita)

Cuando los tipos son incompatibles, como intentar sumar una cadena (`str`) con un número digace (`int`, `float` o `complex`), en cualquiera de los casos ya Python no puede hacerlo automáticamente y arrojará un `TypeError`, y es aquí donde entra en acción la `Conversión Explicita`.

```python
print("Hola" + 5)   # Esto causaría un error
```

En estos casos, debes usar la conversión explícita, por ejemplo:

```python
print("Hola" + str(5))
```

O

```python
print(5 + int("5"))
```

Resultado

```python
"Hola 5"
```