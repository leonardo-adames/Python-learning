# BootCamp Python Sesión 6 - Los Operadores

## 6.2 Operadores Aredméticos ==> (`+, -, *, **,  /, %,  #, //`)

### ¿Qué son?

lOS OPERADORES ARIDMÉTICOS CONSISTEN EN REALIZAR CÁLCULOS NUMÉRICOS (`Sumar, Restar, Multiplicar, Dividir, Hacer Potenciación, etc`), y estas son las bases de cualquier programa que trabaje con números `ESTADISTICAS Y CIENCIA DE DATOS`.

```python
# Variables de ejemplo:
a = 6

b = 28

# APLICACIÓN DE OPERADORES ARIDMÉTICOS EN CÁLCULOS NUMÉRICOS:
print(f"a ={b}, a ={b}")    #igualdad
print("a + b", a + b)       #suma
print("a - b", a - b)       #resta
print("a * b", a * b)       #multiplicación
print("a ** b", a ** b)     #realiza exponenciación (“elevar un número a la potencia de otro)
print("a / b", a / b)       #divide
print("a // b", a // b)     #realiza divisiones enteras (floor division)
print("a % b", a % b)       #Decuelve el reducido de la dicisión de dos números
print()
```

OPERACIONES ARIDMÉTICAS BÁSICAS:

```python
# OPERACIONES BÁSICAS
print("Suma (5 + 3):", 5 + 3)
print("Resta (10 - 4):", 10 - 4)
print("Multiplicación (6 * 7):", 6 * 7)
print("División (15 / 2):", 15 / 2)
print("División entera (15 // 2):", 15 // 2)
print("Módulo/residuo (15 % 2):", 15 % 2)
print("Potencia (2 ** 5):", 2 ** 5)
```

## Jerarquía de operaciones

EN PYTHON LA JERARQUÍA DE OPERACIONES SE REFIERE AL NIVEL DE PRIORIDAD
QUE SE LE DA A UNA OPERACIÓN NUMÉRICA O MATEMÁTICA SEGÚN SU ESTRUCTURA SINTAXICA O ECUACIONAL.
SEGÚN LAS MATÉMATICAS DENTRO DE UNA OPERACIÓN ESTE ES EL NIVEL JERARQUICO DE PRIORIDAD SEGÚN LA EJECUCIÓN DE UNA OPERACIÓN.

```python
print("Sin paréntesis 3 + 5 * 2:", 3 + 5 * 2)
print("Con paréntesis (3 + 5) * 2:", (3 + 5) * 2)
```

## REGLAS DE JERARQUÍA DE OPERACIONES

**1. Paréntesis:**

    Todo lo que esté dentro de () se resuelve primero.
    Si hay paréntesis dentro de paréntesis, se resuelven de adentro hacia afuera.

**2. Exponentes:**

    Incluye potencias y raíces.
    En Python estos se represetan don el operador el operador (**).

Ejemplo:

    (2 ** 3) se resuelve antes que multiplicaciones o sumas.

**3. Multiplicación, División, División entera, Módulo:**

Todos estos tienen el mismo nivel de prioridad:

    * (multiplicación).

    / (división).

    // (división entera).

    % (módulo).

    Se resuelven de izquierda a derecha segun el orden de su posición.

**4. Suma y Resta:**

    Tienen la prioridad más baja entre los operadores aritméticos por lo que se terminan resolviendo al final.

## OPERACIONES CON DECIMALES

Suma decimal

```python
(2.5 + 3.7):", 2.5 + 3.7)
```

"Multiplicación decimal

```python
(1.5 * 4):", 1.5 * 4)
```

ESTAS OPERACIONES SON PRACTICAMENTE LO MISMO QUE CON LOS NUMEROS ENTEROS
SOLO QUE CAMBIA EL TIPO DE DATOS.

OPERACIÓN COMBINADA:

```python
resultado = (10 + 5) * 2 ** 3 / 4 - 2
print("(10 + 5) * 2 ** 3 / 4 - 2 =", resultado)
```

Las operaciones combinadas son cálculos donde se mezclan diferentes tipos de operaciones aritméticas dentro de una sola expresión,
y Python debe decidir qué se ejecuta primero para obtener el resultado correcto.

### ¿Para qué sirven?

Sirven para realizar cálculos más complejos en una sola línea, permitiendo:

* simplificar código
* expresar fórmulas matemáticas reales (áreas, promedios, conversiones, etc.)
* controlar el orden de ejecución usando paréntesis

### 5. Trabajando con variables

USO DE VARIABLES:

```python
a = 20
b = 6
print(f"a = {a}, b = {b}")
print("a + b =", a + b)
print("a * b - 10 =", a * b - 10)
```

trabajar operadores aritméticos con variables en Python es poder realizar cálculos dinámicos,
usando valores que pueden cambiar durante la ejecución del programa.

### ¿Por qué es importante?

-Permite manejar datos cambiantes
-Si los valores se guardan en variables, puedes cambiar el valor sin modificar toda la operación.
