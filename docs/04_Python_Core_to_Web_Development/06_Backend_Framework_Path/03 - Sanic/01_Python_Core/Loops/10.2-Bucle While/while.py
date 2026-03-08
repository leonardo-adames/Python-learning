'''
i = 1                                # Declaración de nuestra  condición

while i < 10:
    print(f'El valor de i es: {i}')
    i += 1                           # contador o incremento para evitar bucle infinito

# RESULTADO:
# El valor de i es: 1
# El valor de i es: 2
# El valor de i es: 3
# El valor de i es: 4
# El valor de i es: 5
# El valor de i es: 6
# El valor de i es: 7
# El valor de i es: 8
# El valor de i es: 9

# EL 10 NO SE IMPRIME PORQUE LA CONDICIÓN ES < 10, 
# Y EN PYTHON EL ÚLTIMO ÍNDICE ES EXCLUSIVO

# EL INCREMENTO Y DECREMENTO 
# CON i-- o i++ NO EXIXTE EN PYTHON,
# SE DEBE USAR i += 1 o i -= 1

#EJEMPLO DE BUCLE QUE NO SE EJECUTA:

i = 1

while i <= 0:
    print(f'El valor de i es: {i}')
    i += 1


# ESTA NO DA ERROR AL EJECUTAR, PERO NO SALE NADA
# POR QUÉ PASA ESTO?
# PORQUE LA CONDICIÓN i <= 0 NO SE CUMPLE DESDE EL PRINCIPIO
# Y POR LO TANTO EL BUCLE NO SE EJECUTA.

# UNA POSIBLE SOLUCIÓN PARA ESTO SERÍA EL BUCLE "DO WHILE",
# QUE LO QUE HACE ES QUE PERMITE QUE SE EJECUTE EL BUCLE UNA VEZ 
# AUNQUE NO SE CUMPLA LA CONDICIÓN, PERO EN PYTHON NO EXISTE
# LA SOLUCIÓN EN PYTHON EN PRINCIPIO SERÍA DARLE UNA SALIDA ELTERNATIVA
# A NUESTRO PROGRAMA SI DICHA CONDICIÓN NO SE CUMPLE Y QUEREMOS
# QUE SE EJECUTE EL CÓDIGO DE TODAS FORMAS, EJEMPLO:

while True:
    salida = input("Introduce 'salir' para terminar.\n").lower()
    if salida == "salir":
        break
'''

