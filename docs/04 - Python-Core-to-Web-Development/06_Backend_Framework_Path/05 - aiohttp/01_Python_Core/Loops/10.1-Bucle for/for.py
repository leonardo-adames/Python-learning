'''
# for básico
for i in range(3, -13, -1):
    print(f'El valor de i es: {i}')


# Iterando una lista con for
numbers = [6, 5, 3, 5, 3]
total = 0

for number_value in numbers:
    total += number_value   # 6, 11, 14, 19, 22
    print(f"Total: {total}")

# resultado => total = 22

# For con if con continue
colores = ["rojo", "verde", "azul", "amarillo", "negro", "blanco", "gris", "morado", "naranja"]

print("====Listado de colores====""\n")

for color in colores:
    if color == "amarillo" or color == "negro":
        print('-Color saltado...')
        continue
    print(f'-Color: {color}')

print("\n====Fin del listado====")

'''

# For con if con break
colores = ["rojo", "verde", "azul", "amarillo", "negro", "blanco", "gris", "morado", "naranja"]

print("====Listado de colores====""\n")

for color in colores:
    if color == "amarillo":
        print('-Color amarillo encontrado, deteniendo la ejecución...')
        break
    print(f'- {color}')

print("\n====Fin del listado====")
