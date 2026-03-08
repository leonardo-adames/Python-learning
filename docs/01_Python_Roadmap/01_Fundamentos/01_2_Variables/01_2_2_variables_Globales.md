# Learning Python Level 1  SESIÓN 3 - VARIABLES & CONSTANTES

## 3.8- VARIABLES GLOBALES

Las variables globales son aquellas que se definen fuera de cualquier función y pueden ser accedidas desde cualquier parte del código, incluyendo dentro de funciones. A continuación, se presentan algunos conceptos clave sobre las variables globales en Python:

* **Definición:** Una variable global se declara fuera de cualquier función, generalmente al principio del archivo o en el nivel superior del código.
* **Acceso:** Pueden ser leídas y modificadas desde cualquier parte del programa, incluyendo dentro de funciones.
* **Modificación:** Para modificar una variable global dentro de una función, se debe usar la palabra clave `global` antes de la variable.

Ejemplo 1: uso de una variable global:

```python
# variable global (con la palabra reservada `global`)
adjetivo = "Fantastico"

def use_global_variable():
    print("Python es" + adjetivo)  # Acceder a la variable global

use_global_variable()
```

Salida:

```python
Python es Fantastico
```

En este ejemplo, la variable `adjetivo` es una variable global que se define fuera de la función `use_global_variable()`. La función puede acceder a esta variable y utilizar su valor.

Ejemplo de modificación de una variable global:

```python
contador = 0  # Variable global
def incrementar_contador():
    global contador  # Indicar que se va a usar la variable global
    contador += 1
    print("Contador:", contador)
incrementar_contador()  # Llama a la función
incrementar_contador()  # Llama a la función nuevamente
```

Salida:

```python
Contador: 1
Contador: 2
```

En este ejemplo, la función `incrementar_contador()` modifica la variable global `contador`
Al usar la palabra clave `global`. Cada vez que se llama a la función, el valor de `contador` se incrementa en 1.
Es importante usar las variables globales con precaución, ya que pueden hacer que el código sea más difícil de entender y mantener. En general, es recomendable limitar el uso de variables globales y preferir el paso de parámetros a funciones cuando sea posible.

Ejemplo 2: Sin usar la palabra clave `global`:

```python
# Sin usar la palabra clave `global`:
adjetive = "Increible"
def use_variable():
    adjetive = "Maravilloso"  # Variable local
    print("Python es " + adjetive)  # Accede a la variable local
print("Python es " + adjetive)  # Accede a la variable global
use_variable()
```

Salida:

```python
Python es Increible
Python es Maravilloso
```

En este ejemplo, la variable `adjetive` dentro de la función `use_variable()` es una variable local que no afecta a la variable global `adjetive`. Por lo tanto, cuando se imprime fuera de la función, se muestra el valor de la variable global. Sin embargo, dentro de la función, se utiliza la variable local.
