# Learn  Python Level 1 - SESIÓN 3

## 1. LAS VARIABLES Y LAS CONSTANTES

### **¿Qué es una variable?**

Una variable es un espacio en la memoria de la computadora que se utiliza para almacenar datos que pueden cambiar durante la ejecución de un programa. En Python, las variables se crean al asignarles un valor utilizando el operador de asignación `=`.

<br>

### **¿Cómo se crean las variables en Python?**

Para crear una variable en Python, simplemente debes elegir un nombre para la variable y asignarle un valor. Aquí tienes algunos ejemplos:

*Para crear una variable en python, debemos de realizarlo de la siguiente manera:*

**Sintaxis de creación de una Variable:**

```python
# VARIABLE         VALOR A ASIGNAR
nombre_variable = 'valor_a_asignar'
```
    SIEMPRE USANDO `lower_snake_case` PARA VARIABLES.

**Aquí tienes algunos ejemplos de cómo definir Variableses en Python:**

```python
# Variable

nombre_alumno = "Juan Pérez"   # (nombre_alumno) es una variable, ("Juan Pérez") es el valor a asignado
print(nombre_alumno)           # Salida: Juan Pérez
```

**NOTA IMPORTANTE:**

* **Las Variables en Python primero se declaran y luego se definen.**
* **Las variables en Python no requieren una declaración explícita de tipo de dato; el tipo de datos es determinado automáticamente por el interprete según el valor asignado.**
* **Las variables en Python pueden cambiar de tipo de dato durante la ejecución del programa.**

---

### **Reglas para nombrar variables**

**Al nombrar variables en Python, debes seguir estas reglas:**

1. **Los nombres de las variables** deben comenzar con una letra (`a-z, A-Z`) o un guion bajo (`_`).
2. **Los nombres de las variables** pueden contener letras, números y guiones bajos, pero no pueden contener espacios ni caracteres especiales.
3. **Los nombres de las variables** son sensibles a mayúsculas y minúsculas (por ejemplo, `edad` y `Edad` son variables diferentes).
4. No puedes usar palabras reservadas de Python como n**ombres de variables** (por ejemplo, **`if`, `while`, `for`**,** etc.).

---
<br>
<br>

### **¿QUÉ SON LAS CONSTANTES?**

Las `constantes` en **Python** son valores que no deberían cambiar durante la ejecución de un programa, aunque técnicamente **Python no tiene una sintaxis específica para declarar constantes** como otros lenguajes, sto está documentado formalmente en el `manua de estilo PEP 8`, el manual de estilo oficial de Python. En su lugar, se sigue una `convención de nomenclatura` para indicar que un v**alor debe tratarse como inmutable**. 

Esto significa que **Python no bloquea la modificación**, pero ésta convención indica que una variable debe tratarse como constante por el programador. Las `constantes` suelen **definirse a `nivel de módulo` y escribirse en `mayúsculas` con `guiones bajos**`.

<br>

### **¿Cómo se crean las CONSTANTES en Python?**

*Para crear una variable/constante en python, debemos de realizarlo de la siguiente manera:*

**Sintaxis de creación de una CONSTANTES:**

```python
# CONSTANTE         VALOR A ASIGNAR
NOMBRE_CONSTANTE = 'valor_a_asignar'
```
    SIEMPRE USANDO `UPPER_SNAKE_CASE` PARA CONSTANTES.

---

**Aquí tienes algunos ejemplos de cómo definir CONSTANTES en Python:**

```python
# Definición de constantes
PI = 3.14159
GRAVEDAD = 9.81
VELOCIDAD_LUZ = 299792458
```

**En este ejemplo anterior se muestran algunas `constantes` comunes utilizadas en `física`. siempre que un programador vea una variable en mayusculas sabra que es una constante y que corresponden a una parte del código que no debe ser modificada.**

**FUENTE VERIFICABLE:**

[PEP 8 – Style Guide for Python Code, sección Naming Conventions](https://peps.python.org/pep-0008/)

---
<br>

### **Convención oficial: usar MAYÚSCULAS**

Para declarar una constante, Python usa una convención, no una restricción:

* Se escriben en `MAYÚSCULAS`.

* Opcionalmente se separan con guiones bajos.

* Se ubican a nivel de módulo (`fuera de funciones y clases`).

* Tú como programador te comprometes a no modificarla, pero Python no lo impide.

Ejemplo demostrando que sí pueden modificarse, Esto muestra que Python no obliga, solo recomienda:

```python
PI = 3.14159
PI = 20   # Python lo permite, aunque está mal visto

```

Archivo config.py:

```python
API_KEY = "123ABC"
TIMEOUT = 30
DEBUG_MODE = False

```

Archivo main.py:

```python
from config import TIMEOUT, DEBUG_MODE

print(TIMEOUT)

```
---

<br>

### **Reglas para nombrar Constantes**

Las constantes son valores que no cambian durante la ejecución de un programa. En Python, no hay una sintaxis especial para definir constantes, pero por convención, se utilizan nombres en mayúsculas para indicar que una variable debe ser tratada como una constante y tu como buen programador te comprometes a no modificarlas y trabajar implementandolas buenas practicas y conveniencias universales de la industiria. Aquí tienes algunas reglas para nombrar constantes:

1. **Los nombres de las constantes** deben estar en mayúsculas (por ejemplo, `PI`, `GRAVEDAD`).
2. **Los nombres de las constantes** pueden contener letras, números y guiones bajos, pero no pueden contener espacios ni caracteres especiales.
3. Al igual que con las variables, **los nombres de las constantes** son sensibles a mayúsculas y minúsculas.
4. No puedes usar palabras reservadas de Python como **nombres de constantes**.
5. Es recomendable usar nombres descriptivos para las constantes, de modo que sea fácil entender su propósito en el código.

<br>

### ¿Existen formas de simular constantes reales?

**Sí, pero no son recomendadas para casos simples.** <br>
Existen formas de simular constantes reales en Python, aunque no son recomendadas para casos simples debido a la complejidad adicional que pueden introducir. Aquí hay algunos ejemplos de cómo se podrían simular constantes reales:

**1. Usar una clase con propiedades de solo lectura**

```python
class Constantes:
    @property
    def PI(self):
        return 3.14159

C = Constantes()
print(C.PI)

```
**QUE ESTÁ PASANDO AQUÍ:**<br>
* Se define una clase `Constantes` con una propiedad de solo lectura llamada `PI`.
* La propiedad `PI` devuelve el valor de la constante cuando se accede a ella.
* Intentar modificar `C.PI` resultará en un error, ya que es una propiedad de solo lectura.

**Intentar cambiar C.PI = 10 produce error, para lograrlo se debe usar `typing.Final`, esto solo es posible a partir de `Python 3.8+`** [Fuente: Documentado en PEP 591](=https://peps.python.org/pep-0591/) <br>

**Ej DE USO DE `typing.Final`**

```python
from typing import Final

PI: Final = 3.14159

#No lo bloquea en tiempo de ejecución, 
#pero los linters y herramientas de análisis estático pueden advertir sobre modificaciones.
```
**Esto simula una constante real, pero es más complicado que simplemente usar una variable con mayúsculas.**

<br>

**RECOMENDACIÓN PARA AMBOS CASOS:**

* Siempre es recomendable utilizar `nombres descriptivos` para **variables** y **constantes**, de modo que sea fácil entender su propósito en el código. tambien es reomendable usar el formato de "`snake_case`" para v** ariables y para constantes**, donde las palabras se separan con guiones bajos (por ejemplo, `mi_variable`, `MI_CONSTANTE`).

* Siempre que la variable o constante almacene un valor relacionado con una unidad de medida, es recomendable incluir la unidad en el nombre para mayor claridad (por ejemplo, `altura_metros`, `VELOCIDAD_KMH`).

---
<br>
<br>

### **¿Qué trabajaremos en los ficheros practica?**

1. **Creación de `variables` y `constantes`**.

2. **Asignación de `nombres` y `valores` a `variables` y `onstantes`**.

>- **Reglas y convenciones** para nombrar **variables y constantes**.<br>
>- Nombres de v**ariables y constantes** válidos e inválidos.

3. **signación múltiple de valores.**

4. **Mostrar de salida de las `variables` y `constantes` en consola**.

5. **Introducir información por telado y almacenarlo**.

>- Concatenación texto con una variable.
>- Concatenación deuna variable con otra.

6. **Variables globales**.

---

# Resumen Raçápido (verificable)

>- Python no tiene constantes reales → confirmado por PEP 8.
>- La convención es escribirlas en mayúsculas.
>- Se colocan a nivel de módulo.
>- Python sí permite modificarlas, aunque va contra la convención.
>- Para mayor seguridad existen typing.Final y clases con propiedades de solo lectura.

### Y RECUERDA: ¡Las buenas prácticas de nomenclatura hacen que tu código sea más legible y mantenible!
