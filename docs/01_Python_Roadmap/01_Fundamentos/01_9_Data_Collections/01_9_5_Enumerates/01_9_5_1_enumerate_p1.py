'''
# Function Enumerate()
nombres = ['Luis', 'María', 'Carlos', 'Ana']

for indice, nombre in enumerate(nombres):
    print(f'índice {indice}: {nombre}')

#SALIDA:
#índice 0: Luis
#índice 1: María
#índice 2: Carlos
#índice 3: Ana


# Function Enumerate() con inicio
nombres = ['Luis', 'María', 'Carlos', 'Ana']

for indice, nombre in enumerate(nombres, start=1):
    print(f'Estudiante {indice}: {nombre}')


# Function Enumerate() con cadenas
cadena = 'Python'

for indice, caracter in enumerate(cadena):
    print(f'indice {indice}: {caracter}')

#SALIDA:
# Índice 0: P
# Índice 1: y
# Índice 2: t
# Índice 3: h
# Índice 4: o
# Índice 5: n


# Creando un diccionario a partir de enumerate()
print("\n")
print("Creando un diccionario a partir de enumerate()")

paises = ['España', 'Francia', 'Italia']
diccionario_paises = {indice: pais for indice, pais in enumerate(paises)}

print("Lista de paises antes de crear el diccionario:", paises)
print("\n")
print("Resultado:")
print("Diccionario de paises:", diccionario_paises)

#SALIDA:
# Lista de paises antes de crear el diccionario: ['España', 'Francia', 'Italia']
# 
# Resultado: 
# Diccionario de paises: {0: 'España', 1: 'Francia', 2: 'Italia'}
'''

# Convirtiendo enumerate() a lista de tuplas
print("\nConvertido a Lista:")

paises = ['España', 'Francia', 'Italia']
enumerado = list(enumerate(paises, start=1))
print("Lista de paises convertida a lista:",enumerado)

#SALIDA:
# Lista de paises convertida a lista: 
# [(1, 'España'), (2, 'Francia'), (3, 'Italia')]



