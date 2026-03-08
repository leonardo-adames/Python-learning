# Bootcamp Python SESIÓN 3 -  VARIABLES & CONSTANTES

## 6. VARIABLES DE ENTRADA

### Introducción de information por teclado y almacenarla

En Python, podemos solicitar al usuario que introduzca información a través del teclado utilizando la función `input()`. Esta función pausa la ejecución del programa y espera a que el usuario escriba algo y presione Enter. El valor introducido por el usuario se devuelve como una cadena de texto (string).

**Podemos utilizarlo para:**

* Hacer selección de opciones.

* Introducir información personalizada.

* entre otras cosas más.

**Las posibilidades son muchas.**

#### Ejemplo 1: básico de uso de `input()`

```python
nombre = input("Por favor, introduce tu nombre: ")
print("Hola, " + nombre + "!")
```

En este ejemplo, el programa solicita al usuario que introduzca su nombre y luego lo saluda utilizando el nombre proporcionado.

esto se puede usar para cualquier tipo de dato, pero es importante recordar que `input()` siempre devuelve una cadena. Si necesitamos otro tipo de dato, como un número entero o un número decimal, debemos convertir la cadena a ese tipo utilizando las funciones `int()` o `float()`.

#### Ejemplo 2: conversión de tipos

```python
edad = input("Por favor, introduce tu edad: ")
edad = int(edad)  # Convertimos la cadena a un entero
print("El próximo año tendrás " + str(edad + 1) + " años.")
```

En este ejemplo, el programa solicita al usuario que introduzca su edad, convierte la entrada a un entero y luego calcula cuántos años tendrá el usuario el próximo año.

#### Ejemplo 3: uso de `input()` para selección de opciones

```python
opcion = input("Elige una opción (1, 2 o 3): ")
opcion = input("Elige una opción (1, 2 o 3): ")
if opcion == "1":
    print("Has elegido la opción 1.")
elif opcion == "2":
    print("Has elegido la opción 2.")
elif opcion == "3":
    print("Has elegido la opción 3.")
else:
    print("Opción no válida.")
```

En este ejemplo, el programa solicita al usuario que elija una opción entre 1, 2 o 3 y responde en consecuencia.

### Resumen

La función `input()` es una herramienta poderosa en Python que nos permite interactuar con el usuario y obtener información personalizada. Recuerda siempre convertir la entrada a los tipos de datos necesarios para tu programa.

### ---¡Ahora es tu turno! Prueba a crear un programa que solicite al usuario su nombre y edad, y luego imprima un mensaje personalizado utilizando esa información.
