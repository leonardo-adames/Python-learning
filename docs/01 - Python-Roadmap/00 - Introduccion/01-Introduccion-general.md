# Learning Python Level 1 - Sesión 1 Introducción, Configuración e Instalación de Herramientas

<br>

## 1.1 - Introducción general a Python

## **¿Qué es Python?**

**Python** es un lenguaje de programación de alto nivel muy popular. Fue creado por **Guido van Rossum**, y se estrenó en **1991**.

### **Se utiliza para:**

1. *Desarrollo web (lado servidor `BackEnd`)* 
2. *Desarrollo web (lado del cliente `FrontEnd`)* 
3. *Desarrollo de software*
4. *automatización de tareas*
5. *matemáticas*
6. *scripting del sistema*.
7. *Desarrollo de Aplicaciones*
8. *Machine Learning*
9. *Data Science*
10. *Inteligencia Artificial*
11. *Desarrollo de Juegos*

<br>

## **¿Qué puede hacer Python?**

1. **Python** puede usarse en un servidor para crear `aplicaciones web`.

2. **Python** puede usarse junto con otros software para `crear flujos de trabajo`.

3. **Python** puede conectarse a `sistemas de bases de datos`. También puede `leer` y `modificar archivos`.

4. **Python** puede usarse para manejar `big data` y realizar `matemáticas complejas`.

5. **Python** puede usarse para `prototipado` rápido o para `desarrollo de software` listo para producción.
---
<br>

## **¿Por qué aprender Python?**

**Python** funciona en diferentes plataformas **(Windows, Mac, Linux, Raspberry Pi, etc.).**

**Python** tiene una sintaxis sencilla, similar a la del idioma inglés.
Python tiene una sintaxis que permite a los desarrolladores escribir programas con menos líneas que otros lenguajes de programación.

**Python** funciona en un sistema intérprete, lo que significa que el código puede ejecutarse tan pronto como se escribe. Esto significa que el prototipado puede ser muy rápido.
Python puede tratarse de forma procedimenal, orientada a objetos o funcional.

<br>

## **Bueno saberlo**

La versión principal más reciente de Python es *Python 3**, que vamos a utilizar en este tutorial.
En este tutorial, Python se escribirá en un editor de texto. Es posible escribir Python en un Entorno de Desarrollo Integrado, como **Thonny, Pycharm, Netbeans o Eclipse**, que son especialmente útiles para gestionar colecciones más grandes de archivos Python.

**La Sintaxis de Python** comparada con otros lenguajes de programación. **Python** fue diseñado para facilitar la legibilidad y tiene algunas similitudes con el idioma inglés, influenciadas por las matemáticas.

**Python** utiliza nuevas líneas para completar un comando, a diferencia de otros lenguajes de programación que a menudo usan puntos y coma o paréntesis.

**Python** se basa en la **sangría**, utilizando espacios en blanco, para definir el alcance; como el alcance de **bucles, funciones y clases.** Otros lenguajes de programación suelen usar corchetes para este propósito.

**EJEMPLO:**

```python

print("Hello, World!")

#LA SALIDA DEBERÍA SER "Hello, World!"

```
---
<br>

## **INTRODUCCIÓN INFORMAL A ALGUNOS CONCEPTOS BÁSICOS DE PYTHON**

En los siguientes ejemplos, la entrada y la salida se distinguen por la presencia o ausencia de indicaciones **( >>> y … )**: para repetir el ejemplo, debe escribir todo después de la indicación cuando esta aparezca; las líneas que no comiencen con una indicación se imprimen desde el intérprete. Tenga en cuenta que una indicación secundaria en una línea sola en un ejemplo significa que debe escribir una línea en blanco; esto se utiliza para finalizar un comando de varias líneas.

Puede utilizar **el botón “Copiar”** (aparece en la esquina superior derecha cuando pasa el cursor sobre un ejemplo de código o lo toca), que elimina las indicaciones y omite la salida, para copiar y pegar las líneas de entrada en su intérprete.

Muchos de los ejemplos de este manual, incluso los introducidos en el indicador interactivo, incluyen **comentarios**. En Python, los comentarios comienzan con el carácter **almohadilla (#)** y se extienden hasta el final de la línea. Un comentario puede aparecer al principio de una línea o después de un espacio en blanco o código, pero no dentro de una cadena literal. Un carácter almohadilla dentro de una cadena literal es simplemente un carácter almohadilla. Dado que los comentarios sirven para aclarar el código y Python no los interpreta, pueden omitirse al escribir ejemplos.

Algunos ejemplos:

```python
# este es el primer comentario
spam = 1  # y este es el segundo comentario
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```
---
<br>

## **Usar Python como calculadora**

Probemos algunos comandos sencillos de Python. Inicie el intérprete y espere el indicador principal **>>>.** (No debería tardar mucho).

**Números**

El intérprete actúa como una calculadora simple: se escribe una expresión y se escribe el valor. La sintaxis de las expresiones es sencilla: los operadores **+, -, * y /** se pueden usar para realizar operaciones aritméticas; los paréntesis **( ())** se pueden usar para agrupar. 

**Por ejemplo:**

```python
2 + 2

50 - 5*6

(50 - 5*6) / 4

8 / 5  # division always returns a floating-point number
```

Los números enteros **(p. ej. 2, 4, 20)** tienen tipo int, mientras que los que tienen una parte fraccionaria **(p. ej. 5.0, , 1.6)** tienen tipo float. Veremos más sobre los tipos numéricos más adelante en el tutorial.

División **( /)** siempre devuelve un valor de punto flotante. Para realizar una división base y obtener un resultado entero, se puede usar el **//** operador; para calcular el resto, se puede usar **%:**

```python
17 / 3  # classic division returns a float


17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

5 * 3 + 2  # floored quotient * divisor + remainder
```

**Con Python, es posible utilizar el **operador para calcular potencias [ 1 ] :**

```python
5 ** 2  # 5 squared

2 ** 7  # 2 to the power of 7
```
---
<br>

## **Texto**

Python puede manipular texto (representado por tipo str, las llamadas "cadenas"), así como números. Esto incluye caracteres " !", palabras " rabbit", nombres " Paris", oraciones **" ", etc. " ".Se pueden escribir entre comillas simples ( )** o **dobles ( )** con el mismo resultado [ 2 ] Got your back.Yay! **:'...'"..."**

```python
'spam eggs'  # single quotes
'spam eggs'
"Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
'1975'  # digits and numerals enclosed in quotes are also strings
'1975'
```