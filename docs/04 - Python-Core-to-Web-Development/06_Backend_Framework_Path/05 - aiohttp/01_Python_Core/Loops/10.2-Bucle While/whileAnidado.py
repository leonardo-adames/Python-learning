# EJERCICIO DE WHILE ANIDADO

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
simbolo = input("Ingrese el símbolo: ")

i = 0
while i < filas:          # controla las filas
    j = 0
    while j < columnas:   # controla las columnas
        print(simbolo, end="")
        j += 1            # incrementa columnas
    print()
    i += 1                # incrementa filas
