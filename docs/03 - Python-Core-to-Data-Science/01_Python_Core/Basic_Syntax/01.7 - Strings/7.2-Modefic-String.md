# BootCamp Python Sesión 7 - Los String / Instrumentos de cuerdas

## 7.2 Modificar Cadenas en python

* Python tiene un conjunto de métodos integrados que puedes usar en cadenas.

### Majúsculas

* El método devuelve la cadena en mayúsculas:`upper()`

Ejemplo

```python
a = "Hello, World!"
print(a.upper())
```

### Minúsculas

* El método devuelve la cadena en minúsculas:`lower()`

Ejemplo

```python
a = "Hello, World!"
print(a.lower())
```

### Eliminar espacios en blanco

* El espacio en blanco es el espacio antes y/o después del texto real, y muy a menudo quieres eliminar ese espacio.

Ejemplo

* El método elimina cualquier espacio en blanco desde el principio o el final:`strip()`

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

### Reemplazar la cuerda

* El método reemplaza una cadena por otra cadena:replace()

Ejemplo

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

## Cuerda partida

* El método devuelve una lista donde el texto entre los separadores especificados se convierte en los elementos de la `lista.split()`

Ejemplo

* El método divide la cadena en subcadenas si encuentra instancias del separador:`split()`

```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```

# Concatenación de cadenas En Python

### Concatenación de cadenas

Para concatenar o combinar dos cadenas puedes usar el operador `+`.

Ejemplo

* Fusionar variable con variable en variable :abc

```python
a = "Hello"
b = "World"
c = a + b
print(c)
```

* Para añadir un espacio entre ellos, añade un :`" "`

Ejemplo

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```

# Métodos de cuerdas

* Python tiene un conjunto de métodos integrados que puedes usar en cadenas.

**Nota:** Todos los métodos de cadenas devolven nuevos valores. No cambian la cuerda original.

| Método         | Descripción                                                               |
| -------------- | ------------------------------------------------------------------------- |
| capitalize()   | Convierte el primer carácter a mayúscula                                  |
| casefold()     | Convierte la cadena a minúsculas                                          |
| center()       | Devuelve una cadena centrada                                              |
| count()        | Devuelve el número de veces que un valor específico aparece en una cadena |
| encode()       | Devuelve una versión codificada de la cadena                              |
| endswith()     | Devuelve `True` si la cadena termina con el valor especificado            |
| expandtabs()   | Establece el tamaño de tabulación de la cadena                            |
| find()         | Busca un valor en la cadena y devuelve la posición donde se encontró      |
| format()       | Da formato a valores especificados en una cadena                          |
| format_map()   | Da formato a valores especificados en una cadena                          |
| index()        | Busca un valor en la cadena y devuelve la posición donde se encontró      |
| isalnum()      | Devuelve `True` si todos los caracteres son alfanuméricos                 |
| isalpha()      | Devuelve `True` si todos los caracteres son letras                        |
| isascii()      | Devuelve `True` si todos los caracteres son ASCII                         |
| isdecimal()    | Devuelve `True` si todos los caracteres son decimales                     |
| isdigit()      | Devuelve `True` si todos los caracteres son dígitos                       |
| isidentifier() | Devuelve `True` si la cadena es un identificador válido                   |
| islower()      | Devuelve `True` si todos los caracteres están en minúscula                |
| isnumeric()    | Devuelve `True` si todos los caracteres son numéricos                     |
| isprintable()  | Devuelve `True` si todos los caracteres son imprimibles                   |
| isspace()      | Devuelve `True` si todos los caracteres son espacios en blanco            |
| istitle()      | Devuelve `True` si la cadena sigue las reglas de un título                |
| isupper()      | Devuelve `True` si todos los caracteres están en mayúscula                |
| join()         | Une los elementos de un iterable a la cadena                              |
| ljust()        | Devuelve una versión alineada a la izquierda                              |
| lower()        | Convierte la cadena a minúsculas                                          |
| lstrip()       | Elimina espacios a la izquierda                                           |
| maketrans()    | Crea una tabla de traducción                                              |
| partition()    | Divide la cadena en tres partes y devuelve una tupla                      |
| replace()      | Reemplaza un valor por otro                                               |
| rfind()        | Devuelve la última posición encontrada                                    |
| rindex()       | Devuelve la última posición encontrada                                    |
| rjust()        | Devuelve una versión alineada a la derecha                                |
| rpartition()   | Divide la cadena en tres partes y devuelve una tupla                      |
| rsplit()       | Divide la cadena y devuelve una lista                                     |
| rstrip()       | Elimina espacios a la derecha                                             |
| split()        | Divide la cadena y devuelve una lista                                     |
| splitlines()   | Divide la cadena por saltos de línea                                      |
| startswith()   | Devuelve `True` si la cadena empieza con el valor indicado                |
| strip()        | Elimina espacios a ambos lados                                            |
| swapcase()     | Intercambia mayúsculas y minúsculas                                       |
| title()        | Convierte la primera letra de cada palabra a mayúscula                    |
| translate()    | Traduce la cadena usando una tabla                                        |
| upper()        | Convierte la cadena a mayúsculas                                          |
| zfill()        | Rellena la cadena con ceros al inicio                                     |
