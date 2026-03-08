# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Conjuntos `set`)

## 11.3.4 `Bucles En Set` en python

### Elementos Del Bucle

Puedes recorrer los elementos del conjunto usando un bucle:for

### Ejemplo

Haz un bucle por el conjunto e imprime los valores:

```python
# Definimos un conjunto
frutas = {"manzana", "banana", "cereza"}

# Recorremos el conjunto con un bucle for
for fruta in frutas:
    print(fruta)

```

### Ejemplo con validación y operaciones

```python
# Creamos un conjunto con elementos repetidos (los duplicados se eliminan automáticamente)
numeros = {1, 2, 3, 3, 4, 5}

# Validamos que sea un set
if isinstance(numeros, set):
    print("Recorriendo el conjunto:")
    for num in numeros:
        if num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
else:
    print("El objeto no es un conjunto")

```

### Usando enumerate() para obtener índice y valor

Aunque los set no tienen índices reales, `enumerate()` asigna un contador durante la iteración:

```python
colores = {"rojo", "verde", "azul"}

for i, color in enumerate(colores, start=1):
    print(f"{i}. {color}")

```

### Puntos clave

* Los set no permiten duplicados.
* No tienen un orden fijo.
* Puedes recorrerlos con for o convertirlos a lista si necesitas orden:

``` python
for elemento in sorted(frutas):
    print(elemento)

```
