'''
# Ejercicios con Iteradores e Iterables
print("\n====Trabajando con iteradores e iterables====\n")

print("\nCreación de un Iterador A partir de un Iterable")

empleados= ["Juan", "María", "Pedro", "Ana", "Luis", "Lucía", "Carlos", "Carmen", "Manuel", "Marta"]
it = iter(empleados)

for i in it:
    print(i)


print("\nUsando iteradores en funciones y métodos")

def recorrer(iterable):
    iterator = iter(iterable)
    while True:
        try:
            elemento = next(iterator)
            print(elemento)
        except StopIteration:
            break

coordenadas = (49.5000,-123.5000)
recorrer(coordenadas)

# Salida: 49.5000, -123.5000
'''