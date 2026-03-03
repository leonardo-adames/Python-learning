# BootCamp Python 3.14 - Sesión 2

## 2.6 - Concatenar

### Definición

Concatenar es el proceso de unir dos o más cadenas de texto (strings) para formar una sola cadena. En Python, esto se puede hacer utilizando el operador `+` o el método `join()` entre otros, a continuación algunos ejemplos:

**Usando el operador `+`:**

Para concatenar con el operador `+` se debe colocar el signo `+` entre las cadenas que se desean unir, como se muestra en el siguiente ejemplo:

```python
#Concatenar usando el signo (+):
#---Variables---#
cadena1 = "Hola, "
cadena2 = "mundo!"
print(cadena1 + " " + cadena2)    # Sintaxis para concatenar usando el signo (+)
```

 Resultado:**

```python
Hola, mundo!
```

**Agregando `cadenas de string` antes de las variales:**
También se puede concatenar texto adicional junto con las variables,como en el Ejemplo acontinuación:

```python
#---sintaxis---#
nombre = 'leonardo jose'        #VARIABLE 1
apellido = 'marte adames'       #VARIABLE 2
estatura = 7.6                  #VARIABLE 3
edad = 28                       #VARIABLE 4

print(nombre + " " + apellido)                      #concatenar con (+)
print("mido", estatura, "y tengo", edad, "años")    #con texto entre lemento
```

**Resultado:**

```python
hola me llamo leonardo jose marte adames
mido 7.6 y tengo 28 años
```

**Usando `f-string:**

Otra forma moderna y eficiente de concatenar cadenas en Python es utilizando f-strings (cadenas formateadas), para hacerlo se antepone la letra `f` antes de las comillas de la cadena y se incluyen las variables entre llaves `{}` dentro de la cadena, como se muestra en el siguiente ejemplo:

```python
#---sintaxis f-string---#
nombre = 'leonardo jose'        #VARIABLE 1
apellido = 'marte adames'       #VARIABLE 2
estatura = 7.6                  #VARIABLE 3
edad = 28                       #VARIABLE 4

print(f"hola me llamo {nombre} {apellido}, mido {estatura} y tengo {edad} años")
```

**Resultado**

```python
hola me llamo leonardo jose marte adames, mido 7.6 y tengo 28 años
```

### El uso de `f-strings` el más recomendado por su claridad y eficiencia a la hora de concatenar cadenas de `string y multiples elementos, especialmente cuando se trabaja con múltiples variables

**Usando el método `format()`:**

'''En pyrhon el metodo format consiste en Python es practicamente la misma sintaxis
que el f-tring y comparten el mismo objetivo, en este caso solo reemplazamos las llaves por el formato
de los argumentos u objetos'''

```python
#---sintaxis format()---#
'''Aquí veremos algunos ejemplos en Python sobre el método (format)'''

nombre = 'leonardo jose'        #VARIABLE 1
apellido = 'marte adames'       #VARIABLE 2
estatura = 7.6                  #VARIABLE 3
edad = 28                       #VARIABLE 4

print("hola, me llamo {n} {a}, mido {e} y tengo {ed} años".format(
    n=nombre, a=apellido, e=estatura, ed=edad))
```

**Resultado**

```python
hola, me llamo leonardo jose marte adames, mido 7.6 y tengo 28 años
```

**Usando Comodín `%`:**

Otra forma de concatenar cadenas en Python es utilizando el operador de formato `%`, que permite insertar variables en una cadena de texto mediante especificadores de formato. A continuación, se muestra un ejemplo:

```python
#---sintaxis con el comodín %---#
nombre = 'leonardo jose'        #VARIABLE 1
apellido = 'marte adames'       #VARIABLE 2
estatura = 7.6                  #VARIABLE 3
edad = 28                       #VARIABLE 4
print("hola, me llamo %s %s, mido %.1f y tengo %d años" % (nombre, apellido, estatura, edad))
```

**Resultado**

```python
hola, me llamo leonardo jose marte adames, mido 7.6 y tengo 28 años
```

### Al usar el comodín `%` es importante asegurarse de que los tipos de datos de las variables coincidan con los especificadores de formato utilizados en la cadena:

### `%s` para cadenas

### `%d` para enteros y

### `%.1f` para números de punto flotante con un decimal

## ESTOS SON TODOS LOS MÉTODOS DE CONCATENACIÓN EN PYTHON DE STRINGS, VARIABLES Y VALORES, SIN EMBARGO, EL F-STRING ES EL MAS USADO Y RECOOMENDADO.
