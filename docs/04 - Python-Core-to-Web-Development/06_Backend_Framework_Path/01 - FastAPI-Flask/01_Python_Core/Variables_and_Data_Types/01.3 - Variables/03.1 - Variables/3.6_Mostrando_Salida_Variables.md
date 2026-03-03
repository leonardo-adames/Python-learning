# Bootcamp Python SESIÓN 3 -  VARIABLES & CONSTANTES

## 5. MOSTRANDO INFORMACIÓN DE SALIDA DE LAS VARIABLES

### COMBINANDO TEXTOS Y VARIABLES

Para mostrar información en pantalla, podemos utilizar la función `print()`. Esta función puede combinar textos (cadenas de caracteres) y variables para presentar información de manera clara. añadir un texto existente para concatenar una variable añadimosdo el símbolo `+` entre ellos.

Por ejemplo:

```python
nombre = "Ana"
edad = 28
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")
# Salida: Hola, mi nombre es Ana y tengo 28 años.
```

En este ejemplo, estamos combinando texto con las variables `nombre` y `edad`. Es importante convertir la variable `edad` a cadena de caracteres usando `str()` para evitar errores.

### COMBINANDO VARIABLE Y VARIABLES

También podemos combinar varias variables entre sí utilizando el mismo método de concatenación con el símbolo `+`.

Ejemplo 1:

```python
#TRES VARIABLES CON INFORMACIÓN DE TEXTO:
a = "Python "
b = "es"
c = "genial."
print(a + b + " " + c)
# Salida: Python es genial.
```

En este caso, estamos concatenando las variables `a`, `b` y `c` para formar una oración completa.

Ejemplo 2:

```python
#TRES VARIABLES CON INFORMACIÓN NUMÉRICA:
x = 10.5
y = 20
z = 30
print("La suma de x, y y z es: " + str(x + y + z))
#SALIDA: La suma de x, y y z es: 60.5
```

Aquí, estamos sumando las variables `x`, `y` y `z`, y luego mostrando el resultado en pantalla.

Ejemplo 3:

```python
#TRES VARIABLES DE DIFERENTES TIPOS:
nombre = "Carlos"
edad = 35
altura = 1.75
print("Nombre: " + nombre + ", Edad: " + str(edad) + ", Altura: " + str(altura) + " metros.")
# Salida: Nombre: Carlos, Edad: 35, Altura: 1.75 metros.
```

En este último ejemplo, combinamos una variable de texto (`nombre`), una variable entera (`edad`) y una variable flotante (`altura`) para mostrar toda la información en una sola línea.

Si intentamos combinar dos variables, donde una es texto y otra es de tipo numérico, nos dará error.

Por ejemplo:

```python
nombre = "Luis"
edad = 40
print(nombre + edad)    # Esto generará un error de tipo typeError: unsupported operand type(s) for +: 'str' and 'int'
```

Para evitar este error, debemos convertir la variable numérica a cadena de caracteres utilizando la función `str()`:

```python
nombre = "Luis"
edad = 40
print(nombre + " tiene " + str(edad) + " años.")  # Esto funcionará correctamente.
# Salida: Luis tiene 40 años.
```

Al usar la función `str()`para convertir la variable `edad` a cadena de caracteres, podemos combinarla con la variable `nombre` sin problemas. A esto se le llama conversión de tipos o casting.
