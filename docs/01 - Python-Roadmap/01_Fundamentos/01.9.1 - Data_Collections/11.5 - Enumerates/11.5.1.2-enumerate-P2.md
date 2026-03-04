# Learning Python Level 1 - Sesión 11 Colecciónes

## 11.5.1 - Enumerate - Iterar con índices en Python P2

### Creando un diccionario a partir de `enumerate()`

**Creando un diccionario a partir de `enumerate()`**<br>
En este ejemplo, enumerate se usa en una comprensión de diccionario para crear un diccionario que mapea índices a valores de una lista de países.

```python
paises = ['España', 'Francia', 'Italia']

diccionario_paises = {indice: pais for indice, pais in enumerate(paises)}
print(diccionario_paises)

# Salida: {0: 'España', 1: 'Francia', 2: 'Italia'}
```
**QUÉ ESTÁ PASANDO EN ESTEEJEMPLO:**

En este ejemplo, vamos a desglosar lo que está pasando línea por línea:

```python
paises = ['España', 'Francia', 'Italia']
```
>-Aquí se crea una lista de países.

```python
diccionario_paises = {indice: pais for indice, pais in enumerate(paises)}
```
Aquí esta pasando tres cosas:
>-`diccionario_paises` : Aquí se define la variable diccionario_paises.<br>
>-`for indice, pais in enumerate(paises)` : Aquí se define el bucle for que recorre la lista de países.<br>
>-`print(diccionario_paises)` : Aquí se imprime el diccionario resultante.