<div align="center">
    <kbd><h1><b>CURSO DE PYTHON</b><br>SINTAXIS BÁSICA</b></h1></kbd>
        <img width="2064" height="100%" alt="Image" src="../../../../notes/resources/INTRO/Py_welcome9.png" altº="Image" width="100%"/>
    <br>
    <br>
    <h2><kbd>CONCATENACIÓN DE STRING</kbd></h2>
</div>

<br>

Estas prácticas provienen principalmente de la documentación oficial de Python y del PEP 8, que es el estándar de estilo del lenguaje.

📌 Fuente principal

PEP 8 – Style Guide for Python Code (Python Software Foundation) [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## **RESUMEN BREVE SOBRE EL OBJETIVO DEL MANUAL**

| Área           | Regla clave               |
| -------------- | ------------------------- |
| Python         | Legibilidad > complejidad |
| PEP 8          | Estilo consistente        |
| Visualización  | Claridad > estética       |
| Código gráfico | Reproducible y limpio     |
| Ética          | No engañar con gráficos   |

---
<br>

# **PEP 8 – Guía de estilo para código Python**

<div align="center">
    <h2><b>Autor:</b></h2>
    <a href="https://gvanrossum.github.io/"><b>Guido van Rossum</b></a>
     <br>
    <a href="https://barry.warsaw.us/"><b>Barry Warsaw</b></a>
     <br>
    <a href="https://ncoghlan.github.io/"><b>Alyssa Coghlan</b></a>
    <br>
    <h3>ESTADO: <b>Activo</b></h3>
    <h3>TIPO: <b>Proceso</b></h3>
    <h3>CREADO: <b>05-Jul-2001</b></h3>
    <h3>POST-HISTORIA: <b>05-Jul-2001, 01-Ago-2013</b></h3>
</div>

---

<br>

## Introducción

Este documento describe las convenciones de codificación para el código Python que compone la biblioteca estándar de la distribución principal de Python. Consulte el documento informativo complementario PEP, que describe las pautas de estilo para el código C en la implementación de Python en C.

Este documento y PEP 257 (Convenciones de cadenas de documentación) fueron adaptados del ensayo original de la Guía de estilo de Python de Guido, con algunas adiciones de la guía de estilo de Barry [2] .

Esta guía de estilo evoluciona con el tiempo a medida que se identifican convenciones adicionales y las convenciones pasadas quedan obsoletas debido a cambios en el lenguaje mismo.

Muchos proyectos tienen sus propias pautas de estilo de codificación. En caso de conflicto, dichas guías específicas prevalecen.


<br>

## Una consistencia tonta es el duende de las mentes pequeñas

Una de las ideas clave de Guido es que el código se lee con mucha más frecuencia de la que se escribe. Las directrices que se proporcionan aquí buscan mejorar la legibilidad del código y hacerlo consistente en todo el espectro del código Python. Como dice PEP 20 , «La legibilidad cuenta».

Una guía de estilo se centra en la coherencia. La coherencia con esta guía de estilo es importante. La coherencia dentro de un proyecto es aún más importante. La coherencia dentro de un módulo o función es la más importante.

Sin embargo, sepa cuándo ser inconsistente: a veces las recomendaciones de la guía de estilo simplemente no son aplicables. En caso de duda, use su criterio. Observe otros ejemplos y decida qué se ve mejor. ¡Y no dude en preguntar!

En particular: ¡no rompa la compatibilidad con versiones anteriores solo para cumplir con este PEP!

Algunas otras buenas razones para ignorar una determinada directriz:

Al aplicar la directriz el código sería menos legible, incluso para alguien que está acostumbrado a leer código que sigue esta PEP.
Para ser coherente con el código circundante que también lo rompe (quizás por razones históricas), aunque esta también es una oportunidad para limpiar el desastre de otros (al más puro estilo XP).
Porque el código en cuestión es anterior a la introducción de la directriz y no hay ninguna otra razón para modificar ese código.
Cuando el código necesita seguir siendo compatible con versiones anteriores de Python que no admiten la función recomendada por la guía de estilo.


## Diseño del código

### Sangría

Utilice 4 espacios por nivel de sangría.

Las líneas de continuación deben alinear los elementos ajustados verticalmente mediante la unión de líneas implícita de Python entre paréntesis, corchetes y llaves, o mediante una sangría francesa. Al usar una sangría francesa, se debe tener en cuenta lo siguiente: no debe haber argumentos en la primera línea y se debe usar una sangría posterior para distinguirse claramente como una línea de continuación:

### correcto:

```python

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

### Incorrecto:

```python

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

La regla de los 4 espacios es opcional para las líneas de continuación.

Opcional:

```python
# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```

Cuando la parte condicional de una `if` sentencia - es lo suficientemente larga como para requerir que se escriba en varias líneas, cabe destacar que la combinación de una palabra clave de dos caracteres (p. ej., if), un espacio y un paréntesis de apertura crea una sangría natural de 4 espacios para las líneas subsiguientes de la sentencia condicional multilínea. Esto puede generar un conflicto visual con el conjunto de código sangrado dentro de la `if` sentencia -, que también estaría sangrado naturalmente a 4 espacios. Esta PEP no establece una postura explícita sobre cómo (o si) se deben distinguir visualmente dichas líneas condicionales del conjunto anidado dentro de la `if` sentencia -. Las opciones aceptables en esta situación incluyen, entre otras:

```python
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

(Vea también la discusión sobre si se debe romper antes o después de los operadores binarios a continuación).

La llave/corchete/paréntesis de cierre en construcciones multilínea pueden alinearse debajo del primer carácter que no sea un espacio en blanco de la última línea de la lista, como en:

 ```python
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
 ```
o puede alinearse debajo del primer carácter de la línea que inicia la construcción multilínea, como en:

 ```python
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
 ```

 <br>

## ¿Tabulaciones o espacios?

Los espacios son el método de sangría preferido.

Las tabulaciones deben usarse únicamente para mantener la coherencia con el código que ya está sangrado con tabulaciones.

Python no permite mezclar tabulaciones y espacios para la sangría.

<br>

## Longitud máxima de línea

`Limite` todas las `líneas` a un máximo de `79 caracteres`.

Para bloques de texto largos y fluidos con menos restricciones estructurales (`docstrings` o `comentarios`), la longitud de línea debe limitarse a `72 caracteres`.

Limitar el ancho requerido de la ventana del editor permite tener varios archivos abiertos uno al lado del otro y funciona bien cuando se utilizan herramientas de revisión de código que presentan las dos versiones en columnas adyacentes.

El ajuste de línea predeterminado en la mayoría de las herramientas altera la estructura visual del código, lo que dificulta su comprensión. Estos límites se eligen para evitar el ajuste en editores con un ancho de ventana de 80, incluso si la herramienta coloca un glifo de marcador en la última columna al ajustar las líneas. Algunas herramientas web podrían no ofrecer ajuste de línea dinámico.

Algunos equipos prefieren una longitud de línea mayor. Para el código mantenido exclusiva o principalmente por un equipo que pueda llegar a un acuerdo sobre este tema, se puede aumentar el límite de longitud de línea hasta 99 caracteres, siempre que los comentarios y las cadenas de documentación se mantengan en 72 caracteres.

La biblioteca estándar de Python es conservadora y requiere limitar las líneas a `79 caracteres` maximo y las (`cadenas de documentación`& `comentarios` a `72 caracteres maximo`).

La forma preferida de cerrar líneas largas es usar la continuación de línea implícita de Python entre paréntesis, corchetes y llaves. Las líneas largas se pueden dividir en varias líneas cerrando expresiones entre paréntesis. Se recomienda usar estos paréntesis en lugar de una barra invertida para la continuación de línea.

Las barras invertidas aún pueden ser apropiadas en ocasiones. Por ejemplo, withlas sentencias largas con múltiples caracteres no podían usar la continuación implícita antes de Python 3.10, por lo que las barras invertidas eran aceptables en ese caso:

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

(Consulte la discusión anterior sobre <a href="https://peps.python.org/pep-0008/#multiline-if-statements">sentencias if de varias líneas</a> para obtener más información sobre la sangría de dichas withsentencias de varias líneas).

Otro caso similar es el de assertlas declaraciones.

Asegúrese de sangrar adecuadamente la línea continua.

## ¿Debe un salto de línea ir antes o después de un operador binario?

<br>

Durante décadas, el estilo recomendado fue romper después de los operadores binarios. Sin embargo, esto puede perjudicar la legibilidad de dos maneras: los operadores tienden a dispersarse en diferentes columnas de la pantalla, y cada operador se desplaza de su operando a la línea anterior. En este caso, el ojo humano tiene que esforzarse más para distinguir qué elementos se suman y cuáles se restan.

<br>

### Incorrecto

```python
# operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

Para resolver este problema de legibilidad, los matemáticos y sus editores siguen la convención opuesta. Donald Knuth explica la regla tradicional en su serie "Computadoras y Tipografía ": «Aunque las fórmulas dentro de un párrafo siempre se dividen después de las operaciones y relaciones binarias, las fórmulas mostradas siempre se dividen antes de las operaciones binarias».

Seguir la tradición de las matemáticas generalmente da como resultado un código más legible:

<br>

### correcto

```python
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

<br>

## Líneas en blanco

Rodee las definiciones de funciones y clases de nivel superior con dos líneas en blanco.

Las definiciones de métodos dentro de una clase están rodeadas por una sola línea en blanco.

Se pueden usar líneas en blanco adicionales (con moderación) para separar grupos de funciones relacionadas. Se pueden omitir líneas en blanco entre varios scripts de una sola línea relacionados (por ejemplo, un conjunto de implementaciones ficticias).

Utilice líneas en blanco en las funciones, con moderación, para indicar secciones lógicas.

Python acepta el carácter de avance de página Ctrl+L (es decir, ^L) como espacio en blanco; muchas herramientas tratan estos caracteres como separadores de página, por lo que puede usarlos para separar páginas de secciones relacionadas de su archivo. Tenga en cuenta que algunos editores y visores de código web podrían no reconocer Ctrl+L como avance de página y mostrar otro glifo en su lugar.

Te muestro un ejemplo visual en código Python siguiendo las reglas de PEP 8 sobre líneas en blanco. Así puedes ver cómo se aplican en la práctica:

```python
# Ejemplo de PEP 8: uso de líneas en blanco


class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def metodo_uno(self):
        # Una línea en blanco separa métodos dentro de la clase
        print("Método uno ejecutado")

    def metodo_dos(self):
        print("Método dos ejecutado")


# Dos líneas en blanco separan definiciones de nivel superior
def funcion_principal():
    # Se pueden usar líneas en blanco dentro de la función
    # para separar secciones lógicas

    print("Inicio de la función")

    # Sección lógica 1
    datos = [1, 2, 3]
    for d in datos:
        print(d)

    # Sección lógica 2
    resultado = sum(datos)
    print("Suma:", resultado)


def funcion_auxiliar():
    print("Función auxiliar ejecutada")


# Ejemplo de scripts de una sola línea relacionados (sin líneas en blanco)
x = 1; y = 2; z = 3


# Separador de página con Ctrl+L (puede aparecer como ^L en algunos editores)
# ^L
def otra_funcion():
    print("Nueva sección del archivo")

```
<br>

## 🔎 Explicación visual:

`Dos líneas en blanco` antes de `class MiClase` y `def funcion_principal`.

`Una línea` en blanco entre `métodos` dentro de la `clase`.

`Líneas en blanco` dentro de `funciones` para separar `secciones lógicas` (**Sección lógica 1** y **Sección lógica 2**).

`Scripts de una sola línea` relacionados (`x = 1; y = 2; z = 3`) sin líneas en blanco.

Separador de página `Ctrl+L` o (`^L`) usado para dividir secciones grandes del archivo.

<br>

<br>

## Codificación de archivos fuente

El código en la distribución principal de Python siempre debe usar `UTF-8` y no debe tener una declaración de codificación.

En la biblioteca estándar, las codificaciones distintas de `UTF-8` solo deben usarse para pruebas. Use caracteres distintos de `ASCII` con moderación, preferiblemente solo para indicar lugares y nombres de personas. Si utiliza caracteres distintos de `ASCII`  como datos, evite caracteres Unicode con ruido como `z̯̯͡a̧͎̺l̡͓̫g̹̲o̡̼̘` y marcas de orden de bytes.

Todos los identificadores en la biblioteca estándar de Python DEBEN utilizar `identificadores` que solo sean `ASCII` y DEBEN utilizar palabras en inglés siempre que sea posible (en muchos casos, se utilizan abreviaturas y términos técnicos que no están en inglés).

Se alienta a los proyectos de código abierto con una audiencia global a adoptar una política similar.

<br>

## Importaciones

Las importaciones normalmente deben realizarse en líneas separadas:

```python
# Correct:
import os
import sys
```
```python
# Wrong:
import sys, os
```

Está bien decir esto:

```python
# Correct:
from subprocess import Popen, PIPE
```

Las importaciones siempre se colocan en la parte superior del archivo, justo después de los comentarios y cadenas de documentación del módulo, y antes de las constantes y los valores globales del módulo.
Las importaciones deben agruparse en el siguiente orden:

* Importaciones de biblioteca estándar.
* Importaciones de terceros relacionadas.
* Importaciones específicas de aplicaciones/bibliotecas locales.
* Debes poner una línea en blanco entre cada grupo de importaciones.

Se recomiendan las importaciones absolutas, ya que suelen ser más legibles y tienden a tener un mejor comportamiento (o al menos dan mejores mensajes de error) si el sistema de importación está configurado incorrectamente (como cuando un directorio dentro de un paquete termina en sys.path):

```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

Sin embargo, las importaciones relativas explícitas son una alternativa aceptable a las importaciones absolutas, especialmente cuando se trabaja con diseños de paquetes complejos en los que el uso de importaciones absolutas sería innecesariamente detallado:

```python
from . import sibling
from .sibling import example
```

El código de la biblioteca estándar debe evitar diseños de paquetes complejos y utilizar siempre importaciones absolutas.

Al importar una clase desde un módulo que contiene una clase, generalmente está bien escribir esto:

```python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

Si esta ortografía provoca conflictos en los nombres locales, escríbalos explícitamente:

```python
import myclass
import foo.bar.yourclass
```

y usar myclass.MyClassy foo.bar.yourclass.YourClass.

Se deben evitar las importaciones con comodines `( )`, ya que no aclaran qué nombres están presentes en el espacio de nombres, lo que confunde tanto a los lectores como a muchas herramientas automatizadas. Existe un caso práctico justificable para una importación con comodines: republicar una interfaz interna como parte de una API pública (por ejemplo, sobrescribir una implementación pura de Python de una interfaz con las definiciones de un módulo acelerador opcional, sin saber de antemano qué definiciones se sobrescribirán).`from <module> import*`
Al republicar nombres de esta manera, aún se aplican las pautas a continuación con respecto a las interfaces públicas e internas.

<br>

## ESTE ES UN BREVE RESÚMEN DE LAS BUENAS PRACTICAS Y CONVENCIÓN  EN CUANTO AL ESTILO  DEL CÓDIGO EN PYTHON A L AHORA DE TRABAJAR, SIN ENBARGO, ESTE MANUAL ES MUY EXTENSO, AQUÍ SOLO TOCAMOS ALGUNOS PARAMETROS ESCENCIALES DE LA SECCIÓN 8 DEL MANUAL PEP DE PYTHON, TE INVITO A QUE EXPLORES LA DOCUMENTACIÓN OFICIAL DE PYTHON PARA MÁS INFORMACIÓN: [PEP 8 – Style Guide for Python Code (Python Software Foundation)](https://peps.python.org/pep-0008/)

