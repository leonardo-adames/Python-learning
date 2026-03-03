# ASIGNACIÓN DE VARIABLES MULTIPLES

# Podemos asignar múltiples variables en una sola línea de código

# Ejemplo 1: Asignación múltiple directa
a, b, c = 5, 10, 15    # Asignamos 5 a 'a', 10 a 'b' y 15 a 'c'
print("Ejemplo 1:")    # Imprimimos el título del ejemplo
print("a =", a)        # Imprimimos el valor de 'a'
print("b =", b)        # Imprimimos el valor de 'b'
print("c =", c)        # Imprimimos el valor de 'c'
print()                # Línea en blanco para separar ejemplos
#SALIDA DE EJEMPLO 1:
#Ejemplo 1:
#a = 5
#b = 10
#c = 15

# Ejemplo 2: Asignación del mismo valor a múltiples variables
x = y = z = 20         # Asignamos 20 a 'x', 'y' y 'z'
print("Ejemplo 2:")    # Imprimimos el título del ejemplo
print("x =", x)        # Imprimimos el valor de 'x'
print("y =", y)        # Imprimimos el valor de 'y'
print("z =", z)        # Imprimimos el valor de 'z'
print()                # Línea en blanco para separar ejemplos
#SALIDA DE EJEMPLO 2:
#Ejemplo 2:
#x = 20
#y = 20
#z = 20

# Ejemplo 3: Asignación múltiple no válidos
a, b = 1, 2, 3         # Este generará un error porque hay más valores que variables
print("Ejemplo 3:")    # Imprimimos el título del ejemplo
print("a =", a)        # Imprimimos el valor de 'a'
print("b =", b)        # Imprimimos el valor de 'b'
#SALIDA DE EJEMPLO 3:
#Ejemplo 3:
#a = 1
#b = 2
# Error: ValueError: too many values to unpack (expected 2)
# Nota: El tercer ejemplo generará un error en tiempo de ejecución debido a la desalineación entre el número de variables y valores.

# Ejemplo 4: Asignacion múltiple con listas o tuplas
# Con listas:
lista = [1, 2, 3]      # Definimos una lista con tres elementos
d, e, f = lista        # Asignamos los elementos de la lista a las variables 'd', 'e' y 'f'
print("Ejemplo 4:")    # Imprimimos el título del ejemplo
print("d =", d)        # Im primimos el valor de 'd'
print("e =", e)        # Imprimimos el valor de 'e'
print("f =", f)        # Imprimimos el valor de 'f'
#SALIDA DE EJEMPLO 4:
#Ejemplo 4:
#d = 1
#e = 2
#f = 3

# Con tuplas:
tupla = (4, 5, 6)      # Definimos una tupla con tres elementos
g, h, i = tupla        # Asignamos los elementos de la tupla a las variables 'g', 'h' y 'i'
print("Ejemplo 5:")    # Imprimimos el título del ejemplo
print("g =", g)        # Imprimimos el valor de 'g'
print("h =", h)        # Imprimimos el valor de 'h'
print("i =", i)        # Imprimimos el valor de 'i'
#SALIDA DE EJEMPLO 5:
#Ejemplo 5:
#g = 4
#h = 5
#i = 6
# Nota: Asegúrate de que el número de variables coincida con el número de valores para evitar errores.
