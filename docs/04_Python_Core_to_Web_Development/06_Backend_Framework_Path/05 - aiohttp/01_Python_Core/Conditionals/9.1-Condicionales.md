# BootCamp Python Sesión 9 - Condicionales

## 9.1 Condicionales en python

* En Python, los condicionales son estructuras de control de flujo de ejecución  permiten a un programa ejecutar diferentes bloques de código dependiendo de si una condición es verdadera (`True`) o falsa (`False`).

El `flujo de ejecución` de un programa es el orden en que se ejecutan sus instrucciones, generalmente de forma secuencial (`arriba hacia abajo`), pero puede desviarse mediante estructuras de control (condicionales como `if`/`else`, bucles como `for`/`while`) que permiten tomar decisiones, repetir tareas o saltar a otras partes del código, haciéndolo dinámico y adaptable. 

Las sentencias principales son: `if`, `elif` y `else`.

Sintaxis básica

```python
if condicion:
    Código si la condición es verdadera

elif otra_condicion:
    Código si la primera condición es falsa y esta es verdadera
    
else:
    Código si ninguna condición anterior es verdadera

```

## EJEMPLO PRACTICO

### Programa que clasifica un número

```python
try:
    numero = float(input("Introduce un número: "))

    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

except ValueError:
    print("Error: Debes introducir un valor numérico.")
```

### Explicación

* **if:** Evalúa la primera condición.

* **elif:** Evalúa condiciones adicionales si las anteriores fueron falsas.

* **else:** Captura todos los casos restantes.

* **try-except:** Maneja errores si el usuario introduce algo que no es un número.

### Operadores comunes en condicionales

* **Comparación:** ==, !=, <, >, <=, >=

* **Lógicos:** and, or, not

* **Pertenencia:** in, not in

### Ejemplo con múltiples condiciones + Operador Lógico

```python
edad = 20
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")
```
