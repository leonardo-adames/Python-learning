# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (`Las Tuplas`)

## 11.2.4 `Desempaquetar Tuplas` en python

### Desempaquetando una Tupla

Cuando creamos una tupla, normalmente le asignamos valores. Esto se llama "empaquetar" una tupla:

### Ejemplo

Empaquetar una tupla:

```python
fruits = ("apple", "banana", "cherry")
```

Pero, en Python, también se nos permite extraer los valores de nuevo en variables. Esto se llama "desempaquetar":

Desempaquetando una tupla:

```python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

**Nota:** El número de variables debe coincidir con el número de valores en la tupla, si no, debes usar un asterisco para recopilar los valores restantes como una lista.

**Uso de asterisco**

Si el número de variables es menor que el número de valores, puedes añadir un al nombre de la variable y el Se asignarán valores a la variable como una lista:*

Asigna el resto de valores en una lista llamada "`rojo`":

```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
```

Si el asterisco se añade a otro nombre de variable distinto al anterior, Python asignará valores a la variable hasta que el número de valores restantes coincida con el número de variables restantes.

Añade una lista de valores a la variable "`trópica`":

```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
```
