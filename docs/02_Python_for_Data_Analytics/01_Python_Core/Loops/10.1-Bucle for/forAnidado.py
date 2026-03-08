'''
# for Anidado

for i in range(7):
    for j in range(7):
        print(f"Valor: {i}")
    print("Fin del bucle interno")

print("Fin del bucle externo")


EXPLICACIÓ DEL EJEMPLO ANTERIOR:

AQUÍ TENEMOS UN BUCLE FOR ANIDADO, 

- El PRIMERO ES EL BUCLE EXTERNO Y el SEGUNDO ES EL BUCLE INTERNO.

- EL BUCLE EXTERNO SE EJECUTA 7 VECES.
  DENTRO DE CADA ITERACIÓN DEL BUCLE EXTERNO.

- El BUCLE INTERNO SE EJECUTA 7 VECES EN CADA ITERACIÓN DEL BUCLE EXTERNO.

'''

# EJERCICIO DE FOR ANIDADO: CREAR UN RECTANGULO CON UN SIMBOLO DONDE
# DE NECESITA ESTABLECER UN ANCHO Y UN ALTO PARA ESTO
# SE NECESITA ESTABLECER UN SIMBOLO PARA EL RECTANGULO Y
# UN ANCHO Y UN ALTO PARA CREAR EL RECTANGULO.

# DEFINICIÓN DE SOLICITUDES CON VARIABLES:

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
simbolo = input("Ingrese el simbolo: ")

# CICLO FOR ANIDADO:
for i in range(filas):
    for j in range(columnas):
        print(simbolo, end="")
    print()
print()