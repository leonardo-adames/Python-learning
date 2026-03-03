'''
# ejemplo De una división con manejo de errores:

try:
    number_1 = int(input("Ingrese un número: "))
    number_2 = int(input("Ingrese otro número: "))
    resultado = number_1 / number_2
   
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.\n")
except Exception as e:
    print(f"Ocurrió otro error: {e}")
else:
    print(f'La división fue exitosa: {resultado:.2f}')
finally:
    print('Este bloque siempre se ejecuta.')


# Lanzando excepciones raise
def validate_age(age):
    age = int(input("Ingrese su edad: "))
    if age < 18:
        raise ValueError("La edad debe ser mayor o igual a 18 para realizar esta acción")
    else:
        print("Edad válida.")
    return True

validate_age(0)


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
'''

a = 5
b=  2

print(a + b)