<div align="center">
    <kbd>
        <h1><b>CURSO DE PYTHON</b><br>INTRODUCCIÓN GENERAL</b></h1>
        <img width="2064" height="100%" alt="Image" src="../../notes/resources/INTRO/Py_welcome6.png" altº="Image" width="100%"/>
    </kbd>
    <br>
    <br>
    <h2><b>PALABRAS RESERVADAS [KEYWORDS]</b></h2>
</div>
    
<h3 align="center">🐍 Python Keywords</h3>

<table width="100%" align="center">
  <tr>
    <td align="center"><code>False</code></td>
    <td align="center"><code>break</code></td>
    <td align="center"><code>for</code></td>
    <td align="center"><code>not</code></td>
    <td align="center"><code>None</code></td>
    <td align="center"><code>class</code></td>
  </tr>
  <tr>
    <td align="center"><code>from</code></td>
    <td align="center"><code>or</code></td>
    <td align="center"><code>True</code></td>
    <td align="center"><code>continue</code></td>
    <td align="center"><code>global</code></td>
    <td align="center"><code>pass</code></td>
  </tr>
  <tr>
    <td align="center"><code>__peg_parser__</code></td>
    <td align="center"><code>def</code></td>
    <td align="center"><code>if</code></td>
    <td align="center"><code>raise</code></td>
    <td align="center"><code>and</code></td>
    <td align="center"><code>del</code></td>
  </tr>
  <tr>
    <td align="center"><code>import</code></td>
    <td align="center"><code>return</code></td>
    <td align="center"><code>as</code></td>
    <td align="center"><code>elif</code></td>
    <td align="center"><code>in</code></td>
    <td align="center"><code>try</code></td>
  </tr>
  <tr>
    <td align="center"><code>assert</code></td>
    <td align="center"><code>else</code></td>
    <td align="center"><code>is</code></td>
    <td align="center"><code>while</code></td>
    <td align="center"><code>async</code></td>
    <td align="center"><code>except</code></td>
  </tr>
  <tr>
    <td align="center"><code>lambda</code></td>
    <td align="center"><code>with</code></td>
    <td align="center"><code>await</code></td>
    <td align="center"><code>finally</code></td>
    <td align="center"><code>nonlocal</code></td>
    <td align="center"><code>yield</code></td>
  </tr>
</table>

<br><br>

## **DIFINICIÓN DE PALABRAS RESERVADAS EN PYTHON:**

<br>

Las `palabras reservadas` en Python son identificadores especiales con funciones y restricciones específicas, que no pueden utilizarse como nombres de variables, funciones o cualquier otro identificador. Con cerca de `35 palabras clave` fundamentales incluyendo `False`, `None`, `True`, `and`, `def`, `if`, `class`, `import`—, son esenciales para la sintaxis del lenguaje y están disponibles sin importar módulos.

<br>
<br>

## **Características Clave**

<br>

* **No se pueden usar:** Intentar usar estas palabras como nombres de variables provoca un error de sintaxis.

* **Sensibles a mayúsculas:** Python diferencia entre mayúsculas y minúsculas; `True` es una palabra reservada, pero `true` no lo es.

* **Identificación:** Generalmente, los editores de código `IDEs` resaltan estas palabras en un color diferente. 

**Se pueden consultar todas las palabras reservadas en cualquier momento usando el comando help`"keywords"` en el intérprete de Python.**

<br>

**USO INCORRECTO DE LAS PALABRAS RESERVADAS:**


```python
# Esto generará un error de sintaxis
if = 10

# Esto también generará un error de sintaxis
def = "mi_funcion"
```
**INCORRECTO:** **No se pueden usar** `palabras reservadas` como `nombres` de `variables` o `funciones`.

<br><br>

```PYTHON
# Esto es correcto
if_value = 10  

my_def = "mi_funcion"
```
**ÉSTO PARECE LO CORRECTO:** No es una palabra reservada aquí, es un nombre de variable válido, sin embarGo, tampoco es recomendable usar palabras reservadas como parte de los nombres de variables, aunque técnicamente es posible. Por ejemplo, `if_value` es un nombre de variable válido, pero no es una buena práctica porque puede causar confusión al leer el código.

<br>

**USO INCORRECTO DE LAS PALABRAS RESERVADAS:**

```python


def mi_funcion():
  edad = 25

  if edad > 18:
    print("Mayor de edad")

  else:
    print("Menor de edad") 
```
**CORRECTO Y RECOMENDADO:** Ésto sisría lo correcto y recomendado, ya que se respetan las palabras reservadas en su función original y se utilizan nombres de variables claros y descriptivos.

<br>

<h2 align="center">🐍 Palabras Reservadas & Sus Funciones</h2>

<table align="center" width="100%">
  <thead>
    <tr>
      <th align="center">Keyword</th>
      <th align="center">Definición</th>
      <th align="center">Ejemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr><td align="center"><code>False</code></td><td>Valor booleano falso.</td><td><code>activo = False</code></td></tr>
    <tr><td align="center"><code>None</code></td><td>Representa la ausencia de valor.</td><td><code>resultado = None</code></td></tr>
    <tr><td align="center"><code>True</code></td><td>Valor booleano verdadero.</td><td><code>activo = True</code></td></tr>
    <tr><td align="center"><code>__peg_parser__</code></td><td>Uso interno del parser PEG de Python.</td><td><em>Uso interno del intérprete</em></td></tr>
    <tr><td align="center"><code>and</code></td><td>Operador lógico “y”.</td><td><code>if x > 0 and y > 0:</code></td></tr>
    <tr><td align="center"><code>as</code></td><td>Alias para módulos o excepciones.</td><td><code>import math as m</code></td></tr>
    <tr><td align="center"><code>assert</code></td><td>Verifica una condición; lanza error si es falsa.</td><td><code>assert edad > 0</code></td></tr>
    <tr><td align="center"><code>async</code></td><td>Define funciones asincrónicas.</td><td><code>async def cargar_datos():</code></td></tr>
    <tr><td align="center"><code>await</code></td><td>Espera el resultado de una función asincrónica.</td><td><code>datos = await cargar_datos()</code></td></tr>
    <tr><td align="center"><code>break</code></td><td>Sale de un bucle.</td><td><code>if x == 5: break</code></td></tr>
    <tr><td align="center"><code>class</code></td><td>Define una clase.</td><td><code>class Persona:</code></td></tr>
    <tr><td align="center"><code>continue</code></td><td>Salta a la siguiente iteración del bucle.</td><td><code>if x &lt; 0: continue</code></td></tr>
    <tr><td align="center"><code>def</code></td><td>Define una función.</td><td><code>def saludar():</code></td></tr>
    <tr><td align="center"><code>del</code></td><td>Elimina una variable o elemento.</td><td><code>del lista[0]</code></td></tr>
    <tr><td align="center"><code>elif</code></td><td>Condición adicional en una estructura <code>if</code>.</td><td><code>elif edad &lt; 18:</code></td></tr>
    <tr><td align="center"><code>else</code></td><td>Alternativa si no se cumple ninguna condición previa.</td><td><code>else: print("Mayor de edad")</code></td></tr>
    <tr><td align="center"><code>match</code></td><td>Inicia una estructura de coincidencia de patrones.</td><td><code>match status_code:</code></td></tr>
    <tr><td align="center"><code>case</code></td><td>Define un patrón específico dentro de un <code>match</code>.</td><td><code>case 404: print("No encontrado")</code></td></tr>
    <tr><td align="center"><code>except</code></td><td>Maneja excepciones en bloques <code>try</code>.</td><td><code>except ValueError:</code></td></tr>
    <tr><td align="center"><code>finally</code></td><td>Código que se ejecuta siempre al final de <code>try</code>.</td><td><code>finally: cerrar_archivo()</code></td></tr>
    <tr><td align="center"><code>for</code></td><td>Bucle que itera sobre una secuencia.</td><td><code>for i in range(5):</code></td></tr>
    <tr><td align="center"><code>from</code></td><td>Importa partes específicas de un módulo.</td><td><code>from math import pi</code></td></tr>
    <tr><td align="center"><code>global</code></td><td>Declara una variable como global.</td><td><code>global contador</code></td></tr>
    <tr><td align="center"><code>if</code></td><td>Evalúa una condición lógica.</td><td><code>if edad > 18:</code></td></tr>
    <tr><td align="center"><code>import</code></td><td>Importa módulos.</td><td><code>import os</code></td></tr>
    <tr><td align="center"><code>in</code></td><td>Verifica pertenencia en una secuencia.</td><td><code>if "a" in lista:</code></td></tr>
    <tr><td align="center"><code>is</code></td><td>Compara identidad de objetos.</td><td><code>if x is None:</code></td></tr>
    <tr><td align="center"><code>lambda</code></td><td>Define funciones anónimas.</td><td><code>f = lambda x: x * 2</code></td></tr>
    <tr><td align="center"><code>nonlocal</code></td><td>Declara variables en ámbitos externos no globales.</td><td><code>nonlocal contador</code></td></tr>
    <tr><td align="center"><code>not</code></td><td>Operador lógico de negación.</td><td><code>if not activo:</code></td></tr>
    <tr><td align="center"><code>or</code></td><td>Operador lógico “o”.</td><td><code>if x &lt; 0 or y &lt; 0:</code></td></tr>
    <tr><td align="center"><code>pass</code></td><td>No ejecuta ninguna acción; marcador vacío.</td><td><code>def vacia(): pass</code></td></tr>
    <tr><td align="center"><code>raise</code></td><td>Lanza una excepción.</td><td><code>raise ValueError("Error")</code></td></tr>
    <tr><td align="center"><code>return</code></td><td>Devuelve un valor desde una función.</td><td><code>return resultado</code></td></tr>
    <tr><td align="center"><code>try</code></td><td>Ejecuta código que puede producir errores.</td><td><code>try: abrir_archivo()</code></td></tr>
    <tr><td align="center"><code>while</code></td><td>Bucle que se ejecuta mientras una condición sea verdadera.</td><td><code>while x &lt; 10:</code></td></tr>
    <tr><td align="center"><code>with</code></td><td>Maneja contextos como archivos o recursos.</td><td><code>with open("archivo.txt") as f:</code></td></tr>
    <tr><td align="center"><code>yield</code></td><td>Devuelve valores desde una función generadora.</td><td><code>yield elemento</code></td></tr>
  </tbody>
</table>

<br>
<br>

### **IMPORTANTE:**<br>
AQUÍ NO LAS DEFINIREMOS TODAS, A MEDIDA QUE AVANCE EL CURSO IREMOS DEFINIENDO CADA UNA A SUVEZ LLEVANDOLA A LA PRACTICA SEGÚN CORRESPONDA 

<br>



## **CLASIFICACIÓN DE LAS KEYWORDS INTEGRADAS DE PYTHON**

<br>

<h3 align="center"><b>🐍 Lista principal de palabras reservadas <kbd>Python 3</kbd></b></h3>

<br>

<table width="100%" align="center">
  <tr>
    <td align="center" valign="top" width="33.33%">
      <kbd>
        <strong>1️⃣ Booleanos · Nulos</strong>
        <br><br>
        <code>False</code> · <code>None</code> · <code>True</code>
      </kbd>
    </td>
    <td align="center" valign="top" width="33.33%">
      <kbd>
        <strong>2️⃣ Lógicos</strong>
        <br><br>
        <code>and</code> · <code>or</code> · <code>not</code>
      </kbd>
    </td>
    <td align="center" valign="top" width="33.33%">
      <kbd>
        <strong>3️⃣ Definición de elementos</strong>
        <br><br>
        <code>def</code> · <code>class</code> · <code>lambda</code>
      </kbd>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="33.33%">
      <kbd>
      <br>
        <strong>4️⃣ Estructuras de control</strong>
        <br><br>
        <code>if</code> · <code>elif</code> · <code>else</code> · <code>for</code> · <code>while</code> · <code>break</code> · <code>continue</code> · <code>return</code> · <code>match</code> · <code>case</code>
      </kbd>
    </td>
    <td align="center" valign="top" width="33.33%">
      <kbd>
      <br>
        <strong>5️⃣ Manejo de excepciones</strong>
        <br><br>
        <code>try</code> · <code>except</code> · <code>finally</code> · <code>raise</code> · <code>assert</code>
      </kbd>
    </td>
    <td align="center" valign="top" width="33.33%">
      <kbd>
      <br>
        <strong>6️⃣ Importación · Alias</strong>
        <br><br>
        <code>import</code> · <code>from</code> · <code>as</code>
      </kbd>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="33.33%">
      <kbd>
      <br>
        <strong>7️⃣ Gestión de variables</strong>
        <br><br>
        <code>del</code> · <code>global</code> · <code>nonlocal</code>
      </kbd>
    </td>
    <td align="center" valign="top" width="33.33%">
      <kbd>
      <br>
        <strong>8️⃣ Asincronía</strong>
        <br><br>
        <code>async</code> · <code>await</code>
      </kbd>
    </td>
    <td align="center" valign="top" width="33.33%">
      <kbd>
      <br>
        <strong>9️⃣ Otros</strong>
        <br><br>
        <code>with</code> · <code>pass</code> · <code>yield</code>
      </kbd>
    </td>
  </tr>
</table>

<br>
<br>

## Las palabras clave suaves

Las palabras clave suaves (`soft keywords`) en Python, introducidas principalmente desde la versión 3.10, son identificadores especiales que actúan como palabras reservadas solo en contextos específicos (ej. estructuras `match-case` o `type`), permitiendo que se usen como nombres de variables normales fuera de esos bloques. Las principales palabras clave suaves son `match`, `case` y `_` (**comodín**). 

<br>

- `match` y `case`: Se usan en la coincidencia de patrones estructurales. Fuera de esta estructura, pueden ser nombres de variables válidos.

<br>

```python
# CASO DE USO DE match y case como variables
match = "esto es una variable"
case = "esto es otra variable" 
```
<br>

```python
# Uso en contexto de match-case
valor = 10
match valor:
    case 10:
        print("Es diez")
```

**Aquí `match` y `case` actúan como palabras clave suaves, y no pueden ser usadas como variables.
En este contexto, `match` inicia la estructura de coincidencia y `case` define los patrones a comparar, En cualquiera de los casos tampoco es conveniente usarlas cono nombre de variables, según las buenas prácticas y convensión del Lenguaje**

<br>

- `_` (guion bajo): Funciona como un comodín en `match-case`, pero también se utiliza en el intérprete interactivo para referirse al último resultado.

<br>

**Uso de `_` como comodín en match-case**

```python

valor = 10
match valor:
    case 10:
        print("Es diez")
    case _:
        print("No es diez")
print(f"El valor es: {valor}")
```
<br>

**Uso de `_` para referirse al último resultado en el intérprete interactivo**

```python

>>> 10 + 5
15
>>> _ + 5
20
```

<br>

**Otros casos de uso de _**

Uso de `_` para ignorar valores en desempaquetado de tuplas o listas:

```python

a, _, c = (1, 2, 3)
print(f"a: {a}, c: {c}")
```

<br>

Uso de `_` para ignorar el índice en un bucle for:

```python

for _ in range(3):
    print("Hola")
```
<br>

Uso de `_` para ignorar argumentos en una función lambda

```python
saludar = lambda x, _, z: f"Hola {x} y {z}"
print(saludar("Mundo", "ignorado", "Python"))
```
<br>

Uso de `_` para nombrar variables que no se usarán

```python
def procesar_datos():
    return 10, 20, 30

valor1, _, _ = procesar_datos()
print(f"Valor 1: {valor1}")

```

- `type`: **Convertido en palabra clave** suave en `Python 3.12` para `declaraciones de tipo`, pero sigue siendo utilizable fuera de ese contexto. 

```python
# Uso de type como palabra clave suave en anotaciones de tipo
def suma(a: int, b: int) -> int:
    return a + b

# Uso de type como variable normal
type = "esto es una variable"


#Uso de type para declarar tipos

def procesar_datos(data: type) -> type:
    return data.upper()
```

<br>

**Ventaja**: Permiten introducir nuevas funcionalidades en Python sin romper el código antiguo que ya utilizaba estas palabras como nombres de variables. 

<br>

**EJEMPLO:**

```python
# Uso como palabra clave suave
match = 5  # Válido (variable)
case = 10  # Válido (variable)

# Uso en contexto especial (match-case)
valor = 10
match valor:
    case 10:  # Aquí 'case' es palabra clave suave
        print("Es diez")

```

---
<br>
<br>

<h2 align="center">📚 Bibliografía completa · Fuentes oficiales de Python</h2>

<table width="100%" align="center">
  <tr>
    <th align="center" width="55%">Tema</th>
    <th align="center" width="45%">Fuente oficial</th>
  </tr>
  <tr>
    <td>Flujo de control (<code>if</code>, <code>for</code>, <code>while</code>, <code>break</code>, <code>continue</code>, <code>pass</code>)</td>
    <td><a href="https://docs.python.org/3/tutorial/controlflow.html">docs.python.org/3/tutorial/controlflow.html</a></td>
  </tr>
  <tr>
    <td>Tipos integrados: <code>list</code> (métodos de listas)</td>
    <td><a href="https://docs.python.org/3/library/stdtypes.html#list">docs.python.org/3/library/stdtypes.html#list</a></td>
  </tr>
  <tr>
    <td>Tipos integrados: <code>dict</code> (métodos de diccionarios)</td>
    <td><a href="https://docs.python.org/3/library/stdtypes.html#mapping-types-dict">docs.python.org/3/library/stdtypes.html#mapping-types-dict</a></td>
  </tr>
  <tr>
    <td>Operadores aritméticos y conversiones</td>
    <td><a href="https://docs.python.org/3/reference/expressions.html#arithmetic-conversions">docs.python.org/3/reference/expressions.html#arithmetic-conversions</a></td>
  </tr>
  <tr>
    <td>Operaciones booleanas (<code>and</code>, <code>or</code>, <code>not</code>)</td>
    <td><a href="https://docs.python.org/3/reference/expressions.html#boolean-operations">docs.python.org/3/reference/expressions.html#boolean-operations</a></td>
  </tr>
  <tr>
    <td>Operaciones de membresía e identidad (<code>in</code>, <code>is</code>)</td>
    <td><a href="https://docs.python.org/3/reference/expressions.html#membership-test-operations">docs.python.org/3/reference/expressions.html#membership-test-operations</a></td>
  </tr>
  <tr>
    <td>Asignación aumentada (<code>+=</code>, <code>-=</code>)</td>
    <td><a href="https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements">docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements</a></td>
  </tr>
  <tr>
    <td>Declaraciones simples (<code>import</code>, <code>from</code>, <code>global</code>, <code>nonlocal</code>)</td>
    <td><a href="https://docs.python.org/3/reference/simple_stmts.html">docs.python.org/3/reference/simple_stmts.html</a></td>
  </tr>
  <tr>
    <td>Sentencias compuestas (<code>def</code>, <code>class</code>, <code>try</code>, <code>with</code>, <code>async</code>)</td>
    <td><a href="https://docs.python.org/3/reference/compound_stmts.html">docs.python.org/3/reference/compound_stmts.html</a></td>
  </tr>
  <tr>
    <td>Manejo de errores y excepciones</td>
    <td><a href="https://docs.python.org/3/tutorial/errors.html">docs.python.org/3/tutorial/errors.html</a></td>
  </tr>
  <tr>
    <td>Constantes (<code>True</code>, <code>False</code>, <code>None</code>)</td>
    <td><a href="https://docs.python.org/3/library/constants.html">docs.python.org/3/library/constants.html</a></td>
  </tr>
  <tr>
    <td>Palabras clave (lista oficial de keywords)</td>
    <td><a href="https://docs.python.org/3/reference/lexical_analysis.html#keywords">docs.python.org/3/reference/lexical_analysis.html#keywords</a></td>
  </tr>
  <tr>
    <td>FAQ: por qué Python no tiene <code>++</code> ni <code>--</code></td>
    <td><a href="https://docs.python.org/3/faq/design.html#why-doesn-t-python-have-increment-and-decrement-operators">docs.python.org/3/faq/design.html#why-doesn-t-python-have-increment-and-decrement-operators</a></td>
  </tr>
  <tr>
    <td>Modelo de datos (orden de <code>dict</code>)</td>
    <td><a href="https://docs.python.org/3/reference/datamodel.html#dict">docs.python.org/3/reference/datamodel.html#dict</a></td>
  </tr>
  <tr>
    <td>PEP 20 – El Zen de Python</td>
    <td><a href="https://peps.python.org/pep-0020/">peps.python.org/pep-0020/</a></td>
  </tr>
</table>

<br>
<br>

## **¡Y eso es todo por ahora!**

<br>

---
